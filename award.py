'''
Task 04

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

pseudo code:
purpose - determine the award and tell the user

get user minutes for each event store as ints >0 use try? not sure how to do this in a loop?
show a running total of event time
total the event times
print the total time
if any event less than 0 they clearly didnt do all events - this will also stop negs entered
if <=100 = provincial cols
elif >=101 and <=105 half provincial cols
elif >=106 and <=110 half provincial scroll
else (>110) = no award - use in else state

other comments that i should raise/find out about:
i dont understand why "message" is treated as a constant not a variable and 
i dont understand why it should be named in caps (pylint?)
and i dont understand the final missing newline (pylint?)

'''

#get times
swim_time = int(input("Please enter the time for your swimming segment (in minutes)..."))
print (f"Total time so far {swim_time} minutes")
cycle_time = int(input("Please enter the time for your cycling segment (in minutes)..."))
print (f"Total time so far {swim_time + cycle_time} minutes")
run_time = int(input("Please enter the time for your running segment (in minutes)..."))
print (f"Total time so far {swim_time + cycle_time + run_time} minutes")

event_total_time = swim_time + cycle_time + run_time

#display total time for event
print(f"Your total time for this event is {event_total_time} minutes")

#tests and message calc and display...
if (swim_time <1 or cycle_time <1 or run_time <1):
    message = ("But unfortunately you did not finish all events"
    " but well done for getting here - see you next year!")
elif event_total_time <= 100:
    message = "Amazing time you have earned the Provincial Colours award"
elif 101 <= event_total_time <=105:
    message = "Great effort and you have earned the Provincial Half Colours award"
elif 106 <= event_total_time <=110:
    message = "Good result and you have earned the Provincial Scroll award"
else:
    message = "you finished but didn't qualify for an award this time."

#output the award result
print()
print (f"Well done - {message}")
