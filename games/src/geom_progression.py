import random

def progression_game():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(10)]
    missing_index = random.randint(0, len(progression) - 1)
    missing_value = progression[missing_index]
    progression[missing_index] = ".."
    
    question = ' '.join(map(str, progression))
    correct_answer = str(missing_value)
    return question, correct_answer
