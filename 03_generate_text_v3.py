# import library
from faker import Faker


# using a function print random words
def generate_text():
    faker = Faker()
    random_word = faker.word()
    return random_word


line_length = 0
words = []
max_line_length = 60

# print 50 random words with structure
for x in range(50):
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


