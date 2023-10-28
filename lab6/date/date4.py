date1 = datetime(2023, 10, 19)
date2 = datetime(2023, 9, 27)

if(date1 > date2):
    print((date1-date2).total_seconds())
else:
    print((date2-date1).total_seconds())

