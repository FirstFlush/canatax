from canatax.calculators.base_calclulator import BaseCalculator
from canatax.enums import ProvinceOrTerritory
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


    def __init__(self, income:float|int, province:ProvinceOrTerritory):
        super().__init__(province=province)
        self.income = income
        self.federal_tax = FederalIncomeTaxRate()
        self.provincial_tax:ProvincialIncomeTaxRate = self.PROVINCE_MAPPING[self.province][0]()

    @classmethod
    def calculate(cls, income:float|int, province:str) -> IncomeTaxEstimate:
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
            federal_tax=round(federal_tax, 2),
            provincial_tax=round(provincial_tax, 2),
            ei=round(ei, 2),
            cpp=round(cpp, 2),
            total_tax=round(total_tax, 2),
            net_income=round(net_income, 2),
        )

    def _cpp(self) -> float:
        if self.income > self.CPP_MAX_EARNINGS:
            return self.CPP_MAX_AMOUNT
        else:
            return self.income * percent_to_decimal(self.CPP_RATE)

    def _ei(self) -> float:
        if self.income > self.EI_MAX_EARNINGS:
            return self.EI_MAX_AMOUNT
        else:
            return self.income * percent_to_decimal(self.EI_RATE)

    def _tax(self) -> tuple[float, float]:
        if not isinstance(self.income, (float, int)):
            raise TypeError(f"Parameter 'income' must be of type int or float, not `{type(self.income)}`")
        federal_tax = self.federal_tax.calculate_tax(self.income)
        provincial_tax = self.provincial_tax.calculate_tax(self.income)
        return federal_tax, provincial_tax
    

