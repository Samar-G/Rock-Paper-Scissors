import random

options = ["Rock", "Paper", "Scissors"]

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

figures = [rock, paper, scissors]

user = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors:"))
print(figures[user])

randComp = random.randint(0, len(options)-1)

print("Computer chose:", randComp, ",", options[randComp])
print(figures[randComp])

if user == randComp:
    print("It is a DRAW!")
elif (user == 2 and randComp == 0) or (user == 0 and randComp == 1) or (user == 1 and randComp == 2):
    print("You LOSE!")
else:
    print("You WON!")
