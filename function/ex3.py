#Exercise 3.1: Hello
#(a)Write a function hello_world that prints ’Hello, world!’
from os import name


def funcition():
    print('hello wold')
funcition()
# (b) Write a function hello_name(name) that prints ’Hello, name!’ where name is a string.
def hello_name(name):
    print('hello'+ name +'!')
hello_name(' nhung')
#(c)
#Explain the difference between the print and return keywords. What would change if instead of print you would use return?
print('''print は 画面に表示するため の命令

値を 関数の外に返さない''')
print('''return は 関数の結果を呼び出し元に返す

返された値は 変数に保存したり、計算に使える
''')

#Exercise 3.2: Polynomial
def function(x):
    return 3*x**2 - x + 2
y = function(2)
print(y)

#Exercise 3.3 Maximun
def my_max(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
result = my_max(x, y)
print("the maximum is :" ,result)
#(b) Use if but not else (nor elif).
def my_max(x, y):
    if x > y:
        return x
    return y 

x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
result = my_max(x, y)
print("the maximum is :" ,result)

#Exercise 3.4: Primes
#(a) Write a function is_prime(n) that returns True only if n is prime.

def isprime(n):
    if n <=1 :
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
print(isprime(7))   # True
print(isprime(9))   # False
#(b)

def isprime(n):
    if n <=1 :
        return False
    if n <=3 :
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5 
    while i * i <=n:
        if n % i == 0  or n % (i+2)==0:
            return False
        i += 6
    return True
               

print(isprime(7))   # True
print(isprime(9))   # False
print(isprime(35))  # False
print(isprime(49)) # False

#(c) Write a function that returns all primes up to n.

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
    prime=[0]
    for i in range(2,n+1):
        if isprime(i):
            prime.append(i)
    return prime
n = int(input("Nhap n: "))
result = prime_up(n)
print(result)

#Exercise 3.5: Root finding
#(a)
def root(f,a,b):
    for i in range(100):
        m = (a+b)/2
        if f(m) ==0:
            return m 
        elif f(a)*f(m)<0:
            b=m
        else:
            a=m
        return (a+b)/2    
def f(x):
    return x**2 - 2

print(root(f, 2, 3))
#b
def root(f, a, b):
    # 1. Không phụ thuộc a < b
    if a > b:
        a, b = b, a

    # 2. Không phụ thuộc f(a) < 0, f(b) > 0
    if f(a) * f(b) > 0:
        print("function evals have same sign")
        return None

    # 3. Chia đôi tìm nghiệm
    for i in range(100):
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return (a + b) / 2
root(f, 0, 2)   # a < b
root(f, 2, 0)   # a > b
#c 
def root(f, a, b):
    fa = f(a)
    fb = f(b)

    # kiểm tra cùng dấu
    if fa > 0 and fb > 0 or fa < 0 and fb < 0:
        print("function evals have same sign")
        return None
def f(x):
    return x**2 + 1   # ++

root(f, -2, 2)



