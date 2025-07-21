def numeros_primos(n):
    primos = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primos.append(num)
    return primos

print(numeros_primos(20))
