#!/usr/bin/python3
"""File Storage unittest"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of FileStorage for each test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up any resources or files created during the tests"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_save_and_reload(self):
        """Test the save and reload methods"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())
        self.assertIsInstance(new_storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
