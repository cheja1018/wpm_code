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
            # make sure the number chosen is while range
            if selection < 1 or selection > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        # Tell the user it isn't a number in range
        except ValueError:
            print("Invalid input. Please enter a number.")

    # the number corresponds to a duration
    if selection == 1:
        duration = 10
    elif selection == 2:
        duration = 15
    elif selection == 3:
        duration = 30
    else:
        duration = 60

    # prints their chosen duration
    print(f"You have selected {duration}s.")
    return duration


# print the function
selected_duration = ask_duration()
