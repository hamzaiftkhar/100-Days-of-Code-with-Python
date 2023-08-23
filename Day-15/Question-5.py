# greeting Program

import datetime

time = datetime.datetime.now()
print(time)

if time.hour > 4 and time.hour < 12:
    print("Good Morning")
elif time.hour >= 12 and time.hour < 16:
    print("Good Afternoon")
elif time.hour >= 16 and time.hour < 21:
    print("Good Evening")
else:
    print("Good Night")

