from decimal import Decimal
import unittest
from canatax.calculators import SalesTaxCalculator
from canatax.enums import ProvinceOrTerritory
from canatax.exc import InvalidProvinceError
from canatax.tax_estimate import SalesTaxEstimate


class TestSalesTaxCalculator(unittest.TestCase):

    def setUp(self):
        self.alberta_calculator = SalesTaxCalculator(province=ProvinceOrTerritory.ALBERTA)
        self.bc_calculator = SalesTaxCalculator(province=ProvinceOrTerritory.BRITISH_COLUMBIA)


    def test_invalid_province(self):
        invalid_provinces = ['InvalidProvince', 'ZZ', '123', None, ProvinceOrTerritory]
        for invalid_province in invalid_provinces:
            with self.assertRaises(InvalidProvinceError):
                SalesTaxCalculator(province=invalid_province)


    def test_sales_tax_alberta(self):
        estimate = self.alberta_calculator.calculate(100.0)
        self.assertEqual(estimate.gst_total, Decimal(5.0))
        self.assertEqual(estimate.pst_total, Decimal(0.0))
        self.assertEqual(estimate.hst_total, Decimal(0.0))
        self.assertEqual(estimate.tax_total, Decimal(5.0))
        self.assertEqual(estimate.after_tax_total, Decimal(105.0))


    def test_sales_tax_british_columbia(self):
        estimate = self.bc_calculator.calculate(100.0)
        self.assertEqual(estimate.gst_total, Decimal(5.0))
        self.assertEqual(estimate.pst_total, Decimal(7.0))
        self.assertEqual(estimate.hst_total, Decimal(0.0))
        self.assertEqual(estimate.tax_total, Decimal(12.0))
        self.assertEqual(estimate.after_tax_total, Decimal(112.0))


if __name__ == '__main__':
    unittest.main()