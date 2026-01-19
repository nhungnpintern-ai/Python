#Exercise 4.1: Short questions
#(a) Write a function that prints the elements of a list
list=["hihi","hehe","huu","haha"]
print(list)
#b) Write a function that prints the elements of a list in reverse
list=["hihi","hehe","huu","haha"]
print(list[::-1])
#(c) Write your own implementation of the len function that returns the number of elements in a list.
def len(ds):
    count = 0
    for _ in ds :
        count +=1

    return count
a =  ["cuong","hehe","thuy","trang"]
print(len(a))
#Exercise 4.2: Copying lists
#a Tạo một danh sách a với một số mục.
a = [1,'hai',3,[4,5],6]
#Now set b = a
b = a
#(c) Change b[1]
b[1]=2
print(b)
#d what happend to a ? 
print(a) #out [1, 2, 3, [4, 5], 6]
#Now set c = a[:]
c =a[:]
#change c
c[2]="ba"
#(g) What happened to a?
print("a khong thay doi ")#out [1, 2, 3, [4, 5], 6]
##now cuoi cung tao 1 ham set_first_elem_to_zero(l) va doi phan tu dau tien thanh 0 , ta nhan duoc 
def set_first_elem_to_zero(l):
    l[0] = 0
    return l
list1=[3,5,6]

set_first_elem_to_zero(list1)
print(list1)

#Exercise 4.3: Lists of lists
print("a là tất cả cùng trỏ tới 1 list , b là trỏ tới các phần tử khác nhau , điểm chung đều có 3 phần tử")
#Exercise 4.4: Lists and functions
def set_first_elem_to_zero(l,index):
    l[index] = 0
    return l
list1=[3,5,6]

set_first_elem_to_zero(list1,2)
print(list1)

#Exercise 4.5: Primes
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

#Exercise 4.6: List comprehensions
#a Generate a list with elements [i,j].
n=3
result=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        result.append(i,j)
print(result)        
#bGenerate a list with elements [i,j] with i < j
n=3
result=[]
for i in range(1,n+1):

    for j in range(i+1,n+1):
        result.append([i,j])
print(result) 

#c Generate a list with elements i + j with both i and j prime and i > j.
def snt(n):
    if n < 2 : 
        return False
    for k in range(2,int(n**0.5)+1):
        if n % k ==0:
            return False
    return True
n=10
result = []
for i in range(2, n + 1):
    for j in range(2, n + 1):
        if snt(i) and snt(j) and i > j:
            result.append(i + j)
print(result)    

#(d) Write a function that evaluates an arbitrary polynomial a0 + a1x + a2x
def evaluate_poly(x, coefs):
    return sum(a * x**i for i, a in enumerate(coefs))
coefs=[4,2,3] #4+2x+3x^2
x=5
print(evaluate_poly(x, coefs))
#Exercise 4.7: Filter
def myfilter(func, iterable):
    return [x for x in iterable if func(x)]

nums = [1, 2, 3, 4, 5, 6]

# dùng myfilter
lt1 = myfilter(lambda x: x % 2 == 0, nums)

# dùng filter chuẩn của Python
lt2 = list(filter(lambda x: x % 2 == 0, nums))

print(lt1)
print(lt2)

#Ex 4.8
def flatten(lists):
    return [x for sublist in lists for x in sublist]
data = [[1, 3], [3, 6]]

adn = flatten(data)
print(adn)

#Ex 4.9 
def longest_word(text):
    # Bỏ dấu câu
    clean_text = ""
    for ch in text:
        if ch.isalpha() or ch == " ":
            clean_text += ch

    # Tách thành các từ
    words = clean_text.split()

    # Tìm từ dài nhất
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
text = "Hello, how was the football match earlier today???"
print(longest_word(text))

#EX4.10
#(a) Write a function that for any n, returns its Collatz sequence as a list
def collat_sequence(n):
    nt=[n]
    while n!=1:
        if n % 2==0:
            n = n//2
        else:
            n = 3*n+1
        nt.append(n)  
    return nt  
n=6
print(collat_sequence(n))
#b Write a function that finds the integer x that leads to the longest Collatz sequence with x < n.
def longest_collatz(n):
    max_length = 0
    result = 1

    for x in range(1, n):
        length = len(collat_sequence(x))
        if length > max_length:
            max_length = length
            result = x

    return result
print(longest_collatz(5))
#Ex4.11
def hub(x,ys):
    smaller = [y for y in ys if y < x]
    larger = [y for y in ys if y >= x]
    return smaller + [x] + larger
x = 4
ys = [6,5,1]
print(hub(x,ys))
#Ex 4.12
divisible = lambda x, y: x % y == 0
isprime   = lambda x: x > 1 and not any(divisible(x, y) for y in range(2, x))
primes    = lambda n: [x for x in range(2, n+1) if isprime(x)]
print(primes(20))
