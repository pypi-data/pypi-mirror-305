import unittest
from ethio_date_converter.converter import EthiopianDateConverter
import datetime


class TestEthiopianDateConverter(unittest.TestCase):

    def test_date_to_gregorian(self):
        # Test Ethiopian date to Gregorian date conversion
        ethiopian_date = datetime.date(2017, 4, 10)  # Example Ethiopian date
        expected_gregorian_date = datetime.date(2024, 10, 18)  # Corresponding Gregorian date
        self.assertEqual(EthiopianDateConverter.date_to_gregorian(ethiopian_date), expected_gregorian_date)

    def test_date_to_ethiopian(self):
        # Test Gregorian date to Ethiopian date conversion
        gregorian_date = datetime.date(2024, 10, 18)  # Example Gregorian date
        expected_ethiopian_date = (2017, 4, 10)  # Corresponding Ethiopian date
        self.assertEqual(EthiopianDateConverter.date_to_ethiopian(gregorian_date), expected_ethiopian_date)

    def test_invalid_date(self):
        # Test invalid date conversion
        with self.assertRaises(ValueError):
            EthiopianDateConverter.to_gregorian(0, 0, 0)  # Invalid input
        with self.assertRaises(ValueError):
            EthiopianDateConverter.to_ethiopian(1582, 10, 10)  # Invalid date


if __name__ == '__main__':
    unittest.main()
