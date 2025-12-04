from display import *
def main():
    print("Welcome to the calculator application!")
    while True:
        display_options()
        go_back = False
        try:
            choice = int(input())
        except ValueError:
            bad_input()
            input()
            continue
        if choice not in [1,2,3,4]:
            bad_input()
            input()
            continue
        request_number(1)
        while True:
            try:
                num1 = float(input())
                break
            except ValueError:
                bad_input()
                if (input()=='1'):
                    go_back = True
                    break
        if go_back:
            continue
        request_number(2)
        while True:
            try:
                num2 = float(input())
                break
            except ValueError:
                bad_input()
                if (input()=='1'):
                    go_back=True
                    break
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