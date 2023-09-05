start = 2001
end = 2100

leap_year_count = 0
leap_years_line = ""

for year in range(start, end + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_year_count += 1
        leap_years_line += str(year) + " "

        if leap_year_count % 10 == 0:
            print(leap_years_line)
            leap_years_line = ""

if leap_years_line:
    print(leap_years_line)
