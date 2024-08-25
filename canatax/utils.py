# Handy utility functions used by multiple classes


def to_currency(n:float) -> str:
    return f"{n:,.2f}"


def percent_to_decimal(n:float) -> float:
    return n / 100