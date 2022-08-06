
def add_time(startTime, endTime, dayOfWeek=None):

    # Start Time
    startTime = startTime.split(" ")
    am_pm = startTime[1]
    startTime = startTime[0].split(":")
    startHours = int(startTime[0])
    startMinutes = int(startTime[1])

    # End Time
    endTime = endTime.split(":")
    endHours = int(endTime[0])
    endMinutes = int(endTime[1])

    endMinutes = endMinutes + (60 * endHours)

    if am_pm == "PM":
        startHours = int(startHours) + 12

    startMinutes = startMinutes + (60 * startHours)
    totalMinutes = startMinutes + endMinutes

    # Minutes Calculation
    finalMinutes = totalMinutes % 60
    finalHours = int(totalMinutes / 60)

    if len(str(finalMinutes)) == 1:
        finalMinutes = "0" + str(finalMinutes)
    elif len(str(finalMinutes)) == 2:
        finalMinutes = str(finalMinutes)

    # Calculation Days
    hours = finalHours % 24
    days = int(finalHours / 24)

    # Am & PM Calculation
    hoursFinal = hours % 12

    if int(hours / 12) == 0:
        finalAmPm = "AM"
        if hoursFinal == 0:
            hoursFinal = 12
    else:
        finalAmPm = "PM"
        if hoursFinal == 0:
            hoursFinal = 12

    new_time = str(hoursFinal) + ":" + finalMinutes + " " + finalAmPm

    # Days Calculation
    if not dayOfWeek == None:
        daysOfWeek = ['Monday', 'Tuesday', 'Wednesday',
                      'Thursday', 'Friday', 'Saturday', 'Sunday']
        pos = 0
        while True:
            if dayOfWeek.lower() == daysOfWeek[pos].lower():
                break
            pos = pos + 1
        newDayOfWeek = daysOfWeek[((pos + (days % 7)) % 7)]
        new_time = new_time + ", " + newDayOfWeek

    # Output
    if days == 1:
        new_time = new_time + " (next day)"
    elif days > 1:
        days = str(days)
        new_time = new_time + " (" + days + " days later)"

    return new_time
