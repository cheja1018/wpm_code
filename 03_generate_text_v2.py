# import libraries
from faker import Faker


# function to generate a random word
def generate_text():
    faker = Faker()
    random_word = faker.word()
    return random_word


# print 50 times
for x in range(50):
    text = generate_text()
    print(text)
