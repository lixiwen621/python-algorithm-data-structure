# This lesson will focus on one problem: calculating the number of days between two dates.
# 这节课将集中讨论一个问题：计算两个日期之间的天数。
# 普通年份的每月天数
month_days = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    # Check that the year, month and day are correct
    check_data(year1,month1,day1,year2,month2,day2)

    day = 0
    # Calculate the number of days between years
    # Leap years differ by 366 days
    # 计算年份相差的day
    for y in range(year2-1,year1-1,-1):
        if is_leap_year(y):
            day += 366
        else:
            day += 365
    # Calculate the number of days between months
    # 计算月份相差的day
    for m2 in range(month2-1,0,-1):
        day += get_days_in_month(year2, m2)

    for m1 in range(month1-1,0,-1):
        day -= get_days_in_month(year1, m1)

    # Calculate the day
    # 计算天数
    return day + day2 - day1

def date_is_before(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 <= day2
    return False


def check_data(year1, month1, day1, year2, month2, day2):
    # check date type
    date = [year1,month1,day1,year2,month2,day2]
    if not all(isinstance(d, int) for d in date):
        raise ValueError("The input year, month, and day must be of type int")
    # The date cannot be less than 0
    if year1 <= 0 or month1 <= 0 or day1 <= 0 or year2 <= 0 or month2 <= 0 or day2 <= 0:
        raise ValueError("The year, month and day cannot be less than or equal to 0")
    # The months are only possible from January to December
    if month1 not in month_days or month2 not in month_days:
        raise ValueError("The months are only possible from 1 to 12")
    # Check that the number of days per month is correct
    max_day1_in_month = get_days_in_month(year1,month1)
    if day1 > max_day1_in_month:
        raise ValueError(f"{year1},{month1},{day1} -- {day1} cannot exceed {max_day1_in_month}")
    max_day2_in_month = get_days_in_month(year2,month2)
    if day2 > max_day2_in_month:
        raise ValueError(f"{year1},{month1},{day1} -- {day1} cannot exceed {max_day1_in_month}")

        # check year1, month1, day1 is Before year2, month2, day2
    assert date_is_before(year1, month1, day1, year2, month2, day2), \
            ("The entered date is incorrect. The previous time cannot be greater than the later time")


#Judge leap year
# 是否闰年
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Get the days of the month
# 获取当月天数
def get_days_in_month(year,month):
    if is_leap_year(year) and month == 2:
        return 29

    return month_days.get(month, 0)


def test():
    # tests with 30-day months!
    assert days_between_dates(2013, 1, 1, 2013, 1, 1) == 0
    assert days_between_dates(2013, 1, 1, 2013, 1, 2) == 1
    print("Tests finished.")



if __name__ == '__main__':
    day = days_between_dates(2004,11,28,2009,2,28)
    test()
    print(day)
