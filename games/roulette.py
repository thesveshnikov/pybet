import random

def roulette():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen_number = None
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
