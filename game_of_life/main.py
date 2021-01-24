from functions import *
from time import sleep
import os


def clear():
    # for Windows
    if os.name == "nt":
        _ = os.system("cls")
    # for Mac and Linux(here, os.name is 'posix')
    else:
        _ = os.system("clear")


state = load_state_from_file("states/state_glider_gun.txt")


# Run simulation
for _ in range(1_000):
    display(state)
    state = get_next_state(state)
    sleep(0.1)
    clear()