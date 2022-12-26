def ndays(y, m):
    if m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            return 29
        else:
            return 28
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30
def calddays(year, month, day):
    days = 0
    for y in range(1, year):
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            days += 366
        else:
            days += 365
    for m in range(1, month):
        days += ndays(year, m)
    days += day
    return days
year = int(input("年: "))
if year < 1:
    year = 1
month = int(input("月: "))
if month < 1:
    month = 1
elif month > 12:
    month = 12
day = int(input("日: "))
if day < 1:
    day = 1
elif day > ndays(year, month):
    day = ndays(year, month)
print("从1年1月1日到{}年{}月{}日共{}天".format(
    year, month, day, calddays(year, month, day)))
