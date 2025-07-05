import random

def rubbelkarten():
    max_attempts = 10
    attempts = 0
    correct_choices = 0

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
