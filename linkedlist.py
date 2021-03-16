#tictactoe game using python 
board = ['_|','_|','_|',
         '_|','_|','_|',
         '_|','_|','_|']

count = 1
def get_input():
    global count;
    if count % 2 == 0:
        uservalue = input(f"It's user {A} turn.")
    else:
        uservalue = input(f"It's user {B} turn.")
    
def main_game():
    get_input()
