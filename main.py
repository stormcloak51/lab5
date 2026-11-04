eps = float(input("Введите точность (например 0.0001): "))

print(len(str(eps)))
e = 1
fact = 1
n = 1
term = 1

while term > eps:
    print(e)
    fact *= n
    term = 1 / fact
    e += term
    n += 1

# логичка вычисления чисел после точки
print(f"e = {e:.{len(str(eps)) - 2}f}")
