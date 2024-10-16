# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 9
# Date:         7 November 2022

def toohigh():
    print('Too high!')

def toolow():
    print("Too low!")
        

#needed inputs     
secret= 26
print('Guess the secret number! Hint: it\'s an integer between 1 and 100...')
guess= (input('What is your guess? \n'))
counter= 1

while guess != secret:
    try: 
        if int(guess) > secret:
            toohigh()
            counter+=1
            guess= int(input("What is your guess? \n"))
        elif int(guess) < secret:
            toolow()
            counter+=1
            guess= int(input('What is your guess? \n'))
        elif int(guess) == 26:
            break
    except:
        guess= (input('Bad input! Try again: \n'))
    

print(f'You guessed it! It took you {counter} guesses.')
