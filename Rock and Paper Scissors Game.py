import random

# Define options for the game
options = ["rock", "paper", "scissors"]

# Function to get user input
def get_user_choice():
  while True:
    choice = input("Choose rock, paper, or scissors (r/p/s): ").lower()
    if choice in options:
      return choice
    else:
      print("Invalid input. Please enter 'r', 'p', or 's'.")

# Function to generate computer's choice
def get_computer_choice():
  return random.choice(options)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Tie"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "Win"
    else:
      return "Lose"
  else:
    if computer_choice == "paper":
      return "Win"
    else:
      return "Lose"

# Function to play a round
def play_round():
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()
  result = determine_winner(user_choice, computer_choice)

  print(f"You chose {user_choice}, computer chose {computer_choice}.")
  print(f"Result: {result}")

# Function to play the game
def play_game():
  while True:
    play_round()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
      break

# Start the game
play_game()