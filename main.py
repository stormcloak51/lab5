n = int(input("Введите число N: "))
primes = []

for num in range(2, n + 1):
    is_prime = True

    # делим num на все числа от 2 до корня из num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(f"Простые числа до {n}: {primes}")
