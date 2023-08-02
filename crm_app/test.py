import calendar


def getDaysInEachMonth(year):
    days_per_month = {}

    for month in range(1, 13):
        _, num_of_days = calendar.monthrange(year, month)
        days_per_month[month] = num_of_days
    return days_per_month


def is_julian(year):
    return year <= 1919


def is_leap_in_julian(year):
    return year % 4 == 0


def dayOfProgrammer(year):
    days_per_month = getDaysInEachMonth(year)
    total_days = 0
    remaining_days = 0
    target_month = 0

    if is_julian(year) and is_leap_in_julian(year):
        days_per_month[2] = 29

    for month in range(1, 13):
        if total_days + days_per_month[month] <= 256:
            total_days += days_per_month[month]
        else:
            target_month = month
            break

    if total_days < 256:
        remaining_days = 256 - total_days

    return f"{remaining_days:02d}.{target_month:02d}.{year}"


print(dayOfProgrammer(1900))
