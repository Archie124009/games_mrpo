def run_game(name, game_func):
    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game_func()
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
