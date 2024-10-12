import random
import math

def find_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = math.lcm(lcm, num)
    return lcm

def lcm_game():
    numbers = random.sample(range(1, 101), 3)
    question = f"{numbers[0]} {numbers[1]} {numbers[2]}"
    correct_answer = str(find_lcm(numbers))
    return question, correct_answer
