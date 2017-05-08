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
