#!/usr/bin/python3
"""Test"""
import unittest
from models.user import User
from datetime import datetime
from models import storage


class TestUser(unittest.TestCase):
    def setUp(self):
        """Test"""
        self.user = User()

    def tearDown(self):
        """Test"""
        pass

    def test_attributes(self):
        """Test"""

        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        """Test"""

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_save_reload(self):
        """Test"""

        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.save()
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        reloaded_user = storage.all()[key]
        self.assertEqual(reloaded_user.email, "test@example.com")
        self.assertEqual(reloaded_user.password, "password123")
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.last_name, "Doe")

    def test_to_dict(self):
        """Test"""

        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], "User")
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_created_at_updated_at(self):
        """Test"""

        self.assertTrue(isinstance(self.user.created_at, datetime))
        self.assertTrue(isinstance(self.user.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
