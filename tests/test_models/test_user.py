"""user tests"""
import unittest
from models.user import User
from models.base_model import BaseModel
class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_attributes(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_instance_of_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

if __name__ == '__main__':
    unittest.main()
