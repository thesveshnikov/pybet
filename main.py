# ROULETTE
def roulette():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return f"You chose the Roulette. Number test: {numbers[0]}"

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