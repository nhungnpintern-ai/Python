divisible = lambda x, y: x % y == 0
isprime   = lambda x: x > 1 and not any(divisible(x, y) for y in range(2, x))
primes    = lambda n: [x for x in range(2, n+1) if isprime(x)]
print(primes(20))
