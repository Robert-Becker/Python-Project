"""
Original Code Written By Robert Becker
Created on July 19, 2019
Last Modified on July 19, 2019
Program was designed to calculate steps per month during a normal year. (365 Days)
Project7 Part2
"""
with open("steps.txt") as f:
    variable = []
    for line in f:
        items = line.split()
        steps = int(items[0])
        variable.append(steps)

january = round(sum(variable[0:31])/len(variable[0:31]), 1)
february = round(sum(variable[31:59])/len(variable[31:59]), 1)
march = round(sum(variable[59:90])/len(variable[59:90]), 1)
april = round(sum(variable[90:120])/len(variable[90:120]), 1)
may = round(sum(variable[120:151])/len(variable[120:151]), 1)
june = round(sum(variable[151:181])/len(variable[151:181]), 1)
july = round(sum(variable[181:212])/len(variable[181:212]), 1)
august = round(sum(variable[212:243])/len(variable[212:243]), 1)
september = round(sum(variable[243:273])/len(variable[243:273]), 1)
october = round(sum(variable[273:304])/len(variable[273:304]), 1)
november = round(sum(variable[304:334])/len(variable[304:334]), 1)
december = round(sum(variable[334:365])/len(variable[334:365]), 1)

print(january, february, march, april, may, june, july, august, september, october, november, december)
stepsPerMonth = [january, february, march, april, may, june, july, august, september, october, november, december]
for month in stepsPerMonth:
    print("Your average monthly steps were " + str(month) + " steps.")

