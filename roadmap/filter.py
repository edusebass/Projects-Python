numeros = range(1, 1000)

def primos(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True

listprimos = list(filter(primos, numeros))

print(listprimos)