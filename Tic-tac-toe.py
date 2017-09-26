def play_tic_tac_toe():
 
  def draw_board(table):
    print('\n')
    print(table[0:3])
    print(table[3:6])
    print(table[6:9])
    print('\n')
  def checker(table,strikes):
      count = 0
      for a in strikes:
        if table[a[0]] == table[a[1]] == table[a[2]] == "X":
          print("Player 1 Wins!\n")
          print("Congratulations!\n")
          return True
        if table[a[0]] == table[a[1]] == table[a[2]] == "O":
          print("Player 2 Wins!\n")
          print("Congratulations!\n")
          return True
      for a in range(9):
        if table[a] == "X" or table[a] == "O":
          count += 1
        if count == 9:
          print("The game ends in a Tie\n")
          return True
          
  player1 = input('\t Player 1, please enter name:')
  player2 = input('\t Player 2, please enter name:')
  print('\n', player1, "will be using 'X' and", player2,"will be using 'O'\n")
  players_want_to_play = True
  current_player = player1
  print('\n',player1,"will go first.")

  while players_want_to_play == True:
    
    table = [1,2,3,4,5,6,7,8,9]
    strikes = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    num_turns = 0
    stop = False
    valid_play = True
  
    while num_turns < 9 and stop != True:
      
      draw_board(table)
      position = int(input(current_player + ', enter position:'))
      if position < 1 or position > 9:
        print('This position does not exist, try again')
        valid_play = False
      else:
        valid_play = (table[position-1] == position)
      
      while (valid_play == False):
        print('Invalid position:',position,'. Try Again')
        position = int(input(current_player + ', enter position:'))
        if position < 1 or position > 9:
          print('This position does not exist, try again')
        else:
          valid_play = (table[position-1] == position)
      
      #updating the table
      if current_player == player1:
        table[position-1] = 'X'
      else:
        table[position-1] = 'O'
      
      # Switches player.
      current_player = player2 if current_player == player1 else player1
    
      num_turns += 1
      stop = checker(table,strikes)
      if stop == True:
        break
  
    draw_board(table)
    
    keep_playing = input('Do you want to keep playing? \n Type yes or no\n -->')
    if keep_playing in ('yes','ye','y','Yes'):
      players_want_to_play = True
    elif keep_playing in ('No','no','n'):
      players_want_to_play = False
      
    
  print('Done playing. Bye bye!')

play_tic_tac_toe()