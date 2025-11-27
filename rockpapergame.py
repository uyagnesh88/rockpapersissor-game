import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

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

game_images = [rock,paper,scissors]

user_choice = input("what do you chosse? type 0 for rock, 1 for papper or 2 for scissors")
if user_choice >= 0 and user_choice <= 2:
   print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer choose :")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you wins!")
elif computer_choice ==0 and user_choice ==2:
    print("you lose!")
elif computer_choice > user_choice:
    print("computer lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw!")
elif user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lose!")
else:
    print("you typed an invalid number. you lose!")
