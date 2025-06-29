# MENU
def print_menu():
    print('Choose an option:\n')

    test_list = ['Roulette']
    for x in range(len(test_list)):
        print(str(x + 1) + '. ' + test_list[x])

print('<---- Welcome to PyBet ---->')
print_menu()
