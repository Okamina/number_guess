"""
Program:
Randomly roll a pair of dice
Add the values of the roll
Ask the user to guess a number
Compare the user's guess to the total value
Decide a winner
Inform the user who the winner is"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(input("Guess a number: "))
  return user_guess
  
def roll_dice():
  number_of_sides = randint(6, 12)
  game_continues = True
  user_game_winner = False
  max_val = number_of_sides * 2
  print ("The maximum possible value is: " + str(max_val))
  sleep(1)
  print ("First rolling...")
  sleep(1)
  first_roll = randint(1, number_of_sides)
  print ("Second rolling...")
  sleep(1)
  second_roll = randint(1, number_of_sides)
  total_roll = first_roll + second_roll
  round_number = 1
  
  while game_continues == True:
    print (str(round_number) + " round")
    print
    user_guess = get_user_guess()
    if user_guess > max_val:
      print
      print ("ERROR. That number is larger than the total possible value. End of the game")
      round_number += 1
    elif user_guess > total_roll:
      print
      print ("Below.")
      round_number += 1
    elif user_guess < total_roll:
      print
      print ("Above.")
      round_number += 1
    elif user_guess == total_roll:
      game_continues = False
      user_game_winner = True
    else:
      print ("ERROR. Something whant wrong. Try again")

    if round_number > 3:
      game_continues = False

  print ("Result...")
  sleep(1)
  print ("First roll: %d" % (first_roll))
  sleep(1)
  print ("Second roll: %d" % (second_roll))
  print
  print ("Total...")
  sleep(1)
  print ("%d" % (total_roll))
  if user_game_winner == True:
    print ("You WON! Super")
    return
  else:
    print ("You lose")       
    return  
  
roll_dice()