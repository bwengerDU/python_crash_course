import unittest

from Ch11_TIY import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.cale = Employee('cale', 'makar', 100_000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.cale.give_raise()
        self.assertEqual(self.cale.salary, 105000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.cale.give_raise(10000)
        self.assertEqual(self.cale.salary, 110000)

if __name__ == '__main__':
    unittest.main()