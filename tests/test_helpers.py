import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from types import SimpleNamespace

S = Path(__file__).resolve().parents[1] / 'skills/family-travel-editor/scripts'
sys.path.insert(0, str(S))
from timeline import build
from project import catalog
from resolve_bridge import guarded_import


class Helpers(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)
        self.media = self.root / 'media'; self.media.mkdir()
        (self.media / 'clip space.mp4').write_bytes(b'test fixture, not real video')
        self.plan = {'fps': 25, 'width': 640, 'height': 360,
                     'shots': [{'path': 'clip space.mp4', 'in': 25, 'out': 75, 'source_frames': 100}]}
    def tearDown(self):
        self.tmp.cleanup()
    def test_range_and_uri(self):
        output = self.root / 'cut.xml'
        self.assertEqual(build(self.plan, self.media, output), 50)
        xml = ET.parse(output)
        self.assertEqual(xml.findtext('.//clipitem/in'), '25')
        self.assertEqual(xml.findtext('.//clipitem/out'), '75')
        self.assertEqual(xml.findtext('.//clipitem/end'), '50')
        self.assertIn('clip%20space.mp4', xml.findtext('.//pathurl'))
        with self.assertRaises(FileExistsError): build(self.plan, self.media, output)
    def test_invalid_ranges(self):
        for start,end in [(0,101),(50,50),(-1,20)]:
            self.plan['shots'][0].update({'in':start,'out':end})
            with self.assertRaises(ValueError): build(self.plan,self.media,self.root/'bad.xml')
        self.assertFalse((self.root/'bad.xml').exists())
    def test_path_escape(self):
        (self.root/'outside.mp4').write_bytes(b'private')
        self.plan['shots'][0]['path']='../outside.mp4'
        with self.assertRaises(ValueError): build(self.plan,self.media,self.root/'bad.xml')
    def test_unsupported_rate(self):
        self.plan['fps']=29.97
        with self.assertRaises(ValueError): build(self.plan,self.media,self.root/'bad.xml')
    def test_catalog_hash_and_no_overwrite(self):
        report=self.root/'catalog.json'
        self.assertEqual(catalog(self.media,report,ffprobe='definitely-unavailable-probe'),1)
        data=json.loads(report.read_text())['files'][0]
        self.assertEqual(data['metadata_status'],'unavailable');self.assertEqual(len(data['sha256']),64)
        with self.assertRaises(FileExistsError):catalog(self.media,report)
        with self.assertRaises(ValueError):catalog(self.media,self.media/'catalog.json')
    def test_skip_symlink(self):
        (self.root/'outside.mp4').write_bytes(b'private')
        (self.media/'link.mp4').symlink_to(self.root/'outside.mp4')
        self.assertEqual(catalog(self.media,self.root/'catalog.json','missing-probe'),1)
    def test_resolve_refuses_wrong_project(self):
        project=SimpleNamespace(GetName=lambda:'Existing film')
        resolve=SimpleNamespace(GetProjectManager=lambda:SimpleNamespace(GetCurrentProject=lambda:project))
        with self.assertRaisesRegex(RuntimeError,'explicitly named'):
            guarded_import(resolve,'unused.xml','Demo')
    def test_resolve_refuses_populated_project(self):
        project=SimpleNamespace(GetName=lambda:'Demo',GetTimelineCount=lambda:1,
            GetMediaPool=lambda:SimpleNamespace(GetRootFolder=lambda:None))
        resolve=SimpleNamespace(GetProjectManager=lambda:SimpleNamespace(GetCurrentProject=lambda:project))
        with self.assertRaisesRegex(RuntimeError,'populated'):
            guarded_import(resolve,'unused.xml','Demo')


if __name__ == '__main__': unittest.main()
