# MENU
def print_menu():
    print('Choose an option:\n')

    test_list = ['Test 1', 'Test 2', 'Test 3']
    for x in range(len(test_list)):
        print(str(x + 1) + '. ' + test_list[x])

print('<---- Welcome to PyBet ---->')
print_menu()
