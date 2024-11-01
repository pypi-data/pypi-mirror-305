
def mdc(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a,b):
    return abs (a*b) // mdc(a,b)

def verifica_primo(num):
    if num < 2:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeiros_primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        if verifica_primo(num):
            primos.append(num)
        num += 1
    return primos

def primos_ate(n):
    primos = []
    for num in range(2, n + 1):
        if verifica_primo(num):
            primos.append(num)
    return primos
