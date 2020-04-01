from functions import get_names, calculate_score, print_results

#read the file with elements, strip unnecessary pieces of strings, close the file
file = open("elements.txt", "r")
element_list = file.readlines()

for index in range(len(element_list)):
    element_list[index] = element_list[index].strip("\n").lower()

file.close()

#print the instructions for a user
print("Greetings! It is time to check your knowledge about ATOMIC ELEMENTS.")
print("Enter any 5 of the first 20 atomic elements from Period Table and I will give you a grade.")

user_input = input("Are you ready (y/n)?\n")
print("******************************************************************")

if user_input.lower() == "y" or user_input.lower() == "yes":
    # get user input collected in a list
    answer_list = get_names()

    # distribute correct and incorrect answers in 2 separate lists
    correct_answers = []
    incorrect_answers = []

    for answer in answer_list:
        if answer in element_list:
            correct_answers.append(answer)
        else:
            incorrect_answers.append(answer)

    # calculate points
    points = calculate_score(correct_answers)

    # print results
    print_results(points, correct_answers, incorrect_answers)
else:
    print("Sorry to see you go :(")








