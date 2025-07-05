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

def rubbelkarten():
    max_attempts = 10
    attempts = 0
    correct_choices = 0

    # RANDOM NUMBERS
    first_random_number = random.randint(1, 30) - 1
    second_random_number = random.randint(1, 30) - 1
    third_random_number = random.randint(1, 30) - 1

    while len({first_random_number, second_random_number, third_random_number}) != 3:
        second_random_number = random.randint(1, 30) - 1
        third_random_number = random.randint(1, 30) - 1

    hashes = [['#' for _ in range(10)] for _ in range(3)]

    while correct_choices < 3 and attempts < max_attempts:
        try:
            choice = int(input("\nChoose a number to scratch (1-30): "))
            if 1 <= choice <= 30:
                choice -= 1

                if choice == first_random_number:
                    print("You guessed the first number!")
                    correct_choices += 1
                    hashes[0][choice] = '@'
                    first_random_number = -1
                elif choice == second_random_number:
                    print("You guessed the second number!")
                    correct_choices += 1
                    hashes[1][choice] = '@'
                    second_random_number = -1
                elif choice == third_random_number:
                    print("You guessed the third number!")
                    correct_choices += 1
                    hashes[2][choice] = '@'
                    third_random_number = -1
                else:
                    print(f"You chose number {choice + 1}, but it's not one of the drawn numbers.")

                print("\nCurrent hashes:")
                for line in hashes:
                    print(''.join(line))

            else:
                print("Invalid choice. Please choose a number between 1 and 30.")
        except ValueError:
            print("Please enter a valid number.")

        attempts += 1

    if correct_choices == 3:
        print("\nCongratulations, you guessed all the numbers! You won!")
    else:
        print(f"\nGame over! You've used all {max_attempts} attempts.")

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
            print("Exiting...")
            break
        result = switch(option)
        print(result)

# RUN THE PROGRAM
print('<---- Welcome to PyBet ---->')
print_menu()