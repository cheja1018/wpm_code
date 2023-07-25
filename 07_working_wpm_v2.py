# libraries
from faker import Faker
import time
from time import sleep


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
    sleep(1)
    print()
    # the rules
    print("Hey there!")
    sleep(0.5)
    print("The objection is to type as quickly as you can with the given words.\n"
          "Firstly, you will be provided the options of 10, 20, 30 or 5o words.\n"
          "The stopwatch will start as soon as you press enter and you'll have to type the \n"
          "randomly generated paragraph as fast as possible.\n"
          "The stopwatch would automatically stop and will calculate your WPM for you!\n"
          "TAKE IN CONSIDERATION THIS DOES NOT CALCULATE ACCURACY")
    return ""


# ask for the amount of text they would like to type
def ask_text_amount():
    global amount_of_text
    print("Select how many words do you want to type?\n"
          "\n"
          "The following amount of words include:\n"
          "1. 10\n"
          "2. 20\n"
          "3. 30\n"
          "4. 50")

    while True:
        try:
            # user input for selection
            selection = int(input("Enter your choice (1-4): "))
            print()
            # more than 4 less than 1 response
            if selection < 1 or selection > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        # when text is entered instead of an integer
        except ValueError:
            print("Invalid input. Please enter a number.")

    # corresponds to the selection of words
    if selection == 1:
        amount_of_text = 10
    elif selection == 2:
        amount_of_text = 20
    elif selection == 3:
        amount_of_text = 30
    else:
        amount_of_text = 50

    print(f"You have selected {amount_of_text} words.")
    print()
    return amount_of_text


# generate random words
def generate_text():
    # using faker create 'fake' text
    faker = Faker()
    random_word = faker.word()
    return random_word


# print generated words to desired amount
def generate_random_words(amount_of_text):
    # so it doesn't exceed a certain length
    line_length = 0
    words = []
    max_line_length = 80

    # amount of text chosen previously
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


# calculate the words per minute
def calculate_wpm(text, elapsed_time):
    # splitting the words in the user input
    words = text.split()
    # using len to count the number of words
    word_count = len(words)
    # dividing by 60 to get wom
    minutes = elapsed_time / 60
    wpm = word_count / minutes
    return wpm


# putting it together and display wpm
def main():
    # starting when users are ready
    input("Press Enter to start the timer...")

    # begin timer
    start_time = time.time()
    # Simulating user input. Replace this with your own logic for obtaining user input.
    user_input = input("Type the passage:\n")
    # end timer
    end_time = time.time()
    # calculate wpm
    elapsed_time = end_time - start_time

    # displaying it
    wpm = calculate_wpm(user_input, elapsed_time)
    print("Calculating WPM...")
    time.sleep(1)
    print("Your WPM: {:.2f}".format(wpm))


# main routine goes here...
# welcoming statement
print("Welcome to my WPM calculator!")
time.sleep(0.5)  # wait 0.5 secs

# user input to ask if they had played before
played_before = yes_no("Have you calculated your WPM with this game before? (yes or no)  ")

# ask if they need a reminder of the instructions
if played_before == "continue program":
    played_before = yes_no("Do you remember how it works?   ")

# when users need instructions display them
if played_before == "show instructions":
    instructions()
    print()

sleep(3)  # wait 3 secs

# print out the functions
amount_of_text = ask_text_amount()
# Generate random words
generate_random_words(amount_of_text)
print()

if __name__ == '__main__':
    main()
