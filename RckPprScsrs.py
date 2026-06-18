# Rock Paper Scissors

import random, sys

win = 0
loss = 0
ties = 0

while True: #loop for whole game
    print('%s Wins, %s Losses, %sTies' %(win, loss, ties) ) #prints W, L, T so far
    while True: #loop for input
        print("Pick (r)ock, (p)aper, (s)cissors, or (q)uit")
        choice = input('')

        if choice == 'q':
            sys.exit()
        if choice == 'r' or choice == 'p' or choice == 's':
            break
        print('Pick between r, p, s, or q')

    #player choice
    if choice == 'r':
        print('Rock vs... ')
    elif choice == 'p':
        print('Paper vs... ')
    elif choice == 's':
        print('Scissors vs... ')
    
    #comp choice
    comp_num = random.randint(1, 4)
    
    if comp_num == 1: 
        comp_choice = 'r'
        print('Rock')
    elif comp_num == 2: 
        comp_choice = 'p'
        print('Paper')
    elif comp_num == 3: 
        comp_choice = 's'
        print('Scissor')
    
    #Record win/loss/tie
    if choice == comp_choice:
        ties = ties + 1
        print('It is a Tie')
    elif choice == 'r' and comp_choice == 'p':
        loss = loss + 1
        print('Womp Womp, you lost')
    elif choice == 'r' and comp_choice == 's':
        win = win + 1
        print('You won')
    elif choice == 'p' and comp_choice == 'r':
        win = win + 1
        print('You won')
    elif choice == 'p' and comp_choice == 's':
        loss = loss + 1
        print('Womp Womp, you lost')
    elif choice == 's' and comp_choice == 'p':
        win = win + 1
        print('You won')
    elif choice == 's' and comp_choice == 'r':
        loss = loss + 1
        print('Womp Womp, you lost')
    
