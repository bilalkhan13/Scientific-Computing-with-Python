
def add_time(startTime, stopTime, dayOfWeek=None):
    # Start Time
    [startTime, start_am_pm] = startTime.split()
    [startHours, startMinutes] = startTime.split(':')

    # End Time
    [stopHours, stopMinutes] = stopTime.split(":")

    stopMinutes = int(stopMinutes) + (60 * int(stopHours))

    if start_am_pm == "PM":
        startHours = int(startHours) + 12

    startMinutes = int(startMinutes) + (60 * int(startHours))
    totalMinutes = startMinutes + stopMinutes

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
    finalHours = hours % 12

    if int(hours / 12) == 0:
        finalAmPm = "AM"
        if finalHours == 0:
            finalHours = 12
    else:
        finalAmPm = "PM"
        if finalHours == 0:
            finalHours = 12

    new_time = str(finalHours) + ":" + finalMinutes + " " + finalAmPm

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