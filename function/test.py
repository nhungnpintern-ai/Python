def isprime(n):
    if n <=1:
        return False
    if n <=3:
        return True
    if n % 2 ==0 or n%3==0:
        return False
    i = 5 
    while i * i<=n:
        if n % i == 0 or n%(i+2)==0:
            return False
        i +=6
    return True
def prime_up(n):
    prime=[]
    for i in range(2,n+1):
        if isprime(i):
            prime.append(i)
    return prime
n = int(input("Nhap n: "))
result = prime_up(n)
print(result)
