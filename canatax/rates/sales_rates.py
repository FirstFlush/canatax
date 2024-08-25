


class BaseSalesTaxRate:

    GST = None
    PST = None
    HST = None

    @property
    def rate(self) -> float:
        applicable_taxes = [tax for tax in self.tax_types if tax is not None]
        if not applicable_taxes:
            raise AttributeError(f"`{self.__class__.__name__}`: GST, PST, and HST are all None type!")
        return sum(applicable_taxes)

    @property
    def tax_types(self) -> list[float|None]:
        return [self.GST, self.PST, self.HST]

class AlbertaSalesTaxRate(BaseSalesTaxRate):
    
    GST = 5
    PST = None
    HST = None


class BritishColumbiaSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = 7
    HST = None


class ManitobaSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = 7
    HST = None


class QuebecSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = 9.975
    HST = None


class PEISalesTaxRate(BaseSalesTaxRate):
        
    GST = None
    PST = None
    HST = 15


class NovaScotiaSalesTaxRate(BaseSalesTaxRate):
        
    GST = None
    PST = None
    HST = 15


class NewBrunswickSalesTaxRate(BaseSalesTaxRate):
        
    GST = None
    PST = None
    HST = 15


class NewfoundlandSalesTaxRate(BaseSalesTaxRate):
        
    GST = None
    PST = None
    HST = 15


class NunavutSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = None
    HST = None


class NorthwestTerritoriesSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = None
    HST = None


class SaskatchewanSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = 6
    HST = None


class OntarioSalesTaxRate(BaseSalesTaxRate):
        
    GST = None
    PST = None
    HST = 13


class YukonSalesTaxRate(BaseSalesTaxRate):
        
    GST = 5
    PST = None
    HST = None
