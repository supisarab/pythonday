def generate_prime(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print(generate_prime(10))
print(generate_prime(20))
print(generate_prime(1))
print(generate_prime(2))