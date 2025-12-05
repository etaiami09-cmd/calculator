import sys
import asyncio
from display import *
from inputs import *
from history import Tracker
from utils import *
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
def main():
    print("Welcome to the calculator application!")
    tracker = Tracker()
    while True:
        num1=0
        num2=0
        go_back = False
        choice, go_back = prompt_choice(tracker)
        if go_back:
            continue
        request_number(1)
        num1, go_back = get_number(1)
        if go_back:
            continue
        request_number(2)
        num2, go_back = get_number(2)
        if go_back:
            continue
        if choice==1:
            result = num1+num2
        elif choice==2:
            result = num1-num2
        elif choice==3:
            result = num1*num2
        else:
            try:
                result = num1/num2
            except ZeroDivisionError:
                div_zero_complain()
                input()
                continue
        result = safe_floats(result)
        num1 = safe_floats(num1)
        num2 = safe_floats(num2)
        display_result(result)
        tracker.add_calculation(f'{num1}{string_operations()[choice]}{num2}={result}')
        input()

if __name__=='__main__':
    main()