def get_income_in_minutes(
    monthly_income: float, monthly_hours: float = 20 * 7.
) -> float:
    return monthly_income / (monthly_hours * 60.)
