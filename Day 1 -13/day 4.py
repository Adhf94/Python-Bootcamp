import random
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


game_images = [rock,paper,scissors]
while True:
  choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
  if choice != "0" and choice != "1" and choice != "2":
    if choice != 0 and choice != 1 and choice != 2:
        print("YOU MUST CHOOSE BETWEEN : 0, 1, 2")
  else:
    break
int_choice = int(choice)
AI = random.randint(0,2)

if int_choice == AI:
  print(f"{game_images[int_choice]}\n----------------------\n{game_images[AI]}\n ITS A DRAW.")
elif int_choice == 0 and AI == 2:
  print(f"{game_images[int_choice]}\n----------------------\n{game_images[AI]}\n You win!.")
elif AI == 0 and int_choice == 2:
  print(f"{game_images[int_choice]}\n----------------------\n{game_images[AI]}\n You lose!.")
elif AI > int_choice:
  print(f"{game_images[int_choice]}\n----------------------\n{game_images[AI]}\n You lose!.")
elif int_choice > AI:
  print(f"{game_images[int_choice]}\n----------------------\n{game_images[AI]}\n You win!.")
