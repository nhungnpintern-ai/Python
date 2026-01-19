x = (1, 2, 3)
y = (4, 0, 6)
def l1_space(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))
import math 
def l2_space(x,y):
    return math.sqrt(sum((a-b)**2 for a,b in zip(x,y)))
print(l1_space(x,y))
print(l2_space(x,y))