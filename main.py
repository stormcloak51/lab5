import random
import math


def monte_carlo_pi(n):
    """
    Вычисление числа π методом Монте-Карло.
    n - количество случайных точек.
    """
    inside_circle = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # проверяем, попала ли точка в четверть круга
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / n
    return pi_estimate


# --- Основная программа ---
n = int(input("Введите количество точек N: "))

pi_approx = monte_carlo_pi(n)
pi_real = math.pi

print(f"\nРезультаты:")
print(f"  Приближённое значение π: {pi_approx:.6f}")
print(f"  Точное значение π:       {pi_real:.6f}")
