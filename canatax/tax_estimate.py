from dataclasses import dataclass


@dataclass
class TaxEstimate:
    gross_income: float
    federal_tax: float
    provincial_tax: float
    cpp: float
    ei: float
    total_tax: float
    net_income: float
    # marginal_tax_rate: float