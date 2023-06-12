# import library
from faker import Faker


# ask how long they would like to type for
def ask_duration():
    print("Select how long you would like to type for?\n"
          "\n"
          "The following times include:\n"
          "1. 10s\n"
          "2. 15s\n"
          "3. 30s\n"
          "4. 60s")

    while True:
        try:
            # ask the question
            selection = int(input("Enter your choice (1-4): "))
            print()
            # make sure the number chosen is while range
            if selection < 1 or selection > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        # Tell the user it isn't a number in range
        except ValueError:
            print("Invalid input. Please enter a number.")

    # the number corresponds to a duration
    # adding a number for amount of text displayed
    if selection == 1:
        duration = 10
        amount_of_text = 20
    elif selection == 2:
        duration = 15
        amount_of_text = 30
    elif selection == 3:
        duration = 30
        amount_of_text = 50
    else:
        duration = 60
        amount_of_text = 100

    print(f"You have selected {duration}s.")
    print()
    return amount_of_text


# print the function
def generate_text():
    faker = Faker()
    random_word = faker.word()
    return random_word


line_length = 0
words = []
max_line_length = 80

# print amount of words when asked
for x in range(ask_duration()):
    text = generate_text()  # generate a random word
    word_length = len(text)  # get the word length using len

    if line_length + word_length <= max_line_length:
        # if words could fit in the line, fit it in
        words.append(text)
        line_length += word_length + 1  # add space
    else:
        # if the line exceeds 80 characters, start a new line
        print(" ".join(words))  # joining the words in a list and adding a space in between
        words = [text]
        line_length = word_length  # make sure line_length starts back to 0
