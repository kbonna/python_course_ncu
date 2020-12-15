# General rules & guidelines

1. You should not use any external Python library without prior permission. You can ask for permission to use libraries that will help you visualize the problem or make the interaction between the user and program more "professional" (e.g. creating GUI).
2. Be sure that the program works, and won't "crash" when user / player provide unexpected input. As a rule of thumb, all user inputs (e.g. game moves) should be validated before further processing. If the validation fails, user should be prompted again.
3. Try to break down your code into smaller, reusable functions that are easy to test and understand. Try to document your functions using docstrings. If you have time, write tests for the most critical functions.

# Project 1 "Battleship"

Create ["Battleship" game](https://en.wikipedia.org/wiki/Battleship_(game)) using Python. Player should be able to play against computer. Game features:
- game should consist of two phases (setup phase and shooting phase)
- during setup phase user can lay out all ships using just console commands or can upload his initial board setup from file (one or the other, you don't have to implement both). Setup phase **should be validated** using standard Battleship rules – ships cannot touch or cross each other, etc.
- during shooting phase player should see current situation on his own board and his enemy board (e.g. board can be nicely printed to the console before each shot)
- at each turn player can select the field to shoot (this fild has to be also validated, e.g. same field cannot be hit twice)
- player should be informed about sinking enemy ship
- game should be automatically ended whenever one of the two players win (appropriate message should be displayed to the user)

Extra credit:
- if you want, you can make computer play intelligent, not random
- if you want, you can add an option to randomly place player ships

# Project 2 "Mastermind"

Create ["Mastermind" game ](https://pl.wikipedia.org/wiki/Mastermind_(gra_planszowa)) using Python. Player should be able to select either the role of codebraker or codemaker. Game features:
- if the player is codemaker:
    - he should be asked to create secret code at the beginning of the game
    - he should see each guess of the computer (response to guess should be generated automatically)
    - computer should guess according to strategy enabling him to win within maximum number of guesses
- if the player is codebreaker:
    - computer should automatically generate secret code at the beginning of the game
    - player should be able to make a guess at each turn (e.g. typing `"BGYY"` representing peg color sequence to the console)
    - player should receive correct feedback after each guess
    - player should be informed about breaking the code or loosing after using all attempts
    
Board representation could be nicely printed string to the console depending on the current game situation. Board representation should be similar for player playing as either codemaker or codebraker. 

Extra credit:
- if you want, you can use external library to produce colorful board output
- if you want, you can provide a hint system for the player playing as codebreaker

# Project 3 "Chess move validator"

Create a program that takes as an input chess board representation (e.g. from file formatted according to your specification) and return the file with the list of possible moves for all detected pieces (again, you can create your own specification as long as it is consistent). 

Program should take into account:
- each piece movement pattern 
- ability to capture enemy pieces
- forbidden moves leading to checking the king
    
Extra credit:
- if you want, you can create full chess game for two players using validator and Python console to draw the board and input next moves
- if you want, you can include en passant and castling moves