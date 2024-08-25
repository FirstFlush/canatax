from dataclasses import dataclass, asdict
from typing import Any
from canatax.enums import ProvinceOrTerritory
from canatax.utils import to_currency


@dataclass
class BaseTaxEstimate:
    province: ProvinceOrTerritory

    def _prettify(self, d:dict[str, Any]) -> dict[str,Any]:
        d2 = {}
        for k, v in d.items():
            if isinstance(v, float):
                d2[k] = to_currency(v)
            elif isinstance(v, ProvinceOrTerritory):
                d2[k] = v.value
            else:
                d2[k] = v
        return d2

    def to_dict(self, prettify:bool=False) -> dict[str, Any]:
        d = asdict(self)
        if prettify:
            d = self._prettify(d)
        return d
    

@dataclass
class SalesTaxEstimate(BaseTaxEstimate):
    before_tax_total: float
    gst_total: float
    pst_total: float
    hst_total: float
    tax_total: float
    after_tax_total: float


@dataclass
class IncomeTaxEstimate(BaseTaxEstimate):
    gross_income: float
    federal_tax: float
    provincial_tax: float
    cpp: float
    ei: float
    total_tax: float
    net_income: float