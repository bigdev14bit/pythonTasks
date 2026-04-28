def interest(balance, rate, years):
    if rate < 0:
        raise ValueError("Rate can't be negative")
    if rate < 1:
        raise ValueError("Years should be at least 1")

    final_balance = balance * (1 + rate) ** years

    return round(final_balance, 2)
