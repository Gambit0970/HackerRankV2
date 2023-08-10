import calendar
#days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
mm,dd,yy = [int(x) for x in input().split()]

print(calendar.day_name[calendar.weekday(yy, mm, dd)].upper())
