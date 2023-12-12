#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = BaseModel()

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            output = mock_stdout.getvalue().strip()


if __name__ == '__main__':
    unittest.main()
