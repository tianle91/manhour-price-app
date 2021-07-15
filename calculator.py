def get_income_in_minutes(
    monthly_income: float, 
    monthly_hours: float = 22. # 262 working days, 8 hours a day
) -> float:
    return monthly_income / (monthly_hours * 60.)
