from dataclasses import dataclass


@dataclass
class TaxEstimate:
    federal_tax: float
    provincial_tax: float
    cpp: float
    ei: float
    total_tax: float
    after_tax_income: float
    # marginal_tax_rate: float