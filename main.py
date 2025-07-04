# ROULETTE
def roulette():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen_number = None

    def number_loop_condition():
        nonlocal chosen_number
        try:
            user_input = int(input("Choose a number 1-10: "))
            if user_input in numbers:
                chosen_number = user_input
                return False
            else:
                print("Invalid number. Please choose a number between 1 and 10.")
                return True
        except ValueError:
            print("Please enter a valid number.")
            return True

    condition = True
    while condition:
        condition = number_loop_condition()

    return f"You chose the Roulette. Number: {chosen_number}"

# SLOTS
def slots():
    return "You chose the Slots."

# RUBBELKARTEN
def rubbelkarten():
    return "You chose the Rubberkarten."

# SWITCH
def switch(option):
    if option == "1":
        return roulette()
    elif option == "2":
        return slots()
    elif option == "3":
        return rubbelkarten()
    else:
        return "Invalid option."

# MENU
def print_menu():
    print('Choose an option:\n')

    test_list = ['Roulette', 'Slots', 'Rubbelkarten']
    for x in range(len(test_list)):
        print(f"{x + 1}. {test_list[x]}")

    option = input("\nEnter your choice: ")
    result = switch(option)
    print(result)

# RUN THE PROGRAM
print('<---- Welcome to PyBet ---->')
print_menu()