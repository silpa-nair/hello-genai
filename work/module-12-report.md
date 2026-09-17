# Module 12 Completion Report

## Instruction File
- Filename: instructions/calculate-compound-interest.agent.md

```markdown
- Use this when asked to calculate compound interest (final amount, total interest, growth over time) for a given principal and rate.
- Tool: `tools/compound_interest.py`.
- Invocation:
  + Run via `python tools/compound_interest.py <principal> <annual_rate> <compounds_per_year> <years>`.
  + `principal` — starting amount, plain number (e.g. `15847`).
  + `annual_rate` — decimal form, not a percentage (e.g. `0.0734` for 7.34%).
  + `compounds_per_year` — integer compounding frequency (e.g. `12` for monthly, `4` for quarterly, `1` for annually).
  + `years` — total duration in years as a decimal; convert months to a fraction of a year first (e.g. 8 years 7 months → `8.5833333`, computed as `years + months/12`).
- Processing:
  + Do not hand-calculate the result — always invoke the script and use its printed output.
  + If the requested duration includes months, convert to decimal years before calling the script; do not pass months separately.
- Output format:
  + Present both printed lines from the script verbatim: `Final amount: $...` and `Total interest: $...`.
  + Do not reformat, round further, or recompute the values shown by the script.
- Constraints:
  + Never fabricate results without running the script.
  + If any input (principal, rate, frequency, years) is missing, ask the user before invoking the script rather than guessing values.
```

## Script File
- Filename: tools/compound_interest.py
- Language: Python

```python
import argparse


def compound_interest(principal, annual_rate, periods_per_year, years):
    """Return (final_amount, total_interest) for compound interest over a number of years."""
    total_periods = periods_per_year * years
    rate_per_period = annual_rate / periods_per_year
    final_amount = principal * (1 + rate_per_period) ** total_periods
    total_interest = final_amount - principal
    return final_amount, total_interest


def parse_args():
    parser = argparse.ArgumentParser(description="Calculate compound interest.")
    parser.add_argument("principal", type=float, help="Initial principal amount")
    parser.add_argument("annual_rate", type=float, help="Annual interest rate as a decimal (e.g. 0.0734 for 7.34%%)")
    parser.add_argument("compounds_per_year", type=int, help="Number of times interest compounds per year")
    parser.add_argument("years", type=float, help="Total number of years")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    final_amount, total_interest = compound_interest(
        args.principal, args.annual_rate, args.compounds_per_year, args.years
    )

    print(f"Final amount: ${final_amount:,.2f}")
    print(f"Total interest: ${total_interest:,.2f}")
```

## Script Execution Output
```
usage: compound_interest.py [-h]
                            principal annual_rate compounds_per_year years

Calculate compound interest.

positional arguments:
  principal             Initial principal amount
  annual_rate           Annual interest rate as a decimal (e.g. 0.0734 for
                        7.34%)
  compounds_per_year    Number of times interest compounds per year
  years                 Total number of years

options:
  -h, --help            show this help message and exit
```
