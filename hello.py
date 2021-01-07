# def divide(a, b):
#     try:
    
#         assert b != 0, "You cannot give denomenator 0."
#         return a/b
#     except:
#         print("Error message, divide by 0")

# div = divide(2, 2)
# print(div)

# import copy
# list1 = [1,3, 4, 5, 6, 43]
# list2 = copy.copy(list1)
# print(list2)

# class demo:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __repr__(self):
#         return '__repr__ for demo'
    
#     def __str__(self):
#         return "__str__for demo"

# o = demo(1, 2)

# print(str(o))
# print(repr(o))


# pip install virtualenv
# virtualenv <name>
# virtualenv activated



# import pygame
# background_colour = (255,255,255)
# (width, height) = (300, 200)
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Tutorial 1')
# screen.fill(background_colour)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             running = False 
# import numpy as np
# array = np.array([[0,1,3],[9,8,7],[8,3,2]])
# print(array)

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
    return pos

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
            player = 'x'
        else:
            player = 'y'

        
        pos = user_input()
        place_player(pos, player)
        counter += place_player(pos, player)
        for j in range(3):
            game_on = check_column(j)
            game_on = check_row(j)
        check_diagonal(board[0][0], board[1][1], board[2][2])
        check_diagonal(board[0][2], board[1][1], board[0][2])
        
        print_board(board)
        game_tie()


    


main()
