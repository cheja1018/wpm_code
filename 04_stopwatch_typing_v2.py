# import libraries
import time

# begin to start timing
start_time = time.time()
user_input = input("timing how long you enter things!   ")
# end the timer
end_time = time.time()

# calculating how much time it took
total_time = end_time - start_time

# printing results
print(user_input)
print(total_time)
