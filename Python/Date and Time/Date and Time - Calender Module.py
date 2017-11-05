import calendar
d, m, y = map(int, raw_input().split())
print calendar.day_name[calendar.weekday(y,d,m)].upper()