# Canatax: The Canadian Income Tax Calculator

**Canatax** is a simple and straightforward package for calculating Canadian income taxes based on the current year's tax rates. Whether you want to quickly calculate your federal and provincial taxes, CPP, EI, or after-tax income, Canatax makes it easy with no additional dependencies.

## Features

- **Current Year Rates:** Calculates taxes based on the most up-to-date rates for the current year.
- **Federal and Provincial Taxes:** Automatically determines federal and provincial taxes based on your income and province.
- **CPP and EI Deductions:** Includes Canada Pension Plan (CPP) and Employment Insurance (EI) deductions in the calculation.
- **After-Tax Income:** Provides your net income after all deductions.

## Installation

You can install Canatax via pip:

```bash
pip install canatax
```

## Usage

### Quick Usage Example with the `TaxCalculator` Class

Here's a quick example of how to use the `TaxCalculator` class to calculate your taxes:

```python
from canatax import TaxCalculator

# Example income and province
income = 80000
province = "AB"

# Calculate tax estimate
estimate = TaxCalculator.calculate(income=income, province=province)

# Or create an instance of TaxCalculator, if you prefer
calculator = TaxCalculator(income=income, province=province)
estimate = calculator.calculate_all()

# Output the results
print(estimate.federal_tax)
print(estimate.provincial_tax)
print(estimate.cpp)
print(estimate.ei)
print(estimate.total_tax)
print(estimate.after_tax_income)
```