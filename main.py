# ======== итеративная версия ========
n = int(input("Введите n: "))

a, b = 0, 1

print(f"Первые {n} чисел Фибоначи:")
for i in range(n):
    # здесь делаем параметр end=" ", т.к. нам нужно вывести эти числа в строчку
    # по умолчанию, end="\n"
    print(a, end=" ")
    a, b = b, a + b

print()

# ======== рекурсивная версия ========
N = int(input("Введите n: "))


def fib(a=0, b=1, counter=1):
    print(a, end=" ")

    if counter == N:
        print()
        return
    return fib(b, a + b, counter + 1)


fib()
