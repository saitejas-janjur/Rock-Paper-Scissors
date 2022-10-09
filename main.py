import random

player = 0
comp = 0
ties = 0
global p1move, cmove, round


def sayInstructions():
  print(
    "A classic two-person game. Players start each round by saying, “rock, paper, scissors, shoot!” On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors. Rock crushes scissors, cissors cut paper, and paper covers rock. See who wins each round!"
  )


def getPlayer1Move():
  p1move = (int(
    input(
      "What move would you like to play? Rock is 1, Paper is 2, Scissors is 3: "
    )))
  return p1move


def getComputerMove():
  cmove = (random.randint(1, 3))
  return cmove


def getRounds():
  roundnum = (int(input("How many rounds would you like to play? ")))
  return roundnum


def getRoundWinner(p1move, cmove):
  global ties, computer, player
  ties = 0
  computer = 0
  player = 0
  if (p1move > cmove):
    player += 1
  elif (p1move < cmove):
    computer += 1
  else:
    ties += 1


def rps(roundnum):
  num1 = getPlayer1Move()
  num2 = getComputerMove()
  num3 = getRoundWinner()
  roundnum = getRounds()
  print("The current score of the game is: ", player, " and ", computer)
  print(player)
  print(computer)
  print(ties)


def main():
  print("Welcome to Rock, Paper, and Scissors.")
  question = input(
    "Would you like the instructions for Rock Paper Scissors? (Yes/No): ")
  if (question == "Yes" or question == "yes"):
    print(
      "A classic two-person game. Players start each round by saying, “rock, paper, scissors, shoot!” On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors. Rock crushes scissors, cissors cut paper, and paper covers rock. See who wins each round!"
    )
  else:
    print("Okay.")


rps(1)
