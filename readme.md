# Introduction
Welcome to the Tic-Tac-Toe game! This simple console-based game allows two players to take turns and compete against each other on a customizable game board.

## Getting Started

### Prerequisites

Before you begin, make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ybakyurek/AS2_tictoctoe.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tic-tac-toe
   ```

### Running the Game

1. Open your terminal and navigate to the project directory.

2. Run the following command to start the game:

   ```bash
   python3 tic_tac_toe.py
   ```

# How to Play
1. **Game Board Size:**
   - When you run the program, it will prompt you to enter the size of the Tic-Tac-Toe game board. Enter an integer value equal to or greater than 3.
   - The standard Tic-Tac-Toe game has a 3x3 board, but this implementation allows for a customizable size, providing a more challenging experience.

2. **Game Board Representation:**
   - The game board is represented by a grid of numbers, where each number corresponds to a cell on the board.
   - Players take turns entering the number of the cell where they want to place their symbol ('X' for Player 1 and 'O' for Player 2).

3. **Winning the Game:**
   - The game checks for a winner after each move, considering rows, columns, and diagonals.
   - If a player successfully places their symbol in a complete row, column, or diagonal, they win the game.
   - The game will display the winning player and exit.

4. **Game Progress and Input Validation:**
   - The game continues indefinitely, allowing players to take turns until there is a winner or a draw.
   - If a player tries to make an invalid move (e.g., selecting a cell that is already occupied or entering an out-of-range number), the game will prompt them to make a valid move.

5. **Ending the Game:**
   - If all cells on the board are filled with 'X' and 'O' without a winner, the game ends in a draw.

# Example Gameplay
```bash
What size Game tictactoe? 3
 0 1 2
 3 4 5
 6 7 8
Player 1 turn --> 0
 X 1 2
 3 4 5
 6 7 8
Player 2 turn --> 4
 X 1 2
 3 O 5
 6 7 8
Player 1 turn --> 2
 X 1 X
 3 O 5
 6 7 8
Player 2 turn --> 1
 X O X
 3 O 5
 6 7 8
Player 1 turn --> 5
 X O X
 3 O X
 6 7 8
Player 2 turn --> 7
 X O X
 3 O X
 6 O 8
Winner: O
```

# Enjoy the Game!
Have fun playing Tic-Tac-Toe! Customize the board size for a different challenge, and may the best player win. If you encounter any issues or have suggestions for improvement, feel free to contribute or provide feedback. Happy gaming!
