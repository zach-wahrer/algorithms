import string
import random

goal_string = "abcdef"
goal_string1 = "methinks it is like a weasel"


def generate_string(length):
    possibles = string.ascii_lowercase + " "
    generated_string = ""
    for _ in range(length):
        generated_string += random.choice(possibles)
    return generated_string


def score_string(test_string, goal_string):
    return number_correct(test_string, goal_string) * (100 / len(test_string))


def get_goal(goal_string):
    display_count = 1
    attempts = 1
    closest_match = {'score': 0, 'string': ""}
    goal_string = goal_string.lower()

    while True:
        test_string = generate_string(len(goal_string))
        score = score_string(test_string, goal_string)

        if score == 100:
            print_success(test_string, attempts)
            break

        if closest_match['score'] < score:
            closest_match['score'] = score
            closest_match['string'] = test_string

        if display_count == 1000:
            print_progress(closest_match, attempts)
            display_count = 0

        display_count += 1
        attempts += 1


def number_correct(test_string, goal_string):
    correct = 0
    for test, goal in zip(test_string, goal_string):
        if test == goal:
            correct += 1
    return correct


def print_progress(closest_match, attempts):
    print(f"Closest match ({int(closest_match['score'])}%) in {attempts:,} attempts:")
    print(f"{closest_match['string']}\n")


def print_success(string, attempts):
    print(f"Found randomly generated match for: '{string}'")
    print(f"It took {attempts} attempts.")


if __name__ == "__main__":
    get_goal(goal_string)
