import unittest

from mailswan.db import User


class UserTestCase(unittest.TestCase):

    def test_when_created_with_salt_given_should_have_given_salt(self):
        user = User('user@example.com', 'somepassword', salt='somesalt')
        self.assertEquals(user.salt, 'somesalt')

    def test_when_created_with_no_salt_should_use_random_salt(self):
        user = User('user@example.com', 'somepassword')
        self.assertIsNotNone(user.salt)

    def test_salt_should_be_concatenated_with_password_before_hashing(self):
        user = User('user@example.com', 'somepass', salt='somesalt')
        self.assertEquals(
            User.hash_password('somepass', 'somesalt'),
            user.password_hash
        )
