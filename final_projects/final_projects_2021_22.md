# General rules & guidelines

1. Don't ask other people to write code for you. If you won't be able to answer basic questions about your code you will automatically get zero points for the project and fail to pass the class.
2. You should not use any external Python library without prior permission (standard library is allowed). You can ask for permission to use libraries that will help you visualize the problem or make the interaction between the user and program more "professional" (e.g. creating GUI). However, this is not reqire.
3. Be sure that the program works, and won't "crash" when a user provide unexpected input. As a rule of thumb, all user inputs (e.g. game moves, commands) should be validated before further processing. If the validation fails, user should be prompted again or at least informed what went wrong.
4. Try to break down your code into smaller, reusable functions that are easy to test and understand. Try to document your functions using [documentation strings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
5. Focus on completing each milestone separately and then try to merge them together into single working program.
6. If you have any questions or struggle with your code **just ask or join consultation**!
7. Project submission deadline is **03.02.2022**.

# Project 1 "Budget tracker"

### Description

Create budget tracker script/program that takes as an input two files - budget plan and expense list - and output a nicely formatted summary of your budget.

### Requirements

- budget plan should contain information about budget categories and planned expenses for a category
- budget plan should be accepted as a file (preferably csv or tsv - just a text file with some predefined separation between columns)

Example budget plan file:

```
grocery 500
bills 1500
subscriptions 200
party 500
```

- expense list should contain a single record for each expense with expense value, category and date
- you can accept more columns for both budget plan file and expense list file if you want use them in more complex program

Example expense list file:

```
grocery 10.50 01.01.2022
bills 790 01.01.2022
party 125 02.01.2022
clothes 199.99 03.01.2022
grocery 87.39 03.01.2022
...
grocery 60.29 30.01.2022
```

- budget summary should be placed in a separate file (if you want you may ask user to specify filename for this file)
- budget summary should contain information about:
  - total budget, total expenses and a difference
  - total budget for a category, total expenses for a category and a difference
  - how many entries are for each category and on how many different days you made an expense for a category
  - extra points if you can calculate information on which day budget/budget for category was exceeded

Example budget summary file:

```
category      budget  costs   difference  entries unique_days when_exceeded
all           2700    2922.32 222.32      41      29          23.01.2022
grocery       500     512.27  12.27       10      10          25.01.2022
bills         1500    1490    -10         1       1           –
party         125     230.98  105.98      5       3           15.01.2020
subscriptions 200     689.07  489.07      6       4           17.01.2020
```

> **Please note that a conventions showed above are not mandatory, and are just an example.** You can decide on different way of formatting inputs or a different way of presenting a summary.

### Milestones:

1. Create functions that load and validate data from budget plan and expense list files
2. Create a function that aggregate information from different entries of the same category calculating number of unique entries and unique days
3. Create a function that aggregate information about entire budget
4. Create a function that nicely format output table and fill it given calculated data
5. Create a fucntion that saves formatted summary into a file

# Project 2 "Gomoku"

### Description

Create ["Gomoku" game](https://pl.wikipedia.org/wiki/Gomoku) using Python. You should code game interactions, validation of inserted moves, artificial opponent for a player and mechanism determining if the game is over.

### Requirements

- user should be able to choose black or white marbles (or circles/crosses in another version)
- user should have the visual representation of the board before he makes a move
- user input should be validates, so invalid input cannot break the game
- computer should respond after each move with its own move
- extra credit if computer moves are not "dumb", but it is not required
- user should see information who won when the game is over

### Milestones

1. Create a function that visualize the current status of the board.
2. Create a function that validates user input
3. Create a function that responds with the computer generated move
4. Create a function that detects if a game is over and display score after the game
5. Create a game loop which use all above functions
