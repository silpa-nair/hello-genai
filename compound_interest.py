def compound_interest(principal, annual_rate, periods_per_year, years, months=0):
    """Return (final_amount, total_interest) for compound interest over years and months."""
    total_periods = periods_per_year * years + periods_per_year * months // 12
    rate_per_period = annual_rate / periods_per_year
    final_amount = principal * (1 + rate_per_period) ** total_periods
    total_interest = final_amount - principal
    return final_amount, total_interest


if __name__ == "__main__":
    principal = 15847
    annual_rate = 0.0734
    periods_per_year = 12
    years = 8
    months = 7

    final_amount, total_interest = compound_interest(principal, annual_rate, periods_per_year, years, months)

    print(f"Final amount: ${final_amount:,.2f}")
    print(f"Total interest: ${total_interest:,.2f}")
