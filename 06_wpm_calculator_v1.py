import time


def calculate_wpm(text, elapsed_time):
    words = text.split()
    word_count = len(words)
    minutes = elapsed_time / 60
    wpm = word_count / minutes
    return wpm


def main():
    input("Press Enter to start the timer...")

    start_time = time.time()

    # Simulating user input
    user_input = input("Type the passage:\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

    wpm = calculate_wpm(user_input, elapsed_time)
    print("Calculating WPM...")
    time.sleep(1)
    print("Your WPM: {:.2f}".format(wpm))


if __name__ == '__main__':
    main()
