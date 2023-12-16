def get_input(event_name):
    while True:
        try:
            time = int(input(f"Please enter the time for your {event_name} segment (in minutes)..."))
            if time > 0:
                return time
            else:
                print("The time must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get times for each segment
swim_time = get_input("swimming")
print(f"Total time so far {swim_time} minutes")
cycle_time = get_input("cycling")
print(f"Total time so far {swim_time + cycle_time} minutes")
run_time = get_input("running")
print(f"Total time so far {swim_time + cycle_time + run_time} minutes")

event_total_time = swim_time + cycle_time + run_time

# Display total time for event
print(f"Your total time for this event is {event_total_time} minutes")

# Tests and message calculation...
if event_total_time <= 100:
    message = "Amazing time you have earned the Provincial Colours award"
elif 101 <= event_total_time <= 105:
    message = "Great effort and you have earned the Provincial Half Colours award"
elif 106 <= event_total_time <= 110:
    message = "Good result and you have earned the Half Provincial Scroll award"
else:
    message = "you finished but didn't qualify for an award this time."

print()
print(f"Well done - {message}")
print()
