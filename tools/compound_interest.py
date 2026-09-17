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
