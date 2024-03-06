import unittest
import pandas as pd
from datetime import datetime

class TestDataValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_excel('HINDALCO_1D.xlsx')

    def test_valid_decimal_values(self):
        for col in ['open', 'high', 'low', 'close']:
            with self.subTest(column=col):
                self.assertTrue(all(isinstance(val, float) for val in self.df[col]), f"{col} is not decimal")

    def test_valid_integer_volume(self):
        self.assertTrue(all(isinstance(val, int) for val in self.df['volume']), "Volume is not integer")

    def test_valid_string_instrument(self):
        self.assertTrue(all(isinstance(val, str) for val in self.df['instrument']), "Instrument is not string")

    def test_valid_datetime(self):
        self.assertTrue(all(isinstance(val, datetime) for val in self.df['datetime']), "Datetime is not datetime object")

if __name__ == '__main__':
    unittest.main()
