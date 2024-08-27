from decimal import Decimal


def to_currency(n:float|Decimal) -> str:
    return f"{n:,.2f}"


def percent_to_decimal(n:float|Decimal) -> Decimal:
    return Decimal(n / 100)