#!/usr/bin/python3
"""test"""

import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """test"""

    def setUp(self):
        """test"""
        self.state = State()

    def tearDown(self):
        """test"""
        pass

    def test_attributes(self):
        """test"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_default_values(self):
        """test"""
        self.assertEqual(self.state.name, "")

    def test_save_reload(self):
        """test"""
        self.state.name = "California"
        self.state.save()
        key = "{}.{}".format(self.state.__class__.__name__, self.state.id)
        reloaded_state = storage.all()[key]
        self.assertEqual(reloaded_state.name, "California")

    def test_to_dict(self):
        """test"""
        self.state.name = "New York"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "New York")
        self.assertEqual(state_dict['__class__'], "State")
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)

    def test_created_at_updated_at(self):
        """test"""
        pass


if __name__ == "__main__":
    unittest.main()
