import unittest
import os
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up a clean environment before each test."""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "test_file.json"

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the 'all' method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        self.assertEqual(objects, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test the 'new' method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_save_and_reload(self):
        """Test the 'save' and 'reload' methods."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = f"{obj.__class__.__name__}.{obj.id}"

        self.assertIn(key, new_storage.all())

        reloaded_obj = new_storage.all()[key]
        self.assertIsInstance(reloaded_obj, BaseModel)

        self.assertEqual(reloaded_obj.id, obj.id)

if __name__ == "__main__":
    unittest.main()
