def increment_date(year, month, day):
    """
    模拟日期进位操作，当天数或月份超出范围时自动进位。
    :param year: 当前年份
    :param month: 当前月份
    :param day: 当前日
    :return: 进位后的 (year, month, day)
    """
    # 每个月的天数，假设非闰年
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # 检查是否是闰年
    def is_leap_year(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    # 如果是闰年，2月天数为29
    if is_leap_year(year):
        days_in_month[2] = 29

    day += 1
    # 处理天数进位
    while True:
        if day > days_in_month[month]:
            day -= days_in_month[month]
            month += 1

            # 如果月份超出范围，年份进位
            if month > 12:
                month = 1
                year += 1
        yield year, month, day
        day += 1


increment_date =increment_date(2018,1,31)
print(next(increment_date))
print(next(increment_date))
print(next(increment_date))
print(next(increment_date))
print(next(increment_date))
print(next(increment_date))