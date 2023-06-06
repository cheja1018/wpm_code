# importing time in order to display text not all at the same time
import time

print("Welcome to my WPM calculator!")
time.sleep(0.5)


# function goes here
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


# instructions in a function, basic rules
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


# main routine goes here...
played_before = yes_no("Have you calculated your WPM with this game before? (yes or no)  ")

# ask if they need a reminder of the instructions
if played_before == "continue program":
    played_before = yes_no("Do you remember how it works?   ")

# when users need instructions display them
if played_before == "show instructions":
    instructions()
