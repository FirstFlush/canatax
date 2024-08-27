from decimal import Decimal, ROUND_HALF_UP
from canatax.calculators.base_calculator import BaseCalculator
from canatax.enums import ProvinceOrTerritory, TaxType
from canatax.tax_estimate import SalesTaxEstimate
from canatax.rates.sales_rates import BaseSalesTaxRate
from canatax.utils import percent_to_decimal


class SalesTaxCalculator(BaseCalculator):

    def __init__(self, province:ProvinceOrTerritory):
        super().__init__(province=province)
        self.tax_rate = self._get_tax_rate(TaxType.SALES)




    @classmethod
    def quick_calc(cls, amount:float, province:ProvinceOrTerritory) -> SalesTaxEstimate:
        calculator = cls(province=province)
        return calculator.calculate(amount)


    def calculate(self, amount:float) -> SalesTaxEstimate:
        amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        gst_total = (amount * percent_to_decimal(self.tax_rate.GST)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) if self.tax_rate.GST else Decimal('0.00')
        pst_total = (amount * percent_to_decimal(self.tax_rate.PST)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) if self.tax_rate.PST else Decimal('0.00')
        hst_total = (amount * percent_to_decimal(self.tax_rate.HST)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) if self.tax_rate.HST else Decimal('0.00')
        tax_total = (gst_total + pst_total + hst_total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        after_tax_total = (amount + tax_total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return SalesTaxEstimate(
            province=self.province,
            before_tax_total=amount,
            tax_total=tax_total,
            after_tax_total=after_tax_total,
            gst_total=gst_total,
            pst_total=pst_total,
            hst_total=hst_total,
        )