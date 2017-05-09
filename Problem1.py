'''
from random import shuffle, randint

cards = ['J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

failures = 0
trials = 1000

for i in range(trials):
    shuffle(cards)
    #print(cards)
    for j in range(9):
        #print(cards[j] + cards[j+1] + cards[j+2] + cards[j+3])
        if (cards[j] + cards[j+1] + cards[j+2] + cards[j+3]) in ['JJJJ', 'QQQQ', 'KKKK']:
            failures += 1
            break
        
print((trials-failures)/trials*100, '%')
'''

from random import shuffle, randint

people = ['T', 'T', 'T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']

successes = 0
amount = 0
trials = 10

for i in range(trials):
    shuffle(people)
    print(people)
    for j in range(10):
        #print(people[j] + people[j+1] + people[j+2] + people[j+3])
        if (people[j] + people[j+1] + people[j+2] + people[j+3] + people[j+4]) == 'SSTSS':
            amount += 1
        if amount == 3:
            successes += 1
        amount = 0
        
print((successes)/trials*100, '%')