from display import *
from history import Tracker
def get_choice(tracker):
    try:
        choice = int(input())
    except ValueError:
        bad_input()
        input()
        return 0, True
    if choice not in [1,2,3,4,5]:
        bad_input()
        input()
        return 0, True
    if choice==5:
        display_history(tracker)
        input()
        return 0, True
    return choice, False
def get_number(index):
    while True:
        try:
            num = float(input())
            break
        except ValueError:
            bad_input_exit()
            if input()=='1':
                return 0, True
            request_number(index)
    return num, False