#!/usr/bin/python3
"""test"""

import unittest
from models.city import City
from datetime import datetime
from models import storage


class TestCity(unittest.TestCase):
    """test"""

    def setUp(self):
        """test"""
        self.city = City()

    def tearDown(self):
        """test"""
        pass

    def test_attributes(self):
        """test"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_default_values(self):
        """test"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_save_reload(self):
        """test"""
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        self.city.save()
        key = "{}.{}".format(self.city.__class__.__name__, self.city.id)
        reloaded_city = storage.all()[key]
        self.assertEqual(reloaded_city.state_id, "CA")
        self.assertEqual(reloaded_city.name, "San Francisco")

    def test_to_dict(self):
        """test"""
        self.city.state_id = "NY"
        self.city.name = "New York City"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], "NY")
        self.assertEqual(city_dict['name'], "New York City")
        self.assertEqual(city_dict['__class__'], "City")
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    def test_created_at_updated_at(self):
        """test"""
        self.assertTrue(isinstance(self.city.created_at, datetime))
        self.assertTrue(isinstance(self.city.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
