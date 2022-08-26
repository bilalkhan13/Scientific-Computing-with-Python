def add_time(start_time, stop_time, day_of_week=None):
    PM = "PM"
    [intial_time, start_day_unit] = get_time(start_time)
    [start_hours, start_minutes] = get_hours_minutes(intial_time)

    [stop_hours, stop_minutes] = get_hours_minutes(stop_time)

    stop_minutes = into_minutes(stop_minutes, stop_hours)

    if start_day_unit == PM:
        start_hours = start_hours + 12

    start_minutes = into_minutes(start_minutes, start_hours)
    total_minutes = start_minutes + stop_minutes

    final_minutes = total_minutes % 60
    total_hours = int(total_minutes / 60)

    if final_minutes < 10:
        final_minutes = "0" + str(final_minutes)
    else:
        final_minutes = str(final_minutes)

    hours = total_hours % 24
    days = int(total_hours / 24)

    final_hours = hours % 12

    if int(hours / 12) == 0:
        am_or_pm = "AM"

        if final_hours == 0:
            final_hours = 12
    else:
        am_or_pm = PM

        if final_hours == 0:
            final_hours = 12

    time_stamp = str(final_hours) + ":" + final_minutes + " " + am_or_pm

    if not day_of_week == None:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pos = 0

        while True:
            if day_of_week.lower() == days_of_week[pos].lower():
                break

            pos = pos + 1

        newDay_of_week = days_of_week[((pos + (days % 7)) % 7)]
        time_stamp += ", " + newDay_of_week

    if not days == 0:
        time_stamp += " (next day)" if days == 1 else " (" + str(days) + " days later)"

    return time_stamp


def get_time(get_time):
    [time, start_day_unit] = get_time.split()
    return time, start_day_unit


def get_hours_minutes(get_time):
    [hours, minutes] = get_time.split(":")
    return int(hours), int(minutes)


def into_minutes(minutes, hours):
    return int(int(minutes) + (60 * int(hours)))
