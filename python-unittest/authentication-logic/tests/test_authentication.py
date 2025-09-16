import unittest
from unittest.mock import (Mock, MagicMock)
from authentication.authentication import UserAuthentication

# PassHash test
class TestPassHash(unittest.TestCase):

    def setUp(self):
        UA = UserAuthentication()
        self.password = input("Enter a password to hash: ")
        self.wrong_password = input("Enter a wrong password to test: ")
        self.passhash = UA.hash_password(self.password)

    def test_hash_password(self):
        hashed = self.passhash
        self.assertNotEqual(self.password, hashed)
        self.assertTrue(UA.verify_password(self.password, hashed))

    def test_verify_password(self):
        hashed = self.passhash
        self.assertTrue(UA.verify_password(self.password, hashed))
        self.assertFalse(UA.verify_password(self.wrong_password, hashed))
        self.assertFalse(UA.verify_password("", hashed))
        self.assertFalse(UA.verify_password(None, hashed))

if __name__ == '__main__':
    unittest.main()
