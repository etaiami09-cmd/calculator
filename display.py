from history import Tracker
def display_options():
    print("==============================================")
    print("Please choose one of the following options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show history")
    print("==============================================")
    print("Enter your choice:")
def bad_input():
    print("That is not a valid input!")
    print("Press Enter to restart.")
def bad_input_exit():
    print("That is not a valid input!")
    print("Press Enter to try again or 1 to restart!")
def request_number(index):
    lit_index = "first" if index == 1 else "second"
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
def display_history(tracker):
    print("==============================================")
    print("Calculation history:")
    for calculation in tracker.calculations_by_recent():
        print(calculation)
    print("==============================================")
    print("Press Enter to go back to start.")