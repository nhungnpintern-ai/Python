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
f = [
    "the fire and the wind.",
    "the wind and the rain."
]

trans = process_textfile(f)

print(generate_line(trans))
print(generate_line(trans))
