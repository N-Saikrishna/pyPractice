import sys

def collatz(number): 
    global num
    if num % 2 == 0: 
        num = num // 2
        print(num, end=' ')
    elif num % 2 == 1: 
        num = (3 * num) + 1
        print(num, end=' ')


try:
    print('Enter the number: ')
    num = int(input(''))
    print(num, end=' ')
except ValueError: 
    print("Enter an integer") 

while num != 1: 
    collatz(num)

sys.exit()