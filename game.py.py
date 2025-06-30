import random

# ASCII art representations for rock, paper, and scissors
rock_art = '''
    _______
---'   ____)
      (_____)
      (_____ )
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices to display based on index
choices_visuals = [rock_art, paper_art, scissors_art]

# Get user input and display their choice
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
print(f"""
You Chose:
{choices_visuals[user_input]}
""")

# Generate random choice for computer
computer_input = random.randint(0, 2)
print(f"""
Computer Chose:
{choices_visuals[computer_input]}
""")

# Determine the winner
if user_input == computer_input:
    print("It's a Tie!!")
elif (user_input == 0 and computer_input == 2) or \
     (user_input == 1 and computer_input == 0) or \
     (user_input == 2 and computer_input == 1):
    print("You Win!!")
else:
    print("You Lose!!")