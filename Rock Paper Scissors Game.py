rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
computer_options = [rock, paper, scissors]
human_options = [rock, paper, scissors]
human_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors:\n ")) -1
if human_choice > 3 or human_choice < 0:
  print("Invalid Value. You Lose!")
computer_choice = random.randint(0,2)

##Want to avoid not null instances (figuring out still)
#input_error = isinstance(human_choice,int)
#if input_error == True:
#  print()

##Human Choice
print(f"\nYour choice:\n {human_options[human_choice]}")
##Print Computer Choice
print(f"\nComputer Choice:\n {computer_options[computer_choice]}")

##My Logic for Rock paper scissors:

if human_choice > computer_choice:
  if computer_choice == 0 and human_choice == 2:
    print("You Lose")
  else:
    print("You Win")
elif human_choice == computer_choice:
  print("Draw")
elif human_choice == 0 and computer_choice == 2:
  print("You win")
else:
  print("You Lose")

##Solution Logic:
# if human_choice > 3 or human_choice < 0:
#   print("Invalid Value. You Lose!")
# elif human_choice > computer_choice:
#   if computer_choice == 0 and human_choice == 2:
#     print("You Lose")
#   else:
#     print("You Win")
# elif human_choice < computer_choice:
#   if computer_choice == 2 and human_choice == 0:
#     print("You Win")
#   else:
#     print("You Lose")
# elif human_choice == computer_choice:
#   print("Its a Draw!")