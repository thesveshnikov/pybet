from games.roulette import roulette
from games.slots import slots
from games.rubbelkarten import rubbelkarten

def switch(option):
    if option == "1":
        return roulette()
    elif option == "2":
        return slots()
    elif option == "3":
        return rubbelkarten()
    else:
        return "Invalid option."

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
