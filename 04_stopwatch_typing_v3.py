# import libraries
import time


# function to get time
def get_user_input():
    global user_input
    print("Type the following paragraph as fast as you can:")
    paragraph = "The quick brown fox jumps over the lazy dog."
    print(paragraph)

    start_time = time.time()
    user_input = input("Your input: ")
    end_time = time.time()
    return user_input, end_time - start_time


if __name__ == "__main__":
    user_input, time_taken = get_user_input()
    print(f"\nYou typed: {user_input}")
    print(f"Time taken: {time_taken:.2f} seconds")
