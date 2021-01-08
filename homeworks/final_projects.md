# General rules & guidelines

1. You should not use any external Python library without prior permission (standard library is allowed). You can ask for permission to use libraries that will help you visualize the problem or make the interaction between the user and program more "professional" (e.g. creating GUI).
2. Be sure that the program works, and won't "crash" when user / player provide unexpected input. As a rule of thumb, all user inputs (e.g. game moves) should be validated before further processing. If the validation fails, user should be prompted again.
3. Try to break down your code into smaller, reusable functions that are easy to test and understand. Try to document your functions using docstrings. If you have time, write tests for the most critical functions.
4. Focus on completing each milestone separately and then try to merge them together into single working program.
5. If you have any questions or struggle with your code **just ask or join consultation**!

# Project 1 "Battleship"

### Description

Create ["Battleship" game](<https://en.wikipedia.org/wiki/Battleship_(game)>) using Python. Player should be able to play against computer. Game features:

- game should consist of two phases (setup phase and shooting phase)
- during setup phase user can lay out all ships using just console commands or can upload his initial board setup from file (one or the other, you don't have to implement both). Setup phase **should be validated** using standard Battleship rules – ships cannot touch or cross each other, etc.
- during shooting phase player should see current situation on his own board and his enemy board (e.g. board can be nicely printed to the console before each shot)
- at each turn player can select the field to shoot (this fild has to be also validated, e.g. same field cannot be hit twice)
- player should be informed about sinking enemy ship
- game should be automatically ended whenever one of the two players win (appropriate message should be displayed to the user)

### Milestones:

1. Create a function that either load a board setup from file (think about your own representation, e.g. `1` for a ship and `0` for empty field) or ask user to place all the ships (for example by passing board coordinates for both ends of the ship, e.g. (1, 3) – (1, 5) would represent ship with lenght 2)
2. Create a function that validates board setup. This function can chceck if all ships are present and if ships are not touching each other (this is usually forbidden).
3. Create a function that allows you visualize the board in any given time (e.g. by printing it to the console).
4. Create a function that allows you to shoot the field of enemy and returns a new board and feedback if you hit enemy ship.
5. Create a function that shoots your field.
6. Create a game loop where you and computer can make subsequent shots until all ships are sunk.

### Extra credit

- if you want, you can make computer play intelligent, not random
- if you want, you can add an option to randomly place player ships

# Project 2 "Mastermind"

### Description

Create ["Mastermind" game ](<https://pl.wikipedia.org/wiki/Mastermind_(gra_planszowa)>) using Python. You can choose if the player has the role of codebraker or codemaker (you can choose one or the other). Game features in both cases:

- if the player is codemaker:
  - he should be asked to create secret code at the beginning of the game
  - he should see each guess of the computer (response to guess should be generated automatically)
  - computer should guess according to strategy enabling him to win within maximum number of guesses (usually 12)
- if the player is codebreaker:
  - computer should automatically generate secret code at the beginning of the game
  - player should be able to make a guess at each turn (e.g. typing `"BGYY"` representing peg color sequence to the console)
  - player should receive correct feedback after each guess
  - player should be informed about breaking the code or loosing after using all attempts

Board representation could be nicely printed string to the console depending on the current game situation.

### Milestones codemaker

1. Create a function that visualize the current status of the board.
2. Create a function that create a feedback according to the current guess and secret code.
3. Create a function that creates next guess (of the computer) depending on previous guesses and feedbacks (you should implement some sort of algorithm to make smart guesses).
4. Create a function that asks user for the secret code and return its representation (e.g. as a list).
5. Create a game loop. In each iteration, computer should take next guess until it finds correct solution or reach maximum number of attempts.

### Milestones codebraker

See milestones 1. 2. of codemaker.

3. Create a function that ask user for the next guess.
4. Create function that creates and set random secret code at the beginning of the game.
5. Create a game loop. In each iteration, user should takek the next guess until correct solution is found or maximum number of attepmts is reached.

### Extra credit

- if you want, you can use external library to produce colorful board output
- if you want, you can provide a hint system for the player playing as codebreaker

# Project 3 "Chess move validator"

### Description

Create a program that takes as an input chess board representation (e.g. from file formatted according to your specification) and return the file with the list of possible moves for all detected pieces (again, you can create your own specification as long as it is consistent).

Program should take into account:

- each piece movement pattern
- ability to capture enemy pieces
- forbidden moves leading to checking the king

### Milestones

1. Create a function to load chessboard representation from file (you can read [this](<https://en.wikipedia.org/wiki/Board_representation_(computer_chess)>) for ideas)
2. Create a function that for a chessboard field and piece type return all possible unrestricted movements.
3. Create a function that for a chessboard field and given pieces setup determine if this field is attacked by the enemy piece (it will be used to determine if this field is allowed due to possibility of checking the king)
4. Create a function that saves all moves (e.g. represented as dictionary) to file.
5. Create a function that detect all possible moves of a piece for a given setup (use functions from 2. and 3.)

### Extra credit

- if you want, you can create full chess game for two players using validator and Python console to draw the board and input next moves
- if you want, you can include en passant and castling moves
