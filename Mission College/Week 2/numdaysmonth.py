month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))


days = 0

if month == 2:
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        days = 29
    else:
        days = 28


elif month in [4, 6, 9, 11]:
    days = 30

else:
    days = 31

print("Number of days:", days)

