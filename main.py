from random import randint

n = randint(1000, 9999)

while True:
    bulls, cows = 0, 0
    n_str = str(n)

    sug = input("Введите число: ")

    if n_str == sug:
        print("Угадали")
        break

    for i in range(4):
        if sug[i] == n_str[i]:
            bulls += 1
        elif sug[i] in n_str:
            cows += 1
    print(
        "Не угадали!",
        f"Количество быков: {bulls}",
        f"Количество коров: {cows}",
        sep="\n",
    )
    (
        bulls,
        cows,
    ) = 0, 0
