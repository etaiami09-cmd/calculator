from display import *
from history import Tracker
from InquirerPy.prompts.list import ListPrompt
from InquirerPy.base.control import Choice
from InquirerPy.utils import InquirerPyStyle
from InquirerPy.utils import get_style
def prompt_choice(tracker):
    style = InquirerPyStyle(dict([
        ("pointer", "#8810ce"),           # Highlighted option
        ("", "#0400ff"),                  # Default text (unselected options)
        ("question", "#e5c07b"),
        ("answer", "#8810ce"),
    ]))
    
    options = [Choice(value=1,name='◉ Add'),
               Choice(value=2,name='◉ Subtract'),
               Choice(value=3,name='◉ Multiply') ,
               Choice(value=4,name='◉ Divide'),
               Choice(value=5,name='◉ View History')]
    choice = ListPrompt(message="Please choose one of the following options:",
                    choices=options,
                    default=1,
                    style=style,
                    qmark='',
                    ).execute()
    if choice==5:
        display_history(tracker)
        input()
        return 0, True
    return choice, False
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