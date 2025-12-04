def main():
    print("Welcome to the calculator application!")
    while True:
        go_back = False
        print("==============================================")
        print("Please choose one of the following operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("==============================================")
        print("Enter your choice:")
        try:
            choice = int(input())
        except ValueError:
            print("That is not a valid input!")
            print("Press Enter to restart.")
            input()
            continue
        if choice not in [1,2,3,4]:
            print("That is not a valid input!")
            print("Press Enter to restart.")
            input()
            continue
        print("==============================================")
        print("enter your first number:")
        print("==============================================")
        while True:
            try:
                num1 = float(input())
                break
            except ValueError:
                print("That is not a valid input!")
                print("Press Enter to try again or enter 1 to go back")
                if (input()=='1'):
                    go_back = True
                    break
        if go_back:
            continue
        print("==============================================")
        print("enter your second number:")
        print("==============================================")
        while True:
            try:
                num2 = float(input())
                break
            except ValueError:
                print("That is not a valid input!")
                print("Press Enter to try again or enter 1 to go back")
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
                print("ERROR")
                print("Cannot divide by zero!")
                print("Press Enter to return to start.")
                input()
                continue
        print("==============================================")
        print(f"Result: {result}")
        print("==============================================")
        print("Press Enter to go back to start.")
        input()

if __name__=='__main__':
    main()