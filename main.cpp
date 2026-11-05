#include <iostream>

int main() {
    int n;
    std::cout << "Введите N: ";
    std::cin >> n;

    long long total = 0;
    long long fact = 1;

    for (int i = 1; i <= n; ++i) {
        total += i;
        fact *= i;
    }

    std::cout << "Сумма: " << total << "\n";
    std::cout << "Факториал: " << fact << "\n";

    return 0;
}
