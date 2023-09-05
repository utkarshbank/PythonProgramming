amount = eval(input("Enter an amount, for example, 11.56: "))

cents = int(amount * 100)

dollars = cents // 100
if dollars != 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(dollars, "dollars")

cents %= 100
pennies = cents
if pennies != 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(pennies, "pennies")
