from canatax.calculators.base_calclulator import BaseCalculator
from canatax.enums import ProvinceOrTerritory
from canatax.tax_estimate import SalesTaxEstimate
from canatax.rates.sales_rates import BaseSalesTaxRate
from canatax.utils import percent_to_decimal


class SalesTaxCalculator(BaseCalculator):

    def __init__(self, province:ProvinceOrTerritory):
        super().__init__(province=province)
        self.tax_rate:BaseSalesTaxRate = self.PROVINCE_MAPPING[self.province][1]() 


    @classmethod
    def quick_calc(cls, amount:float, province:ProvinceOrTerritory) -> SalesTaxEstimate:
        calculator = cls(province=province)
        return calculator.calculate(amount)


    def calculate(self, amount:float) -> SalesTaxEstimate:
        amount = float(amount)
        gst_total = amount * percent_to_decimal(self.tax_rate.GST) if self.tax_rate.GST else 0
        pst_total = amount * percent_to_decimal(self.tax_rate.PST) if self.tax_rate.PST else 0
        hst_total = amount * percent_to_decimal(self.tax_rate.HST) if self.tax_rate.HST else 0
        tax_total = gst_total + pst_total + hst_total
        after_tax_total = amount + tax_total
        return SalesTaxEstimate(
            province=self.province,
            before_tax_total=amount,
            tax_total=tax_total,
            after_tax_total=after_tax_total,
            gst_total=gst_total,
            pst_total=pst_total,
            hst_total=hst_total,
        )