from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from task_2 import main


class TestMegaTrader(TestCase):

    @patch('builtins.input',
           side_effect=['2 2 8000', '1 alfa-05 100.2 2', '2 alfa-05 101.5 5', '2 gazprom-17 100.0 2', ''])
    def test_max_profit(self, _):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            expected_output = "135\n2 gazprom-17 100.0 2\n2 alfa-05 101.5 5\n"
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch(
        'builtins.input',
        side_effect=[
            '2 2 8000', '1 alfa-05 100.2 2', '2 alfa-05 101.5 5', '2 gazprom-17 100.0 2', '2 sber-02 100.25 3' ''
        ]
    )
    def test_invalid_input(self, _):
        with self.assertRaises(Exception) as e:
            main()
            err_message = f"Incorrect number of lots for day 2: It should be less than M"
            self.assertEqual(str(e.exception), err_message)
