from interpretor import *


Num1 = int(input('Number 1: '))
Num2 = input('Expression: ')
Num3 = int(input('Number 2: '))
result = interpretor(Num1, Num2, Num3)
print(f"{result:.1f}")