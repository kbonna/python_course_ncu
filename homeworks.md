# Homework 1.

**1.1.** Write a script (or function) that takes as an input two numbers `width` and `height` and prints a rectangle with specified size. 

Examples: 
- `width=5` and `height=4` should result in terminal output:

```
#####
#   #
#   #
#   #
#####
```
- `width=7` and `height=2` should result in terminal output:
```
#######
#######
```
- `width=1` and `height=1` should result in terminal output:
```
#
```

**1.2.** Sum all perfect squares (numbers that are equal to the square of other number – 1, 4, ..., 9, 16, 25, 36, 49, ..., 9801, 10000) in range between 0 and 10000.

**1.3.** Write a script for setting an alarm, which ask users whether they are employed (yes / no) and whether they are currently on vacation (yes / no). User should answer typing either `Y` for yes or `N` for no. If user specify incorrect answer (anything that is not `Y` or `N`) program should warn user about incorrect answer and ask again.

The script output `True` if user is employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should output `False` otherwise. Examples:

Examples:
- setting an alarm
```
> Are you employed? (Y/N):
> y
> Incorrect answer.
> Are you employed? (Y/N):
> Y
> Are you on vacation (Y/N):
> N
> True
```
- not setting an alarm
```
> Are you employed? (Y/N):
> N
> Are you on vacation (Y/N):
> N
> False
```
