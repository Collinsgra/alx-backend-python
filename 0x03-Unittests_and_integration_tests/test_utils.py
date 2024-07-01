#!/usr/bin/env python3
""" Parameterize a unit test
"""


import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()
            # Access a_property twice
            result1 = instance.a_property
            result2 = instance.a_property
            
            # Ensure a_method was called only once
            mock_method.assert_called_once()
            # Check the result is as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
