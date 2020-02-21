import string
import random

goal_string1 = "abc"
goal_string2 = "methinks it is like a weasel"
goal_string = """Here is a self check that really covers everything so far. You may have heard of the infinite
monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text, such as the com-
plete works of William Shakespeare. Well, suppose we replace a monkey with a Python func-
tion. How long do you think it would take for a Python function to generate just one sentence
of Shakespeare?"""


def get_goal(goal_string):
    display_count = 1
    attempts = 1
    closest_match = {'score': 0, 'string_list': []}
    goal_string = goal_string

    test_string_list = generate_initial_string(len(goal_string))

    while True:

        test_string_list = generate_next_wrong_char(test_string_list, goal_string)

        score = score_string("".join(test_string_list), goal_string)

        if score == 100:
            print_success("".join(test_string_list), attempts)
            break

        if closest_match['score'] < score:
            closest_match['score'] = score
            closest_match['string_list'] = test_string_list

        if display_count == 1000:
            print_progress(closest_match, attempts)
            display_count = 0

        display_count += 1
        attempts += 1


def generate_initial_string(length):
    generated_string = []
    for _ in range(length):
        generated_string.append(generate_random_char())
    return generated_string


def score_string(test_string, goal_string):
    return number_correct(test_string, goal_string) * (100 / len(test_string))


def generate_next_wrong_char(test_list, goal_string):
    wrong_char_location = find_next_wrong_char(test_list, goal_string)
    test_list[wrong_char_location] = generate_random_char()
    return test_list


def find_next_wrong_char(test_list, goal_string):
    pointer = 0
    while pointer < len(goal_string):
        if test_list[pointer] != goal_string[pointer]:
            return pointer
        pointer += 1


def generate_random_char():
    return random.choice(string.ascii_lowercase + string.ascii_uppercase + ".?!,-\n ")


def number_correct(test_string, goal_string):
    correct = 0
    for test, goal in zip(test_string, goal_string):
        if test == goal:
            correct += 1
    return correct


def print_progress(closest_match, attempts):
    print(f"Closest match ({int(closest_match['score'])}%) in {attempts:,} attempts:")
    print(f"{''.join(closest_match['string_list'])}\n")


def print_success(string, attempts):
    print(f"Found randomly generated match for: '{string}'")
    print(f"It took {attempts} attempts.")


if __name__ == "__main__":
    get_goal(goal_string)
