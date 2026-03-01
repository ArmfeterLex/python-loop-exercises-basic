# 1
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A <= B:
    for i in range(A, B + 1):
        print(i, end=" ")
    print()
else:
    print("Ошибка: A должно быть меньше или равно B")
    
# 2
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    for i in range(A, B + 1):
        print(i, end=" ")
    print()
elif A > B:
    for i in range(A, B - 1, -1):
        print(i, end=" ")
    print()
else:
    print(A)
    
# 3
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A > B:
    for i in range(A, B - 1, -1):
        if i % 2 != 0:
            print(i, end=" ")
    print()
else:
    print("Ошибка: A должно быть больше B")
    
# 4
сумма = 0
for i in range(10):
    число = int(input(f"Введите число {i + 1}: "))
    сумма += число
print("Сумма введенных чисел:", сумма)

# 5
N = int(input("Введите количество чисел: "))
сумма = 0
for i in range(N):
    число = int(input(f"Введите число {i + 1}: "))
    сумма += число
print("Сумма введенных чисел:", сумма)

# 6
n = int(input("Введите натуральное число n: "))
if n <= 0:
    print("Ошибка: n должно быть натуральным числом (больше 0)")
else:
    sum_of_cubes = 0
    for i in range(1, n + 1):
        sum_of_cubes += i**3
    print("Сумма кубов от 1 до", n, ":", sum_of_cubes)
    
# 7
n = int(input("Введите натуральное число n: "))
if n < 0:
    print("Факториал определен только для неотрицательных чисел")
elif n == 0:
    print("Факториал 0 равен 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал {n} равен {factorial}")
    
# 8 
n = int(input("Введите натуральное число n: "))
if n <= 0:
    print("Ошибка: n должно быть натуральным числом (больше 0)")
else:
    total_sum = 0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        total_sum += factorial
    print("Сумма факториалов от 1! до", n, ":", total_sum)
    
# 9
N = int(input("Введите количество чисел: "))
count_zeros = 0
for i in range(N):
    number = int(input(f"Введите число {i + 1}: "))
    if number == 0:
        count_zeros += 1
print("Количество нулей:", count_zeros)