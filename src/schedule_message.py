import time
import calendar


# Current Time
curr = time.time()

# Print Starting Point Eloch Time in Seconds
print(curr)

# Tuple of Current Time
print(time.gmtime(curr))


# Binding new Module Object
t = time
print(t.time())
lol = "lol"
print(t.strftime("%b %d, the day is %A"))

#help(calendar)
print(calendar.monthcalendar(2026, 1))
print(calendar.prmonth(2026,1,11,1))

TODAY = int(time.strftime("%d"))

def printCurrentTime():
    day = (t.strftime("%d"))
    print(day)
    print(t.sleep(5))
    print(t.strftime(f"%b {day}, %Y %H:%M:%S"))

printCurrentTime()

# Visualizing Printing time using Formatting
def printAll():
    printTime()
    printYear()
    printMonth()
    printDay()

def printTime():
    print(t.strftime("The hour is: %H"))
    print(t.strftime("The minute is: %M"))
    print(t.strftime("The second is: %S"))
    print(t.strftime("The timezone is: %z"))

def printYear():
    print(t.strftime("This is the year: %Y"))

def printMonth():
    print(t.strftime("This prints the month's name abbreviated: %b "))
    print(t.strftime("This prints the month as a decimal number: %m" ))

def printDay():
    print(t.strftime("This is the abbreviated weekday name: %a"))
    print(t.strftime("This is the full weekday name: %A"))
    print(t.strftime("This prints the day of the month as a decimal number: %d"))
