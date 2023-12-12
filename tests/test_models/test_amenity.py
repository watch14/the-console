#!/usr/bin/python3
"""test"""

import unittest
from models.amenity import Amenity
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    """test"""

    def setUp(self):
        """test"""
        self.amenity = Amenity()

    def tearDown(self):
        """test"""
        pass

    def test_attributes(self):
        """test"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_default_values(self):
        """test"""
        self.assertEqual(self.amenity.name, "")

    def test_save_reload(self):
        """test"""
        self.amenity.name = "Swimming Pool"
        self.amenity.save()
        key = "{}.{}".format(self.amenity.__class__.__name__, self.amenity.id)
        reloaded_amenity = storage.all()[key]
        self.assertEqual(reloaded_amenity.name, "Swimming Pool")

    def test_to_dict(self):
        """test"""
        self.amenity.name = "Fitness Center"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Fitness Center")
        self.assertEqual(amenity_dict['__class__'], "Amenity")
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)

    def test_created_at_updated_at(self):
        """test"""
        self.assertTrue(isinstance(self.amenity.created_at, datetime))
        self.assertTrue(isinstance(self.amenity.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
