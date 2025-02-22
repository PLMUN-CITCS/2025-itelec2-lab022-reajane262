def display_menu():

    print("\n--- Menu ---")
    print("1. Greet User")
    print("2. Check Even or Odd")
    print("3. Exit")

def greet_user():

    print("Hello! Welcome to the program.")

def even_odd_checker_action():
 
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

def handle_menu_choice(choice):

    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        return True  # Signal to terminate the program loop
    else:
        print("Invalid choice. Please select a valid option.")
    return False  # Signal to continue the program loop

def get_integer_input():

    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):

    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

def main():

    while True:
        display_menu()
        try:
            choice = int(input("Select an option (1-3): "))
            if handle_menu_choice(choice):
                break  # Exit the loop if the user chooses to exit
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
