# import libraries
from time import sleep

# count to ten
for i in range(1, 11):
    # counts to ten and remove the previous no.
    print(f"\rcounting to 10, {i}", end="")
    sleep(1)  # counting seconds properly

else:
    print(f"\r", end="")
    print("replace with this line")

