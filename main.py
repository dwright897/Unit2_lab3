# Dalton Wright
# Tic-Tac_Toe
# 10/27/24
from tic_tac_toe import TicTacToe
import random
def player_move(game):
  '''this gets the player move'''
  goal = True
  while goal == True:
    try:
      row = int(input("Enter Row (0,1,2):"))
      col = int(input("Enter Column (0,1,2):"))
      if 0 <= row < 3 and 0 <= col < 3:
        pt = game.place_token(row,col)
        if pt:
          goal = False
        else: 
          print("This spot is already taken!")
      else: 
        print("Please enter a number between 0 and 2!")
    except:
      print("Please enter a number between 0 and 2!")

def computer_move(game):
  '''this generates the computers move'''
  spot = True
  while spot:
    row = random.randint(0,2)
    col = random.randint(0,2)
    if game.place_token(row,col):
      spot = False










def main():
  game = TicTacToe()
  count = 9
  goal = True
  
  while goal == True:
    count -=1
    print("\n")
    print (game)
    if game.get_turn()=='x':
      player_move(game)
    else:
      computer_move(game)
      
    if game.is_winner():
      print("\n")
      print(game)
      print(f"\n\nPlayer {game.get_turn()} wins!")
      goal = False
        
    if count == 0:
      print(f"\n\nNobody wins, its a draw!")
      goal = False
    

        

    



if __name__=="__main__":
  main()