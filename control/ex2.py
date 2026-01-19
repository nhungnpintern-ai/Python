#Exercise 2.1: Range
#input 
for i in range(5):
    print(i)
#output    
0
1
2
3
4

#Exercise 2.2
#(a)Print the numbers 0 to 100
for x in range(0,101):
    print(x)

#(b) Print the numbers 0 to 100 that are divisible by 7
for x in range(0,101):
    if x % 7 ==0:
        print(x)
# (c)Print the numbers 1 to 100 that are divisible by 5 but not by 3    
for x in range(0,101):
    if x % 5 == 0 and x % 3 !=0 :
        print(x)
#(d) In ra tất cả các số chia hết cho x, ngoại trừ 1 và x, với mỗi số x = 2, ..., 20
for x in range(2, 21):
    print("x =", x)
    for e in range(2, x):
        if x % e == 0:
            print(e)

#Exercise 2.3:
#(a)Print the numbers 0 to 100
x=0
while x < 101 : 
    print(x)
    x+=1
#b Print the numbers 0 to 100 that are divisible by 7
x = 0 
while x <=100:
    if x % 7 ==0:
        print(x)
    x+=1 

#Exercise 2.4 


#Exercise 2.5: While loops
number_found = 0 
x = 11 

while number_found <=20 : 
    if  x % 5 == 0 and x % 7 == 0 and x % 11 == 0 :
        print(x)
        number_found +=1 
    x += 1

#Exercise 2.6:   More while loops
x = 1 
while True : 
    ok = True
    for d in range(1,11):
        if x % d !=0:
            ok = False
            break
    if ok :
        print(x)
        break
    x+=1    
#Exercise 2.7 : 
import math 
x = 103 
print(x)
while x!=1:
    if x%2==0:
        x = x//2
    else:
        x=3*x+1
    print(x)

