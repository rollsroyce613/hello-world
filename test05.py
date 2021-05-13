def findLeapYear(arr):
    for i in arr:
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(i)


yearNum = range(2000, 2021)
findLeapYear(yearNum)
