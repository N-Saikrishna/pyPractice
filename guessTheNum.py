import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

for guessed in range(1, 7):
    print('Take a guess')
    guess = int(input(''))

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('your guess is too high')
    else: 
        break #guessed right

if guess == secret_number:
    print('You got it in ' + str(guessed) + ' guesses')
else:
    print('The actual number was ' + secret_number)