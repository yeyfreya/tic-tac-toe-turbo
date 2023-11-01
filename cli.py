from logic import check_winner

def get_empty_board():
    """
    what is "board"?
    row_1 = ['O', 'O', 'O']
    row_2 = ['O', 'O', 'O']
    row_3 = ['O', 'O', 'O']

    board = row_1,
            row_2,
            row_3
    """
    
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print (row) # print row in new line

def get_player_input(current_player):
    """
    input:
        row, col
    return:
        row: int  -> index of row
        col: int  -> index of column
    """ # """" is the way to writ multi-line comments
    
    prompt = f"Player {current_player} >"
    # prompt = f"Player {current_player}, please input your move, e.g. row,col\n" #"\n" -> print a new line
    
    player_input = input(prompt)
    # <-- originally before adding "prompt": player_input = input(f"> ") 
    # # "f" means formatted string, can be used to add players in this case
    # # this is a str input -> "1,1"
    # skip: print(player_input)
    # eg "1,1".split(',') -> ["1", "1"] (split the str by comma)
    #### if want a whole block to become comment, use "cmd + /(?)" for the selected block
    
    
    row_col_list= player_input.split(',') #-> ["1","1"]
    
    # to convert it into numbers -> [1,1]
    row, col = [int(x) for x in row_col_list]

    # how to make the str into two int
    # skip to clean up: row = 0
    # skip to clean up: col = 0
    return row, col

def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"


if __name__ == '__main__': # sheild it from import so that i only run it directly
    
    current_player = 'X'


    # get an empty board
    board = get_empty_board()

   

    winner = None 

    while winner is None:

         #print the board
        print_board(board)

        try:
            row, col = get_player_input(current_player) # ask user input
        except ValueError:
                print("Invalid input, try again")
                continue

        # ask user input
        row, col = get_player_input(current_player)
        # print(row)
        # print(col)

        # mark the board:
        board[row][col] = current_player
        
        
        # swap the player
        current_player = switch_player(current_player)
        # current_player = "X" if current_player == "O" else "O"

        # check for winner
        # check if game is draw
        winner = check_winner(board) # "O"or"X" -> break out of the loop

# print the winner
print_board(board)
print(f"Winner is {current_player}")
        
# control + c: to interrupt the code running
