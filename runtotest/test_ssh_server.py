import unittest
from src.ssh_server import hash_password, authenticate
import hashlib

class TestSSHServer(unittest.TestCase):
    def test_hash_password(self):
        password = 'password1'
        hashed = hash_password(password)
        self.assertEqual(hashed, hashlib.sha256(password.encode()).hexdigest())

    def test_authenticate(self):
        self.assertTrue(authenticate('user1', 'password1'))
        self.assertFalse(authenticate('user1', 'wrongpassword'))

if __name__ == '__main__':
    unittest.main() 