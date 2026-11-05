n = int(input("Введите N: "))

total = 0
fact = 1

for i in range(1, n + 1):
    total += i
    fact *= i

print(f"Сумма: {total}")
print(f"Факториал: {fact}")
