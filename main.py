# SWITCH
def switch(option):
    if option == "1":
        return "You chose the Roulette."
    elif option == "2":
        return "You chose the Test."
    else:
        return "Invalid option."

# MENU
def print_menu():
    print('Choose an option:\n')

    test_list = ['Roulette', 'Test']
    for x in range(len(test_list)):
        print(f"{x + 1}. {test_list[x]}")

    option = input("\nEnter your choice: ")
    result = switch(option)
    print(result)

# RUN THE PROGRAM
print('<---- Welcome to PyBet ---->')
print_menu()