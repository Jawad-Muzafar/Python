import time as t
time=t.localtime()
print("Current time is:", time)## Print the current time in a structured format
# Checking if the current time is in the morning, afternoon, or evening
if time.tm_hour < 12:
    print("Good morning!")
elif 12 <= time.tm_hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
# Calculating the number of seconds since the epoch (January 1, 1970)
epoch_seconds = t.time()
print("Seconds since the epoch:", epoch_seconds)
# Formatting the current time in a more readable format
formatted_time = t.strftime("%Y-%m-%d %H:%M:%S", time)
print("Formatted current time:", formatted_time)