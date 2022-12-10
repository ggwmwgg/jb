## TicTacToe (from JetBrains Academy)

#### Program usage: 
TicTacToe (Console) Game

#### Technologies used:
- *Python/BeautifulSoup/Requests*

#### Usage 
```
python tictactoe.py
```

### Implementation:
(The greater-than symbol followed by a space (```> ```) in examples represents the user input. It's not part of the input.)

- Prints an empty grid at the beginning of the game.
- Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
- The first player has to play as X and their opponent plays as O.
- Ends the game when someone wins or there is a draw.
- Example: 

```
> python tictactoe.py
```

```
---------
|       |
|       |
|       |
---------
> 2 2
---------
|       |
|   X   |
|       |
---------
> 2 2
This cell is occupied! Choose another one!
> two two
You should enter numbers!
> 1 4
Coordinates should be from 1 to 3!
> 1 1
---------
| O     |
|   X   |
|       |
---------
> 3 3
---------
| O     |
|   X   |
|     X |
---------
> 2 1
---------
| O     |
| O X   |
|     X |
---------
> 3 1
---------
| O     |
| O X   |
| X   X |
---------
> 2 3
---------
| O     |
| O X O |
| X   X |
---------
> 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
```

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.
