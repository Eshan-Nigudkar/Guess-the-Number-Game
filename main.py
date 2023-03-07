#Number Guessing Game Objectives:
import random
from art import logo
print(logo)


# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

  
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_answer(guess, answer, turns):
    if guess>answer:
      print("Too High")
      return turns-1
    elif guess<answer:
      print("Too Low")
      return turns-1
    else:
      print(f"That's Correct. The answer is {answer}.")
    

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print("Welcome to the Number guessing game!")
  print ("I am thinking of a number from 1 to 100.")
  answer=random.randint(0,100)
  
  turns=difficulty()
  guess=0
  while guess !=answer:
    print(f"You have {turns} turns left.")
    guess= int(input("Make a guess: "))
    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

## Another method for the same problem

# def user_guess():
#   global guess
#   number=int(input("Make a guess: "))
#   guess=False
#   while not guess:
#     if number>a:
#       print("Too high")
#       break
#     elif number<a:
#       print("Too Low")
#       break
#     elif number==a:
#       print(f"Correct! The number is {a}")
#       guess=True
#       break
#     return guess
# difficulty_level= input("Chose difficulty level: Easy or Hard: ").lower()
# if difficulty_level=="easy":
#   count=10
#   print("You have 10 guesses.")
# elif difficulty_level=="hard":
#   count=5
#   print("You have 5 guesses.")
# user_guess()
# while not guess:
 
#   count-=1
#   print(f"You have {count} guesses.")
#   user_guess()
#   if count ==0:
#     print("You ran out of guesses.")
#     guess=True
#     break