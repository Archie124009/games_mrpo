def greet_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def choose_game():
    print("Choose a game:")
    print("1. Least Common Multiple (LCM)")
    print("2. Guess the Missing Number in a Progression")
    choice = input("Choose the game you want to play (1 or 2): ")
    
    if choice == "1":
        return "lcm"
    elif choice == "2":
        return "progression"
    else:
        print("Invalid choice, try again.")
        return choose_game()
