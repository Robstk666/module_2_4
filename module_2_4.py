numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:  # Внешний цикл для перебора чисел
    if number < 2:  # Пропускаем числа меньше 2, так как 1 не простое и не составное
        continue

    is_prime = True  # Изначально считаем, что число простое

    for i in range(2, number):  # Вложенный цикл для проверки делителей от 2 до (number-1)
        if number % i == 0:  # Если число делится на i без остатка, оно не простое
            is_prime = False
            break  # Прерываем цикл, если нашли делитель

    if is_prime:
        primes.append(number)  # Добавляем простое число в список primes
    else:
        not_primes.append(number)  # Добавляем составное число в список not_primes

print("Primes:", primes)
print("Not Primes:", not_primes)




