import unittest
import os
import json
import time
from src.version_control import ConfigFileHandler

class TestConfigFileHandler(unittest.TestCase):
    def setUp(self):
        self.version_dir = '/tmp/version_test'
        self.user_id = 'test_user'
        os.makedirs(self.version_dir, exist_ok=True)
        self.handler = ConfigFileHandler(self.version_dir, self.user_id)
        self.test_file = '/tmp/test_config.txt'
        with open(self.test_file, 'w') as f:
            f.write('Initial content')

    def tearDown(self):
        shutil.rmtree(self.version_dir)
        os.remove(self.test_file)

    def test_on_modified(self):
        with open(self.test_file, 'w') as f:
            f.write('Modified content')
        event = type('Event', (object,), {'src_path': self.test_file, 'is_directory': False})
        self.handler.on_modified(event)
        timestamp = time.strftime('%Y%m%d%H%M%S')
        version_file = os.path.join(self.version_dir, f"test_config.txt_{timestamp}.json")
        self.assertTrue(os.path.exists(version_file))

    def test_rollback(self):
        with open(self.test_file, 'w') as f:
            f.write('Modified content')
        event = type('Event', (object,), {'src_path': self.test_file, 'is_directory': False})
        self.handler.on_modified(event)
        timestamp = time.strftime('%Y%m%d%H%M%S')
        self.handler.rollback(self.test_file, timestamp)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Modified content')

if __name__ == '__main__':
    unittest.main() 