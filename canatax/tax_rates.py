from canatax.utils import percent_to_decimal


class BaseTaxRate:
    
    brackets:None | list[tuple[float|int, int]] = None

    def calculate_tax(self, income:float|int) -> float:
        """Returns the tax owed (estimate) on a given income amount."""
        tax_owed = 0
        previous_threshold = 0
        for rate, threshold in self.brackets:
            if income > threshold:
                tax_owed += (threshold - previous_threshold) * percent_to_decimal(rate)
                previous_threshold = threshold
            else:
                tax_owed += (income - previous_threshold) * percent_to_decimal(rate)
                break
        return tax_owed


class ProvincialTaxRate(BaseTaxRate):
    ...


class FederalTaxRate(BaseTaxRate):
    """ 2024:
    ==========================
    15% 	on the portion of taxable income that is $55,867 or less, plus
    20.5% 	on the portion of taxable income over $55,867 up to $111,733, plus
    26% 	on the portion of taxable income over $111,733 up to $173,205, plus
    29% 	on the portion of taxable income over $173,205 up to $246,752, plus
    33% 	on the portion of taxable income over $246,752
    """
    brackets = [
        (15, 55867),
        (20.5, 111733),
        (26, 173205),
        (29, 246752),
        (33, float('inf')),
    ]


class AlbertaTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    10% 	on the portion of taxable income that is $148,269 or less, plus
    12% 	on the portion of taxable income over $148,269 up to $177,922, plus
    13% 	on the portion of taxable income over $177,922 up to $237,230, plus
    14% 	on the portion of taxable income over $237,230 up to $355,845, plus
    15% 	on the portion of taxable income over $355,845
    """
    brackets = [
        (10, 148269),
        (12, 177922),
        (13, 237230),
        (14, 355845),
        (15, float('inf')),
    ]


class BritishColumbiaTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    5.06% 	on the portion of taxable income that is $47,937 or less, plus
    7.7% 	on the portion of taxable income over $47,937 up to $95,875, plus
    10.5% 	on the portion of taxable income over $95,875 up to $110,076, plus
    12.29% 	on the portion of taxable income over $110,076 up to $133,664, plus
    14.7% 	on the portion of taxable income over $133,664 up to $181,232, plus
    16.8% 	on the portion of taxable income over $181,232 up to $252,752, plus
    20.5% 	on the portion of taxable income over $252,752
    """
    brackets = [
        (5.06, 47937),
        (7.7, 95875),
        (10.5, 110076),
        (12.29, 133664),
        (14.7, 181232),
        (16.8, 252752),
        (20.5, float('inf')),
    ]


class ManitobaTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    10.8% 	on the portion of taxable income that is $47,000 or less, plus
    12.75% 	on the portion of taxable income over $47,000 up to $100,000, plus
    17.4% 	on the portion of taxable income over $100,000
    """
    brackets = [
        (10.8, 47000),
        (12.75, 100000),
        (17.4, float('inf')),
    ]


class NewBrunswickTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    9.4% 	on the portion of taxable income that is $49,958 or less, plus
    14% 	on the portion of taxable income over $49,958 up to $99,916, plus
    16% 	on the portion of taxable income over $99,916 up to $185,064, plus
    19.5% 	on the portion of taxable income over $185,064
    """
    brackets = [
        (9.4, 49958),
        (14, 99916),
        (16, 185064),
        (19.5, float('inf')),
    ]



class NewfoundlandTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    8.7% 	on the portion of taxable income that is $43,198 or less, plus
    14.5% 	on the portion of taxable income over $43,198 up to $86,395, plus
    15.8% 	on the portion of taxable income over $86,395 up to $154,244, plus
    17.8% 	on the portion of taxable income over $154,244 up to $215,943, plus
    19.8% 	on the portion of taxable income over $215,943 up to $275,870, plus
    20.8% 	on the portion of taxable income over $275,870 up to $551,739, plus
    21.3% 	on the portion of taxable income over $551,739 up to $1,103,478, plus
    21.8% 	on the portion of taxable income over $1,103,478
    """
    brackets = [
        (8.7, 43198),
        (14.5, 86395),
        (15.8, 154244),
        (17.8, 215943),
        (19.8, 275870),
        (20.8, 551739),
        (21.3, 1103478),
        (21.8, float('inf')),
    ]


class NorthWestTerritoriesTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================

    """


class NovaScotiaTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    5.9% 	on the portion of taxable income that is $50,597 or less, plus
    8.6% 	on the portion of taxable income over $50,597 up to $101,198, plus
    12.2% 	on the portion of taxable income over $101,198 up to $164,525, plus
    14.05% 	on the portion of taxable income over $164,525
    """
    brackets = [
        (5.9, 50597),
        (8.6, 101198),
        (12.2, 164525),
        (14.05, float('inf')),
    ]


class NunavutTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    4% 	on the portion of taxable income that is $53,268 or less, plus
    7% 	on the portion of taxable income over $53,268 up to $106,537, plus
    9% 	on the portion of taxable income over $106,537 up to $173,205, plus
    11.5% 	on the portion of taxable income over $173,205
    """
    brackets = [
        (4, 53268),
        (7, 106537),
        (9, 173205),
        (11.5, float('inf')),
    ]


class OntarioTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    5.05% 	on the portion of taxable income that is $51,446 or less, plus
    9.15% 	on the portion of taxable income over $51,446 up to $102,894, plus
    11.16% 	on the portion of taxable income over $102,894 up to $150,000, plus
    12.16% 	on the portion of taxable income over $150,000 up to $220,000, plus
    13.16% 	on the portion of taxable income over $220,000
    """
    brackets = [
        (5.05, 51446),
        (9.15, 102894),
        (11.16, 150000),
        (12.16, 220000),
        (13.16, float('inf')),
    ]


class PEITaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    9.65% 	on the portion of taxable income that is $32,656 or less, plus
    13.63% 	on the portion of taxable income over $32,656 up to $64,313, plus
    16.65% 	on the portion of taxable income over $64,313 up to $105,000, plus
    18.00% 	on the portion of taxable income over $105,000 up to $140,000, plus
    18.75% 	on the portion of taxable income over $140,000
    """
    brackets = [
        (9.65, 32656),
        (13.63, 64313),
        (16.65, 105000),
        (18, 140000),
        (18.75, float('inf')),
    ]


class QuebecTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    $51,780 or less 	14%
    More than $51,780 but not more than $103,545 	19%
    More than $103,545 but not more than $126,000 	24%
    More than $126,000 	25.75%
    """
    brackets = [
        (14, 51780),
        (19, 103545),
        (24, 126000),
        (25.75, float('inf')),
    ]


class SaskatchewanTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    10.5% 	on the portion of taxable income that is $52,057 or less, plus
    12.5% 	on the portion of taxable income over $52,057 up to $148,734, plus
    14.5% 	on the portion of taxable income over $148,734
    """
    brackets = [
        (10.5, 52057),
        (12.5, 148734),
        (14.5, float('inf')),
    ]


class YukonTaxRate(ProvincialTaxRate):
    """ 2024
    ==========================
    6.4% 	on the portion of taxable income that is $55,867 or less, plus
    9% 	on the portion of taxable income over $55,867 up to $111,733, plus
    10.9% 	on the portion of taxable income over $111,733 up to $173,205, plus
    12.8% 	on the portion of taxable income over $173,205 up to $500,000, plus
    15% 	on the portion of taxable income over $500,000
    """
    brackets = [
        (6.4, 55867),
        (9, 111733),
        (10.9, 173205),
        (12.8, 500000),
        (15, float('inf')),
    ]