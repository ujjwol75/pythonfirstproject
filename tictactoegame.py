board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

# board display
def print_board(board):
    for i in range(3):
        print()
        for j in range(3):
            print(board[i][j], end='')
            if j < 2:
                print('|', end='')

# user input value
def user_input():
    pos = input("\n Enter any number from 1 to 9: ")
    pos = int(pos) -1
    if pos <= 9:
        return pos
    else:
        pos = input("\n Enter any number from 1 to 9: ")
        pos = int(pos) -1

# position of the player input in board
def place_player(pos, player):
    row = pos // 3
    column = pos % 3
    board[row][column] = player
    return 1
    
        

# check if game tie 
def game_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return
            else:
                continue
    print("The game is tied.")
    game_on = False

# check if column player win
def check_column(j):
    x = 0
    y = 0
    for i in range(3):
        if board[i][j] == 'x':
            x += 1
        if board[i][j] == 'y':
            y += 1
    if x == 3:
        print('x won')
        return game_on == False

    elif y == 3:
        print('y won')
        return game_on == False
    else:
        return game_on == True


# check if row player win
def check_row(j):
    x = 0
    y = 0
    for i in range(3):
        if board[j][i] == 'x':
            x += 1
        if board[j][i] == 'y':
            y += 1
    if x == 3:
        print('x won')
        return game_on == False

    elif y == 3:
        print('y won')
        return game_on == False
    else:
        return game_on == True       

# check diagonal
def check_diagonal(a,b,c):
    var = [a, b, c]
    x = 0
    y = 0
    for i in var:
        if i == 'x':
            x += 1
        if i == 'y':
            y += 1
    if x == 3:
        print('x won')
        return game_on == False

    elif y == 3:
        print('y won')
        return game_on == False
    else:
        return game_on == True 
        



# main function of game tic tac toe
def main():
    counter = 1
    global game_on 
    game_on = True

    while game_on:
        if counter % 2 == 0:
            player = 'y'
        else:
            player = 'x'

        
        pos = user_input()
        place_player(pos, player)
        counter += place_player(pos, player)
        for j in range(3):
            game_on = check_column(j)
            game_on = check_row(j)
        check_diagonal(board[0][0], board[1][1], board[2][2])
        check_diagonal(board[0][2], board[1][1], board[2][0])
        
        print_board(board)
        game_tie()


    


main()
