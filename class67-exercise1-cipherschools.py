# Exercise, Modify Number Guessing Game
import random
winning_number=random.randint(1,100)
guess=1
num=int(input("Guess number between 1 and 100: "))
game_over=False
while not game_over:
    if num==winning_number:
        print(f"YOU WIN!!!, and you guessed the number in {guess} times")
        game_over=True
    else:
        if num>winning_number:
            print("too high")
        else:
            print("too low")
        guess+=1
        num=int(input("Guess again: "))