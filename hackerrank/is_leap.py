def is_leap(year):
    year = int(year)
    if year % 4:
        return False
    if not year % 100 and year % 400:
        return False
    return True
