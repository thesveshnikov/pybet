import random

# ROULETTE
def roulette():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen_number = None

    # DRAW A NUMBER
    random_number = random.randint(1, 10)

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

    if random_number == chosen_number:
        return "YOU WIN!"
    else:
        return "YOU LOST!"

# SLOTS
def slots():
    characters = ['7', '@', '$']

    # SELECT CHARACTERS
    first = random.choice(characters)
    second = random.choice(characters)
    third = random.choice(characters)

    print(f"{first} {second} {third}")

    if first == second and first == third:
        return "YOU WIN!"
    else:
        return "YOU LOST!"


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
    while True:
        print('\nChoose an option:')
        test_list = ['Roulette', 'Slots', 'Rubbelkarten']
        for x in range(len(test_list)):
            print(f"{x + 1}. {test_list[x]}")
        print("0. Exit")

        option = input("\nEnter your choice: ")
        if option == "0":
            print("Goodbye!")
            break
        result = switch(option)
        print(result)

# Run the menu
print_menu()

# RUN THE PROGRAM
print('<---- Welcome to PyBet ---->')
print_menu()