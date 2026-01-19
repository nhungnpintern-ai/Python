#Exercise 6.1: Printing a dictionary
ds_ban_be={
    'Bui thi thao nguyen' : 20,
    'Le thi thanh suong':23,
    "NGo manh phuoc": 23,
}
print(ds_ban_be['Bui thi thao nguyen'])
#Exercise 6.2: Histogram
heo= ['a', 'b', 'a', 'c', 'b', 'a']
def histogram(heo):
    result = {}

    for x in heo:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result
print(histogram([1, 2, 1, 3, 2, 1]))

#After you are done, look up ‘python collections counter’ in Google. Could you use a counter instead?

from collections import Counter

def histogram(heo):
    return Counter(heo)
#Exercise 6.3: Get method
ds_ban_be={
    'Bui thi thao nguyen' : 20,
    'Le thi thanh suong':23,
    "NGo manh phuoc": 23,
}
print(ds_ban_be.get('Le thi thanh suong'))
#Exercise 6.4: Random text generator
[
 ('BEGIN', 'the'),
 ('the', 'fire'),
 ('fire', 'and'),
 ('and', 'the'),
 ('the', 'wind.'),
 ('wind.', 'END')
]
def process_line(line):
    words = line.strip().split()
    a=[]

    prev='BEGIN'
    for word in words:
        a.append((prev,word))
        prev = word
        
    a.append((prev,'END'))
    return a

#process_textfile
def process_textfile(f):
    transitions={}

    for line in f:
        pairs = process_line(line)
        for current , nxt in pairs:
            if current not in transitions:
                transitions[current]=[]
            transitions[current].append(nxt)    
    return transitions

#Code generate_line
import random

def generate_line(transitions):
    word = 'BEGIN'
    result = []

    while True:
        next_word = random.choice(transitions[word])
        if next_word == 'END':
            break
        result.append(next_word)
        word = next_word

    return ' '.join(result)

#Ex 6.5
