def prime(n):
    for i in range(2, int(n/2) + 1):
        if (n % i) == 0:
            return False

    return True

def select_primes(x):
    re = []
    for number in x:
        if prime(number):
            re.append(number)
    return re