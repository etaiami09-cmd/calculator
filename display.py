def display_options():
    print("==============================================")
    print("Please choose one of the following operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("==============================================")
    print("Enter your choice:")
def bad_input():
    print("That is not a valid input!")
    print("Press Enter to restart.")
def request_number(index):
    lit_index = "first" if index == 1 else "first"
    print("==============================================")
    print(f"enter your {lit_index} number:")
    print("==============================================")
def div_zero_complain():
    print("ERROR")
    print("Cannot divide by zero!")
    print("Press Enter to return to start.")
def display_result(result):
    print("==============================================")
    print(f"Result: {result}")
    print("==============================================")
    print("Press Enter to go back to start.")