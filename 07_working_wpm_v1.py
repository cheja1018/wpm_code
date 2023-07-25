# libraries
from faker import Faker
import time


# function goes here
# asking if users had played before
def yes_no(question):
    valid = False
    while not valid:
        # Ask the user of they have played before
        response = input(question).lower()

        # If they say yes, output program continues
        if response == "yes" or response == "y":
            print()
            response = "continue program"
            # if they say yes, return yes
            return response

        # If they say no, output 'Show instructions
        elif response == "no" or response == "n":
            print()
            response = "show instructions"
            # if they say no, return no
            return response

        # If other, print error
        elif response == "quit":
            response = "to quit"
            # if they say no, return no
            return response
        else:
            print("Please answer yes / no")


# show instruction if needed
def instructions():
    # title
    print("HOW THIS WPM CALCULATOR WORKS")
    print()
    # the rules
    print("Hey there!\nThe objection is to type as quickly and accurately as you can in the given time.\n"
          "Firstly, you will be provided the options of 10s, 15s, 30s and 60s.\n"
          "The stopwatch will start as soon as you press enter and you'll have to type the \n"
          "randomly generated paragraph as fast as possible.\n"
          "The stopwatch would automatically stop and will calculate your WPM for you!")
    return ""


# ask how long users would like to play for
def ask_duration():
    global amount_of_text
    print("Select how long you would like to type for?\n"
          "\n"
          "The following times include:\n"
          "1. 10s\n"
          "2. 15s\n"
          "3. 30s\n"
          "4. 60s")

    while True:
        try:
            selection = int(input("Enter your choice (1-4): "))
            print()
            if selection < 1 or selection > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

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


# generate random words
def generate_text():
    faker = Faker()
    random_word = faker.word()
    return random_word


# generate text according to the selected time
def generate_random_words(amount_of_text):
    line_length = 0
    words = []
    max_line_length = 80

    for _ in range(amount_of_text):
        text = generate_text()
        word_length = len(text)

        if line_length + word_length <= max_line_length:
            words.append(text)
            line_length += word_length + 1
        else:
            print(" ".join(words))
            words = [text]
            line_length = word_length

    if words:
        print(" ".join(words))


# calculate the wpm taking the time of how long users take to type
def calculate_wpm(text, elapsed_time):
    words = text.split()
    word_count = len(words)
    minutes = elapsed_time / 60
    wpm = word_count / minutes
    return wpm


# display everything
def main():
    input("Press Enter to start the timer...")

    start_time = time.time()

    # Simulating user input. Replace this with your own logic for obtaining user input.
    user_input = input("Type the passage:\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

    wpm = calculate_wpm(user_input, elapsed_time)
    print("Calculating WPM...")
    time.sleep(1)
    print("Your WPM: {:.2f}".format(wpm))


# main routine goes here...
# welcoming statement
print("Welcome to my WPM calculator!")
time.sleep(0.5)  # pausing

# user input to ask if they had played before
played_before = yes_no("Have you calculated your WPM with this game before? (yes or no)  ")

# ask if they need a reminder of the instructions
if played_before == "continue program":
    played_before = yes_no("Do you remember how it works?   ")

# when users need instructions display them
if played_before == "show instructions":
    instructions()

# print out the functions
amount_of_text = ask_duration()

generate_random_words(amount_of_text)
print()  # break

if __name__ == '__main__':
    main()
