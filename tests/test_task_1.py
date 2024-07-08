import unittest
from unittest.mock import patch
from io import StringIO

from task_1 import ShareCalculator


class TestShareCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ShareCalculator()

    @patch('sys.stdin', StringIO('4\n1.5\n3\n6\n1.5\n'))
    def test_process(self):
        expected_output = "0.125\n0.250\n0.500\n0.125\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.stdin', StringIO('4\n2\n2\n2\n2\n'))
    def test_equal_shares(self):
        expected_output = "0.250\n0.250\n0.250\n0.250\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.stdin', StringIO('2\n1\n4\n'))
    def test_unequal_shares(self):
        expected_output = "0.200\n0.800\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.stdin', StringIO('3\n1\n1\n1\n'))
    def test_fractional_shares(self):
        expected_output = "0.333\n0.333\n0.333\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.calculator.process()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('sys.stdin', StringIO('4\n1\n1\n1\n'))
    def test_wrong_shares_number(self):
        err_msg = "Number of shares provided does not match the specified N."
        with self.assertRaises(ValueError) as cm:
            self.calculator.process()
        self.assertEqual(str(cm.exception), err_msg)


if __name__ == '__main__':
    unittest.main()
