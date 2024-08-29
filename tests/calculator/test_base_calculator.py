import unittest

from canatax.enums import TaxType, ProvinceOrTerritory
from canatax.calculators.base_calculator import BaseCalculator
from canatax.rates.income_rates import ProvincialIncomeTaxRate
from canatax.rates.sales_rates import BaseSalesTaxRate


class TestBaseCalculator(unittest.TestCase):

    def test_tax_rate(self):

        for tax_type in TaxType:
            for province in ProvinceOrTerritory:
                with self.subTest(tax_type=tax_type, province=province):
                    calculator = BaseCalculator(province=province)
                    match tax_type:
                        case TaxType.INCOME:
                            self.assertIsInstance(calculator._get_tax_rate(tax_type), ProvincialIncomeTaxRate)
                        case TaxType.SALES:
                            self.assertIsInstance(calculator._get_tax_rate(tax_type), BaseSalesTaxRate)
                        case _:
                            self.fail(f"Unexpected tax type `{tax_type}` or province `{province}`")


if __name__ == '__main__':
    unittest.main()
