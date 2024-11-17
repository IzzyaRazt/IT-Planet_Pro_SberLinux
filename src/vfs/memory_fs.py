import unittest
from src.memory_fs import MemoryFS
import os
import stat
from fuse import FuseOSError

class TestMemoryFS(unittest.TestCase):
    def setUp(self):
        self.fs = MemoryFS()

    def test_create_and_getattr(self):
        self.fs.create('/testfile', 0o755)
        attr = self.fs.getattr('/testfile')
        self.assertEqual(attr['st_mode'], (stat.S_IFREG | 0o755))

    def test_mkdir_and_readdir(self):
        self.fs.mkdir('/testdir', 0o755)
        contents = self.fs.readdir('/')
        self.assertIn('testdir', contents)

    def test_unlink(self):
        self.fs.create('/testfile', 0o755)
        self.fs.unlink('/testfile')
        with self.assertRaises(FuseOSError):
            self.fs.getattr('/testfile')

if __name__ == '__main__':
    unittest.main() 