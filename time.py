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
# Checking speed of execution for a simple loop 
start_time = t.time()
for i in range(1000):
    print(i, end=' ')
end_time = t.time()
for_time=execution_time = end_time - start_time
print("\nExecution time for the loop:", for_time, "seconds")
start_time = t.time()
i=0
while i < 1000:
    print(i, end=' ')
    i += 1

end_time = t.time()
while_time=execution_time = end_time - start_time
print("\nExecution time while the loop:", while_time, "seconds")
#Camparing the both the loops
if for_time < while_time:
    print("For loop is faster than while loop.")
elif for_time > while_time:
    print("While loop is faster than for loop.")
else:
    print("Both loops have the same execution time.")


local=t.asctime(t.localtime(t.time()))
print("Local time:", local)