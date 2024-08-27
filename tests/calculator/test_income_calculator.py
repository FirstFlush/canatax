import unittest

from canatax.calculators import IncomeTaxCalculator
from canatax.enums import ProvinceOrTerritory
from canatax.rates.income_rates import *



class TestIncomeCalculator(unittest.TestCase):


    def setUp(self):
        self.provinces:list[ProvinceOrTerritory] = [prov for prov in ProvinceOrTerritory]


    

    