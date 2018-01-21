import random

computer_input = random.randint(1,10)

def game_input():
  count = 0
  while count < 5 :
    try:
      player_input = int(input("Enter number"))
    except ValueError:
      print("The value {} you entered is not a number".format(player_input))
    else:
      if (player_input == computer_input):
        print("It is a hit")
        break
      else:
        if (player_input < computer_input):
          print("Your number is below computer guess")
        elif (player_input > computer_input):
          print("Your number {} is above computer guess".format(player_input))
        print("It is a miss")
    count += 1

def game():
  while True:
    game_input()
    exit_decision = input("Do you want to play again? Y?N")
    if exit_decision.upper() == "N":
      quit()
    else:
      game_input()

game()