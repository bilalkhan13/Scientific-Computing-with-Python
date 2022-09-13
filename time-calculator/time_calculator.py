def add_time(start_full_time, stop_full_time, day_of_week=None):
    PM = "PM"
    [initial_time, start_day_unit] = get_time(start_full_time)
    stop_minutes = get_minutes(stop_full_time)
    start_minutes = get_minutes(initial_time)

    if start_day_unit == PM:
        start_minutes += 12 * 60

    result_minutes = start_minutes + stop_minutes
    final_time_minutes = result_minutes % 60
    final_time_minutes = (f"{final_time_minutes:02d}") if final_time_minutes < 10 else final_time_minutes
    result_hours = int(result_minutes / 60)


    hours = result_hours % 24
    days = int(result_hours / 24)
    final_time_hours = hours % 12

    if int(hours / 12) == 0:
        final_time_unit = "AM"
    else:
        final_time_unit = PM

    if final_time_hours == 0:
        final_time_hours = 12

    time_stamp = str(final_time_hours) + ":" + str(final_time_minutes) + " " + final_time_unit

    if not day_of_week == None:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        position = 0

        while True:
            if day_of_week.lower() == days_of_week[position].lower():
                break

            position = position + 1

        newDay_of_week = days_of_week[((position + (days % 7)) % 7)]
        time_stamp += ", " + newDay_of_week

    if not days == 0:
        time_stamp += " (next day)" if days == 1 else " (" + str(days) + " days later)"

    return time_stamp

def get_time(time):
    return time.split()

def get_minutes(time):
    [hours, minutes] = time.split(":")
    return int(minutes) + (60 * int(hours))