# Canatax: The Canadian Tax Calculator

![Development Status](https://img.shields.io/badge/status-in_development-orange)

**Note:** This package is currently in development. Expect frequent updates and potential breaking changes.

**Canatax** is a simple and straightforward package for calculating Canadian sales or income taxes based on the current year's rates. Whether you need to calculate federal and provincial income taxes, CPP, EI, or estimate GST/PST/HST across different provinces and territories, Canatax provides an easy-to-use interface with no additional dependencies.

## Features

- **Income Tax Calculation:**
  - **Current Year Rates:** Calculates taxes based on the most up-to-date rates for the current year.
  - **Federal and Provincial Taxes:** Automatically determines federal and provincial taxes based on your income and province.
  - **CPP and EI Deductions:** Includes Canada Pension Plan (CPP) and Employment Insurance (EI) deductions in the calculation.
  - **After-Tax Income:** Provides your net income after all deductions.

- **Sales Tax Estimation:**
  - **Provincial and Territorial Rates:** Estimates GST, PST, and HST for all Canadian provinces and territories.
  - **Customizable Inputs:** Allows for quick calculations with adjustable amounts and locations.

## Installation

You can install Canatax via pip:

```bash
pip install canatax
```

## Usage

### Income Tax Calculation with the `IncomeTaxCalculator` Class

Use the `IncomeTaxCalculator` class to calculate your income taxes:

```python
from canatax import IncomeTaxCalculator

# Example income and province
income = 80000
province = "AB"

# Calculate tax estimate
estimate = IncomeTaxCalculator.calculate(income=income, province=province)

# Or create an instance of TaxCalculator, if you prefer
calculator = IncomeTaxCalculator(income=income, province=province)
income_estimate = calculator.calculate_all()

# Output the results
print(estimate.federal_tax)
print(estimate.provincial_tax)
print(estimate.cpp)
print(estimate.ei)
print(estimate.total_tax)
print(estimate.after_tax_income)
```


### Sales Tax Calculation with the `SalesTaxCalculator` Class

Use the `SalesTaxCalculator` class to calculate sales taxes:

```python
from canatax import SalesTaxCalculator

# Example amount and province
amount = 100.00
province = "BC"

# Calculate sales tax estimate
sales_estimate = SalesTaxCalculator.quick_calc(amount=amount, province=province)

# Or create an instance of SalesTaxCalculator
sales_tax_calculator = SalesTaxCalculator(province=province)
sales_estimate = sales_tax_caluclator.calculate() 

# Output the results
print(sales_estimate.gst_total)
print(sales_estimate.pst_total)
print(sales_estimate.hst_total)
print(sales_estimate.tax_total)
print(sales_estimate.after_tax_total)
```

## Roadmap

- **Additional Features:**
  - Expand support for retroactive tax calculations for previous years.
  - Increase testing
  - Add more detailed documentation and usage examples.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.