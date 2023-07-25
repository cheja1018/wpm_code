# user input
user_input = input("Enter something here: ")


# Count the number of words
def word_counter():
    word_count = len(user_input.split())
    return word_count


# Print the result
print("Number of words:", word_counter())
