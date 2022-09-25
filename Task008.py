# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coordAx = float(input("Введите координату Ax: "))
coordAy = float(input("Введите координату Ay: "))
coordBx = float(input("Введите координату Bx: "))
coordBy = float(input("Введите координату By: "))

lengthSegment = ((coordBx - coordAx) ** 2 + (coordBy - coordAy) ** 2) ** (0.5)
lengthSegment = float('{:.3f}'.format(lengthSegment))
print('Расстояние между точками в 2D пространстве = ' , lengthSegment )