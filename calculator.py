def get_income_in_minutes(
    monthly_income: float, 
    monthly_work_hours: float = 22. # 262 working days, 8 hours a day
) -> float:
    return monthly_income / (monthly_work_hours * 60)

def get_price_in_minutes(
    income_in_minutes: float,
    price: float,
) -> float:
    return price / income_in_minutes
