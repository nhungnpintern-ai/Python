#Exercise 5.1: Swapping two values
print("in python if want to change a =b b=a , Then we do it this way: a,b = b,a")
#ex 5.2
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

points = list(zip(x, y))
print(points)
### muon tra nguoc lai (*) unpacking
points = [(1, 5), (2, 6), (3, 7), (4, 8)]
x, y = zip(*points)

x = list(x)
y = list(y)

print(x)
print(y)

#Exercise 5.3: Distances
x = (1, 2, 3)
y = (4, 0, 6)
def l1_space(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

import math 
def l2_space(x,y):
    return math.sqrt(sum((a-b)**2 for a,b in zip(x,y)))
print(l1_space(x,y))
print(l2_space(x,y))
