n = int(input("Введите число: "))
original = n

count = 0
total = 0
product = 1
reversed_num = 0

while n > 0:
    # чтобы получить последнюю цифру числа, берем остаток от деления на 10
    digit = n % 10
    count += 1
    total += digit
    product *= digit
    # сперва умножаем число на 10, чтобы оставить разряд для следующей цифры
    reversed_num = reversed_num * 10 + digit
    # уменьшаем число в 10 раз, чтобы перейти к следующей цифре
    n //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {product}")
print(f"Перевёрнутое число: {reversed_num}")
