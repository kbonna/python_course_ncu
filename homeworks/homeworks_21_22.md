# How to send your homework?

1. Create solutions for your tasks.
2. Put each solution function in a separate python file named `<homework_number>_<task_number>.py`. For example solution for the task **3.1.** should be placed in a file `3_1.py`.
   
   > Note 1. **Your solution function should be named as task requires!**
   
   > Note 2. **Each file should contain only solution function.**
3. Put all of your solutions in the folder named with your index number. For example, if your University index number is 333444, folder should be named `333444`.
4. Compress your files using zip extension (without password protection). Finally your file should be `333444.zip`.

For example if your index is 333444 and you are sending solutions for the first homework your files should have structure (after unzipping `333444.zip`):

```
333444
├── 1_1.py
└── 1_2.py
```

# Homework 1.

**1.1.** Write a function `higher(a, b, c)` that calculates sum and product of three numbers and return higher value as an output. Function should accept as an input three real numbers `a`, `b`, `c` represented as floats and returns higer of the two: `a + b + c` or `a * b * c`.

Examples:

```python
higher(1, 2, 3) # should return 6
higher(0, 1, 1) # should return 2
higher(2, 3, 4) # should return 24
```

**1.2.** Write a function `quadratic_solutions(a, b, c)` that takes as an input three coefficients of quadratic equation `f(x)=ax^2+bx+c` and return number of solutions. Three return values should be possible: 0, 1, and 2.

Examples:

```python
quadratic_solutions(2, 1, 1) # should return 0
quadratic_solutions(4, 2, 1) # should return 1
quadratic_solutions(1, 5, 1) # should return 2
```

# Homework 2.

**2.1.** Write a function `full_price(price, tax)` that calculates full price of a product including tax. New full price should be calculated as `p + tax * p`. Products cheaper than `100` should not be taxed so for them full price is equal to initial price. Assume default tax value as 10 percent. Tax will be a number between 0 (0%) and 1 (100%).

Examples:

```python
full_price(50, tax=0.5) # should return 50 because products under 100 are not taxed
full_price(200, tax=0.5) # should return 300
full_price(200) # should return 220 because default tax is 10%
```

**2.2.** Write a function `max_weight(heigth_in_cm)` that return maximum normal BMI weight for a person `height_in_cm` tall. Assume maximum normal BMI is 25. Function should raise `ValueError` if `height_in_cm` is not positive number.  

Examples:

```python
max_weight(180) # should return 81.0
max_weight(150) # should return 56.25
max_weight(-50) # should raise ValueError
```