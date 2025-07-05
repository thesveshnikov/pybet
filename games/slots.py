import random

def slots():
    characters = ['7', '@', '$']
    first = random.choice(characters)
    second = random.choice(characters)
    third = random.choice(characters)

    print(f"{first} {second} {third}")

    if first == second and first == third:
        return "YOU WIN!"
    else:
        return "YOU LOST!"
