logo = """

                __   __         __        __                __    
| | |  | |\ /| |  | |   |<<    |    |  | |   |<< |<< > | | |    | 
|\| |  | | < | |<>' |<< |>>|   | >> |  | |<< --  --  | |\| | >> | 
| | '<<' |   | |__' |__ |  \   '__| '<<' |__ >>| >>| | | | '__| > 

"""

import random

def game_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return 10
  elif difficulty == 'hard':
    return 5

    
print(logo)
number = random.randint(1,100)

print("Welcome to the number guessing game!\n I am thinking of a number between 1-100.")
# print(f"psst the number is {number}")
lives = game_difficulty()

while lives > 0:
  print(f"You have {lives} attempts to guess the number.")
  guess = int(input("Make a guess: "))

  if guess > number:
    print("Too high.")
    print("Guess again.")
    lives -= 1
  elif guess < number:
    print("Too low.")
    print("Guess again.")
    lives -= 1
  else:
    print(f"You got it! The number was {number}")
    lives = 0