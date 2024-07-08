import unittest
from unittest.mock import patch
from io import StringIO

from task_1 import ShareCalculator


class TestShareCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ShareCalculator()

    @patch('sys.argv', ['script_name.py', '4', '1.5', '3', '6', '1.5'])
    def test_process(self):
        expected_output = "12.500\n25.000\n50.000\n12.500\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.argv', ['script_name.py', '4', '2', '2', '2', '2'])
    def test_equal_shares(self):
        expected_output = "25.000\n25.000\n25.000\n25.000\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.argv', ['script_name.py', '2', '1', '4'])
    def test_unequal_shares(self):
        expected_output = "20.000\n80.000\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.argv', ['script_name.py', '3', '1', '1', '1'])
    def test_fractional_shares(self):
        expected_output = "33.333\n33.333\n33.333\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.argv', ['script_name.py', '3', '1', '1', '1', '2'])
    def test_wrong_shares_number(self):
        err_msg = "Number of shares provided does not match the specified N."
        with self.assertRaises(ValueError) as cm:
            self.calculator.process()
        self.assertEqual(str(cm.exception), err_msg)


if __name__ == '__main__':
    unittest.main()
