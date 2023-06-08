# print the following options
print("Select how long you would like to type for?\n"
      "The following times include:\n"
      "1. 10s\n"
      "2. 15s\n"
      "3. 30s\n"
      "4. 60s")

# ask users for which one they like
selection = int(input("Enter your choice (1-4): "))

# when this is selected the following durations are stored
if selection == 1:
    duration = 10
elif selection == 2:
    duration = 15
elif selection == 3:
    duration = 30
else:
    duration = 60

# print their chosen duration
print(f"You have selected {duration}s.")
