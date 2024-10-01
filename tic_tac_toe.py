import random

class TicTacToe:
  def __init__(self):
    '''initilize the 3x3 board and randomly pick the starting token.'''
    self.__board= [['_']*3 for p in range(3) ]
    self.__turn= random.choice(['x','o'])

  def __check_win(self, player):
    '''checks if the given player has won the game'''
    for i in range(3):
      row_win = True
      col_win = True
      for b in range(3):
        if self.__board[i][b] != player:
          row_win = False
        if self.__board[b][i] != player:
          col_win = False

      diag1_win = self.__board[0][0] == self.__board[1][1] == self.__board[2][2] == player
      diag2_win = self.__board[0][2] == self.__board[1][1] == self.__board[2][0] == player
      if row_win or col_win or diag1_win or diag2_win:
        return True
      else:
        self.switch_turn()

  def switch_turn(self):
    '''this switches to the other players turn'''
    if self.__turn == 'x':
      self.__turn = 'o'
    else:
      self.__turn = 'x'

  def is_winner(self):
    '''returns true if current player has one, else returns false'''
    return self.__check_win(self.__turn)


  def place_token(self,row,col):
    '''this places the current players token in a open cell'''
    
    if self.__board[row][col] == '_':
      self.__board[row][col]=self.__turn
      return True
    else:
      return False


  def __str__(self):
    '''creates a nice display for the user'''
    rows = ""
    for row in self.__board:
      rows +="|"
      for cell in row:
        rows += cell+"|"
        
        #rows+= "|"
      
      rows+="\n"
      
    return rows 
  
  def get_turn(self):
    '''returns the current player'''
    return self.__turn
