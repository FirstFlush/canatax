from decimal import Decimal, ROUND_HALF_UP
from canatax.calculators.base_calculator import BaseCalculator
from canatax.enums import ProvinceOrTerritory, TaxType
from canatax.tax_estimate import IncomeTaxEstimate
from canatax.rates.income_rates import *
from canatax.utils import percent_to_decimal


class IncomeTaxCalculator(BaseCalculator):

    EI_RATE = 1.66
    EI_MAX_EARNINGS = 63200
    EI_MAX_AMOUNT = 1049.12
    CPP_RATE = 5.95
    CPP_MAX_EARNINGS = 68500
    CPP_MAX_AMOUNT = 3867.50


    def __init__(self, income:float|int|Decimal, province:ProvinceOrTerritory):
        super().__init__(province=province)
        self.income = Decimal(income).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.federal_tax = FederalIncomeTaxRate()
        self.provincial_tax:ProvincialIncomeTaxRate = self._get_tax_rate(TaxType.INCOME)


    @classmethod
    def calculate(cls, income:float|int|Decimal, province:str) -> IncomeTaxEstimate:
        try:
            province = ProvinceOrTerritory(province.upper())
        except ValueError:
            raise
        calculator = cls(
            income=income, 
            province=province
        )
        return calculator.calculate_all()


    def calculate_all(self) -> IncomeTaxEstimate: 
        federal_tax, provincial_tax = self._tax()
        ei = self._ei()
        cpp = self._cpp()
        total_tax = federal_tax + provincial_tax + ei + cpp
        net_income = self.income - total_tax
        return IncomeTaxEstimate(
            province=self.province,
            gross_income=self.income,
            federal_tax=federal_tax,
            provincial_tax=provincial_tax,
            ei=ei,
            cpp=cpp,
            total_tax=total_tax,
            net_income=net_income,
        )

    def _cpp(self) -> Decimal:
        if self.income > self.CPP_MAX_EARNINGS:
            return Decimal(self.CPP_MAX_AMOUNT).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        else:
            return (self.income * percent_to_decimal(self.CPP_RATE)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def _ei(self) -> Decimal:
        if self.income > self.EI_MAX_EARNINGS:
            return Decimal(self.EI_MAX_AMOUNT).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        else:
            return (self.income * percent_to_decimal(self.EI_RATE)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


    def _tax(self) -> tuple[Decimal, Decimal]:
        """Return federal tax and provincial tax as a tuple object."""
        if not isinstance(self.income, (Decimal)):
            raise TypeError(f"Parameter 'income' must be of type int or float, not `{type(self.income)}`")
        federal_tax = self.federal_tax.calculate_tax(self.income).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        provincial_tax = self.provincial_tax.calculate_tax(self.income).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return federal_tax, provincial_tax
    

