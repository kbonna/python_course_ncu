# How to send your homework?

1. Create solutions for your tasks.
2. Put each solution function in a separate python file named `<homework_number>_<task_number>.py`. For example solution for the task **3.1.** should be placed in a file `3_1.py`.
   
   > Note. **Your solution function should be named as task requires!**
   
   > Note. **Each file should contain only solution function.**
3. Put all of your solutions in the folder named with your index number. For example, if your University index number is 333444, folder should be named `333444`.
4. Compress your files using zip extension (without password protection). Finally your file should be `333444.zip`.
  
  > Note. **Make sure to compress entire folder, not only solution files.** You can double-check that by unzipping your archive – you should see folder and not solution files.

5. Send solutions to **python.at.ncu@gmail.com**. Your e-mail title should be `Homework <homework_number>`, e.g. `Homework 1`.

For example if your index is 333444 and you are sending solutions for the first homework your files should have structure (after unzipping `333444.zip`):

```
333444
├── 1_1.py
└── 1_2.py
```

# Checklist before sending homework

- [ ] Do my files contain **ONLY** solution function?
 
```python
# This is OK!
def sum_function(a, b):
    return a + b
```
```python
# This is NOT OK!
def sum_function(a, b):
    return a + b
a = float(input("a?"))
b = float(input("b?"))
sum_function(a, b)
```
- [ ] Do my files have correct names? (`1_1.py` is correct, whereas `1.1.py` or `1-1.py` are not)
- [ ] Are my files placed in a directory named with my index number **before compression**? If so, make sure to compress **entire folder** and not only files within!

```
# This is correct structure before compression
333444
├── 1_1.py
└── 1_2.py
```
```
# This is incorrect structure before compression, index directory is missing
├── 1_1.py
└── 1_2.py
```

- [ ] Am I using correct compression format? (`.zip` is correct, whereas `.rar` is not)
- [ ] Am I sending my homework to correct address? (python.at.ncu@gmail.com)
