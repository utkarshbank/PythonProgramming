import random
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

truesum = num1 + num2


sum = int(input(f"What is the sum of {num1} and {num2}? "))


if sum == truesum:
    print("True!")
else:
    print("False")
