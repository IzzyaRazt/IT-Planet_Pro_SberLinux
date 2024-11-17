import unittest
import os
import shutil
from src.backup_system import incremental_backup, differential_backup

class TestBackupSystem(unittest.TestCase):
    def setUp(self):
        self.src = '/tmp/src'
        self.dst = '/tmp/dst'
        self.full_backup_dir = '/tmp/full_backup'
        os.makedirs(self.src, exist_ok=True)
        os.makedirs(self.dst, exist_ok=True)
        os.makedirs(self.full_backup_dir, exist_ok=True)
        with open(os.path.join(self.src, 'file1.txt'), 'w') as f:
            f.write('Content')

    def tearDown(self):
        shutil.rmtree(self.src)
        shutil.rmtree(self.dst)
        shutil.rmtree(self.full_backup_dir)

    def test_incremental_backup(self):
        incremental_backup(self.src, self.dst)
        self.assertTrue(os.path.exists(os.path.join(self.dst, 'file1.txt')))

    def test_differential_backup(self):
        shutil.copytree(self.src, self.full_backup_dir, dirs_exist_ok=True)
        with open(os.path.join(self.src, 'file2.txt'), 'w') as f:
            f.write('New content')
        differential_backup(self.src, self.dst, self.full_backup_dir)
        self.assertTrue(os.path.exists(os.path.join(self.dst, 'file2.txt')))

if __name__ == '__main__':
    unittest.main() 