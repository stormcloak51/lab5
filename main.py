n = int(input("Введите число n: "))

sum_numbers = 0
product = 1
sum_squares = 0

# делаем до n+1, т.к. нужно до n включительно
for i in range(1, n + 1):
    sum_numbers += i
    product *= i
    sum_squares += i**2

print(f"Сумма: {sum_numbers}")
print(f"Произведение (N!): {product}")
print(f"Сумма квадратов: {sum_squares}")
