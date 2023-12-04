#ASSIGNMENT2
#student: Yildirim Bayazit Akyurek
#number:21904343
#section: BBM103

import sys

# Get the size of the tictactoe game from the user
size = int(input('What size Game tictactoe? '))

# Validate the size input
while size < 3:
    size = int(input('Game size must be an integer and equal to or greater than 3: '))

# Create the game board
BoardSize = []
for i in range(size):
    row = []
    for j in range(size):
        j = size * i + j
        row.append(j)
    BoardSize.append(row)

turn = 0

# Function to print the game board
def print_list():
    max_digits = 0
    for i in BoardSize:
        for j in i:
            number_of_digits = len(str(j))
            if number_of_digits > max_digits:
                max_digits = number_of_digits
    for i in BoardSize:
        print_row = ''
        for j in i:
            print_row += f'{j}'.rjust(max_digits + 1, ' ')
        print(print_row)

print_list()

# Function to announce the winner
def winner(A, X):
    if check_equal(A):
        print_list()
        print('Winner:', X)
        sys.exit()

# Function to check if all elements in a list are equal
def check_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

# Function to control the game
def controlling(X):
    for i in range(size):
        control = BoardSize[i].copy()  # row
        winner(control, X)
        control1 = []
        for j in range(size):
            control1.append(BoardSize[j][i])  # column
        winner(control1, X)
        control2 = []
        for i in range(size):
            control2.append(BoardSize[i][i])  # from left upper to right down
        winner(control2, X)
        control3 = []
        for i in range(size):
            control3.append(BoardSize[i][(size - 1) - i])  # from right upper to left down
        winner(control3, X)

# Function to play the game
def play():
    try:
        # If all elements are strings, end the game as a draw
        if all(i.isalpha() for lists in BoardSize for i in lists):
            print('No Winner')
            sys.exit()
    except AttributeError:
        pass

    global turn

    # Player 1 (X) or Player 2 (O) turn
    if turn % 2 == 0:
        print('Player 1 turn --> ', end='')
    else:
        print('Player 2 turn --> ', end='')

    enter = int(input())

    # Validate the user input
    if enter >= size ** 2 or enter < 0:
        print('Please enter a valid number')
        print_list()
    else:
        find_change(enter)
        print_list()

    turn += 1

# Function to find and change the element on the board
def find_change(num):
    global turn
    firstL = num // size
    secondL = num % size

    if turn % 2 == 0:
        if BoardSize[firstL][secondL] == 'X':
            print("You have made this choice before")
        elif BoardSize[firstL][secondL] == 'O':
            print("The other player selected this cell before")
        else:
            BoardSize[firstL][secondL] = 'X'
        controlling('X')
    else:
        if BoardSize[firstL][secondL] == 'O':
            print("You have made this choice before")
        elif BoardSize[firstL][secondL] == 'X':
            print("The other player selected this cell before")
        else:
            BoardSize[firstL][secondL] = 'O'
        controlling('O')

while True:
    play()
