import unittest

from canatax.calculators import IncomeTaxCalculator
from canatax.enums import ProvinceOrTerritory
from canatax.exc import InvalidDollarAmount
from canatax.tax_estimate import IncomeTaxEstimate
from canatax.rates.income_rates import *



class TestIncomeCalculator(unittest.TestCase):

    def test_calculate_return_type(self):

        income = 100000
        for province in ProvinceOrTerritory:
            with self.subTest(province=province):
                calc = IncomeTaxCalculator(income=income, province=province)
                tax_estimate = calc.calculate_all()
                self.assertIsInstance(tax_estimate, IncomeTaxEstimate)


    def test_valid_incomes(self):
        valid_incomes = [0, 1, 0.1, 0.0001, 10, 100000, 95439534942239, 2552.45, 25235.523523]
        for income in valid_incomes:
            with self.subTest(income=income):
                calc = IncomeTaxCalculator.calculate(income=income, province="BC")
                self.assertIsInstance(calc, IncomeTaxEstimate)


    def test_invalid_incomes(self):
        invalid_incomes = [-23525, None, 'asdf', float('inf'), float('nan')]
        for income in invalid_incomes:
            with self.subTest(income=income):
                with self.assertRaises(InvalidDollarAmount):
                    calc = IncomeTaxCalculator.calculate(income=income, province="BC")


if __name__ == '__main__':
    unittest.main()