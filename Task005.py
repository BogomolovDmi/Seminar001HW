# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

xnumber = int(input("Введите значение X= "))
ynumber = int(input("Введите значение Y= "))
znumber = int(input("Введите значение Z= "))

left = not (xnumber or ynumber or znumber)
right = not xnumber and not ynumber and not znumber
if left == right:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

# Если это решается не так, то я уже не знаю как
# Я давно забыл алгебру логики
