from canatax.enums import *
from canatax.exc import InvalidProvinceError
from canatax.rates.income_rates import *
from canatax.rates.sales_rates import *


class BaseCalculator:

    PROVINCE_MAPPING = {
        ProvinceOrTerritory.ALBERTA : (AlbertaIncomeTaxRate, AlbertaSalesTaxRate),
        ProvinceOrTerritory.BRITISH_COLUMBIA: (BritishColumbiaIncomeTaxRate, BritishColumbiaSalesTaxRate),
        ProvinceOrTerritory.MANITOBA : (ManitobaIncomeTaxRate, ManitobaSalesTaxRate), 
        ProvinceOrTerritory.ONTARIO : (OntarioIncomeTaxRate, OntarioSalesTaxRate),
        ProvinceOrTerritory.NEW_BRUNSWICK : (NewBrunswickIncomeTaxRate, NewBrunswickSalesTaxRate),
        ProvinceOrTerritory.NEWFOUNDLAND : (NewfoundlandIncomeTaxRate, NewfoundlandSalesTaxRate),
        ProvinceOrTerritory.NORTHWEST_TERRITORIES : (NorthwestTerritoriesIncomeTaxRate, NorthwestTerritoriesSalesTaxRate),
        ProvinceOrTerritory.NOVA_SCOTIA : (NovaScotiaIncomeTaxRate, NovaScotiaSalesTaxRate),
        ProvinceOrTerritory.NUNAVUT : (NunavutIncomeTaxRate, NunavutSalesTaxRate),
        ProvinceOrTerritory.PRINCE_EDWARD_ISLAND: (PEIIncomeTaxRate, PEISalesTaxRate),
        ProvinceOrTerritory.QUEBEC: (QuebecIncomeTaxRate, QuebecSalesTaxRate),
        ProvinceOrTerritory.SASKATCHEWAN : (SaskatchewanIncomeTaxRate, SaskatchewanSalesTaxRate),
        ProvinceOrTerritory.YUKON : (YukonIncomeTaxRate, YukonSalesTaxRate),
    }

    def __init__(self, province:str|ProvinceOrTerritory):
        """
        Initializes the calculator with a province or territory.

        Args:
            province (str | ProvinceOrTerritory): The province or territory as a string or an enum.

        Raises:
            InvalidProvinceError: If the province or territory is not valid.
        """
        if isinstance(province, str):
            try:
                self.province = ProvinceOrTerritory(province.upper())
            except ValueError as e:
                raise InvalidProvinceError() from e
        elif isinstance(province, ProvinceOrTerritory):
            self.province = province
        else:
            raise InvalidProvinceError(province)