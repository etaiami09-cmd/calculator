from display import *
from inputs import *
def main():
    print("Welcome to the calculator application!")
    while True:
        num1=0
        num2=0
        display_options()
        go_back = False
        choice, go_back = get_choice()
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
        display_result(result)
        input()

if __name__=='__main__':
    main()