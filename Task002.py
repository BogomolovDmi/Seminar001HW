# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number = float(input("Введите дробь через точку после её целой части: "))
first_fractional_part = int( (number*10) % 10 )
if first_fractional_part == 0:
    print('нет')
else:
    print(first_fractional_part)

# Как сделать конкретно проверку на дробь я не знаю, честно говоря
# В задании стоят , и питон на это ругается