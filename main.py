import random

player_1_score = 0
player_2_score = 0
ties = 0


def sayInstructions():
  print("A classic two-person game. Players start each round by saying, “rock, paper, scissors, shoot!” On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors. Rock crushes scissors, cissors cut paper, and paper covers rock. See who wins each round!")
  
def selectGameMode():
  value = (int(input("Type 1 for for regular Rock-Paper-Scissors game or type 2 for Rock-Paper-Scissors-Lizard-Spock game: ")))
  
  game_mode = (int(input("Type 1 for 1 player mode(with computer) or type 2 for 2 player mode: ")))
  
  if value == 1 and game_mode == 1:
    return 1
  elif value == 1 and game_mode == 2:
    return 2
  elif value == 2 and game_mode == 1:
    return 3
  elif value == 2 and game_mode == 2:
    return 4

def getPlayer1Move():
  print("Player 1 Move")
  p1move = (int(
    input(
      "What move would you like to play? Rock is 1, Paper is 2, Scissors is 3: "
    )))
  return p1move


def getPlayer1_Move_5_mode():
  print("Player 1 Move")
  p1move = (int(
    input(
      "What move would you like to play? Rock is 1, Paper is 2, Scissors is 3, Lizard is 4 and Spock is 5: "
    )))
  return p1move

def getPlayer2Move():
  print("Player 2 Move")
  p2move = (int(
    input(
      "What move would you like to play? Rock is 1, Paper is 2, Scissors is 3: "
    )))
  return p2move

def getPlayer2_Move_5_mode():
  print("Player 1 Move")
  p2move = (int(
    input(
      "What move would you like to play? Rock is 1, Paper is 2, Scissors is 3, Lizard is 4 and Spock is 5: "
    )))
  return p2move

def getComputerMove():
  cmove = (random.randint(1, 3))
  return cmove

def getComputerMove_5_mode():
  cmove = (random.randint(1, 5))
  return cmove


def getRounds():
  roundnum = (int(input("How many rounds would you like to play? ")))
  return roundnum


def getRoundWinner(p1move, p2move):
  if p1move == 1:
    if p2move == 2:
      return "player_2"
    elif p2move == 3:
      return "player_1"
    else:
      return "tie"

  elif p1move == 2:
    if p2move == 3:
      return "player_2"
    elif p2move == 1:
      return "player_1"
    else:
      return "tie"

  elif p1move == 3:
    if p2move == 1:
      return "player_2"
    elif p2move == 2:
      return "player_1"
    else:
      return "tie"


def getRoundWinner_5_mode(p1move, p2move):
  if p1move == 1:
    if p2move == 2 or p2move == 5:
      return "player_2"
    elif p2move == 3 or p2move == 4:
      return "player_1"
    else:
      return "tie"

  elif p1move == 2:
    if p2move == 3 or p2move == 4:
      return "player_2"
    elif p2move == 1 or p2move == 5:
      return "player_1"
    else:
      return "tie"

  elif p1move == 3:
    if p2move == 1 or p2move == 5:
      return "player_2"
    elif p2move == 2 or p2move == 4:
      return "player_1"
    else:
      return "tie"

  elif p1move == 4:
    if p2move == 1 or p2move == 3:
      return "player_2"
    elif p2move == 2 or p2move == 5:
      return "player_1"
    else:
      return "tie"

  elif p1move == 5:
    if p2move == 2 or p2move == 4:
      return "player_2"
    elif p2move == 1 or p2move == 3:
      return "player_1"
    else:
      return "tie"


def rps(roundnum):
  for i in range(roundnum):
    player1_move = getPlayer1Move()
    computer_move = getComputerMove()
    print("Computer move was:", computer_move)
    round_winner = getRoundWinner(player1_move, computer_move)
    
    if round_winner == "player_1":
      global player_1_score
      player_1_score += 1
      
    elif round_winner == "player_2":
      global player_2_score
      player_2_score += 1
    
    elif round_winner == "tie":
      global ties
      ties += 1
        
    print("player 1 score is:", player_1_score)
    print("Computer score is:", player_2_score)
    print("Number of ties is:", ties)

def rps_5_mode(roundnum):
  for i in range(roundnum):
    player1_move = getPlayer1_Move_5_mode()
    player_2_move = getComputerMove_5_mode()
    round_winner = getRoundWinner_5_mode(player1_move, player_2_move)
    
    if round_winner == "player_1":
      global player_1_score
      player_1_score += 1
      
    elif round_winner == "player_2":
      global player_2_score
      player_2_score += 1
    
    elif round_winner == "tie":
      global ties
      ties += 1
        
    print("player 1 score is:", player_1_score)
    print("player 2 score is:", player_2_score)
    print("Number of ties is:", ties)



def rps_2_player(roundnum):
  for i in range(roundnum):
    player1_move = getPlayer1Move()
    player_2_move = getPlayer2Move()
    round_winner = getRoundWinner(player1_move, player_2_move)
    
    if round_winner == "player_1":
      global player_1_score
      player_1_score += 1
      
    elif round_winner == "player_2":
      global player_2_score
      player_2_score += 1
    
    elif round_winner == "tie":
      global ties
      ties += 1
        
    print("player 1 score is:", player_1_score)
    print("player 2 score is:", player_2_score)
    print("Number of ties is:", ties)

def rps_2_player_5_mode(roundnum):
  for i in range(roundnum):
    player1_move = getPlayer1_Move_5_mode()
    player_2_move = getPlayer2_Move_5_mode()
    round_winner = getRoundWinner_5_mode(player1_move, player_2_move)
    
    if round_winner == "player_1":
      global player_1_score
      player_1_score += 1
      
    elif round_winner == "player_2":
      global player_2_score
      player_2_score += 1
    
    elif round_winner == "tie":
      global ties
      ties += 1
        
    print("player 1 score is:", player_1_score)
    print("player 2 score is:", player_2_score)
    print("Number of ties is:", ties)



def main():
  print("Welcome to Rock, Paper, and Scissors.")
  question = input(
    "Would you like the instructions for Rock Paper Scissors? (Yes/No): ")
  if (question == "Yes"):
    print(" ")
    sayInstructions()
    print(" ")
  else:
    print(" ")
    print("Okay.")
    print(" ")
    
  game_mode = selectGameMode()

  if game_mode == 1:
    number_of_rounds = getRounds()
    print(" ")
    rps(int(number_of_rounds))
    
  elif game_mode == 2:
    number_of_rounds = getRounds()
    print(" ")
    rps_2_player(number_of_rounds)

  elif game_mode == 3:
    number_of_rounds = getRounds()
    print(" ")
    rps_5_mode(number_of_rounds)

  elif game_mode == 4:
    number_of_rounds = getRounds()
    print(" ")
    rps_2_player_5_mode(number_of_rounds)

main()
