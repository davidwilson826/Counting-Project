from random import shuffle, randint

cards = ['J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

failures = 0
trials = 1000

for i in range(trials):
    shuffle(cards)
    print(cards)
    for j in range(9):
        if cards[j] + cards[j+1] + cards[j+2] + cards[j+3] == 'JJJJ' or 'QQQQ' or 'KKKK':
            failures += 1
            break
        
print(failures/trials*100, '%')
