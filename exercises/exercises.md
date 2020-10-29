# 1. Basic types

**1.1.** Write a simple script that asks user for the name and year of birth and print greeting and calculated age in one sentence.

**1.2.** Write a simple script that asks user for speed in km/h and converts into mph.

# 2. Flow control

**2.1.** Print decision if user age is greater than 20 and user name has at most 5 characters.

**2.2.** Write a program that calculates the distance of thrown ball. 

Program should ask user for:
- initial velocity (in m/s)
- initial angle (in degrees)
- if there is an initial height

Program should validate user input checking if:
- initial velocity is a number > 0
- initial anlge is a number > 0 and < 90
- initial height is a number > 0 (if it is used)

Wikipedia article about [projectile motion](https://en.wikipedia.org/wiki/Projectile_motion).

You may need:
- program exit: `from sys import exit`
- trigonometric functions: `from math import sqrt, sin, cos`
- limiting number to two decimal points: `{:.2f}'.format(my_number)`

**2.3.** Write a program using while loop that ask user for password exactly three times. If the password is correct display hello message, otherwise display account blocked message. On each incorrect password give appropriate message with remaining number of attempts. Password is `test123`.

**2.4.** Write a program which brute force guess user selected password. Password should be three characters long and may contain lowercase ascii characters, numbers and uppercase ascii characters. Program should terminate after 1 million incorrect password guesses. If the password is found program should output the password and number of attempts required to correctly guess the password. 

You may need:
- strings with ascii characters and digits: `from string import ascii_lowercase, ascii_uppercase, digits`
- function choosing random character from the string: `from random import choice`

> *Play around with different character sets and see how it impacts number of guesses required to find correct password*

> Does the number of guesses depend on the password complexity or character set lenght?

**2.5.**  Write a program (using `while` loop) that determines whether integer is a prime number. Wikipedia article about [primality tesst](https://en.wikipedia.org/wiki/Primality_test)

# 3. Iteration

**3.1.** Sum all numbers from 1 to 1000.

**3.2.** Sum all numbers that doesn't contain digit 1 from 1 to 1000.

You may need:

- checking wheter specific letter is inside string: `letter in string`, e.g. `'a' in 'abc'` should return `True`

**3.3.** Ask user to specify two integers: `a` and `b`. Calculate the sum of all numbers divisible by 3 between `a` and `b`.

**3.4.** Use `for` loop, `range()` function and one of formatting techniques to produce output:

```
sub-0080
sub-0085
sub-0090
sub-0095
sub-0100
sub-0105
sub-0110
sub-0115
sub-0120
```

> *Checking formatting documantiation may be useful*

**3.5.** Write a program that selects random number between 1 and 100 (inclusive) and ask user to take subsequent guesses until the number is guessed correctly. After each guess program should give a feedback if guessed number is too high or too low.

You may need:

- function that returns random intiger from specified range: `from random import randint`

**3.6.** Solve Kata (7 kyu): [Coloured Triangles](https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python)

You may need:

- getting first letter from a string `s`: `s[0]`
- getting i-th letter from a string `s`: `s[i-1]`
- getting last letter from a string `s`: `s[-1]`

> You don't have to write a function at this point. Just write a script which solves the puzzle.

# 4. Functions

**4.1.** Write a function that simulate process of rolling a dice. It should output sum of all throws. If 6 is thrown, then the program should roll again (as many times as needed to throw number other than 6).

Example:

- sequence: `4` should output `4`
- sequence: `6, 1` should output `7`
- sequence: `6, 6, 6, 5` should output `23`

**4.2.** Prove that functions without return statement implicitely return `None`.

**4.3.** Assume we have function with three arguments:

```def fun(a, b, c):
    print(f'a={a}, b={b}, c={c}')
```

Write down all possible and unique ways to call function `fun` to produce output `a=1, b=2, c=3`. 

**4.4.** Solve Kata (8 kyu): [Are You Playing Banjo?](https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python)

**4.5.** Write a function calulating factorial.

**4.6.** Solve Kata (7 kyu): [Credit Card Mask?](https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python)

# 5. Lists

**5.1.** 
