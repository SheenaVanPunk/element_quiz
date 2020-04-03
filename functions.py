
def get_names():
    answer_list = []

    for index in range(5):
        answer = input("List any 5 of the first 20 elements: " + str(index + 1) + "# - ")
        while answer.lower() in answer_list or answer == "":
            print("An entry cannot be a duplicate or an empty string. Try again.")
            answer = input("Enter a unique element: " + str(index + 1) + "# - ")
        answer_list.append(answer.lower())

    return answer_list


def calculate_score(list):
    points = len(list) * 20
    return points


def print_results(points, correct, incorrect):
    print_banner("You've completed the quiz!")
    if points >= 80:
        print_separator("Well done! You seem to know elements well! Your score is " + str(points) + "%.")
    elif 20 < points < 80:
        print_separator("You might want to refresh your knowledge of elements. You score is " + str(points) + "%.")
    else:
        print("You should go back to school - your score is " + str(points) + "%.")

    if len(correct) > 0:
        string = ", ".join(correct)
        print_separator("Correct answers: " + string.title())
    else:
        print_separator("Correct answers: none :(")

    if len(incorrect) > 0:
        string = ", ".join(incorrect)
        print_separator("Incorrect answers: " + string.title())
    else:
        print_separator("Incorrect answers: none - :)")


def print_banner(sentence):
    line = "*" * len(sentence)
    print(line)
    print_separator(sentence)


def print_separator(sentence):
    line = "*" * len(sentence)
    print(sentence)
    print(line)
