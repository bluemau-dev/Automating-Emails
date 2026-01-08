import time

# Current Time
curr = time.time()

# Print Starting Point Eloch Time in Seconds
print(curr)

# Tuple of Current Time
print(time.gmtime(curr))


# Binding new Module Object
t = time
print(t.time())
