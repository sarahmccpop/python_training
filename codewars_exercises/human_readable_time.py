# # https://www.codewars.com/kata/52685f7382004e774f0001f7/python

# my massive function
def make_readable(seconds):
    # Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
    hours = 0
    minutes = 0
    leftover_seconds = 0
    if seconds < 60:
        if seconds < 10:
            return_string = f"00:00:0{seconds}"
        else:
            return_string = f"00:00:{seconds}"
        return return_string
    elif seconds >= 60 and seconds < 3600:
        minutes = int(seconds / 60)
        leftover_seconds = int(seconds - (minutes * 60))
        if minutes >= 10 and leftover_seconds >= 10:
            return f"00:{minutes}:{leftover_seconds}"
        elif minutes >= 10 and leftover_seconds < 10:
            return f"00:{minutes}:0{leftover_seconds}"
        elif minutes < 10 and leftover_seconds >= 10:
            return f"00:0{minutes}:{leftover_seconds}"
        elif minutes < 10 and leftover_seconds < 10:
            return f"00:0{minutes}:0{leftover_seconds}"
    elif seconds >= 3600:
        hours = int(seconds / 3600)
        leftover_seconds = int(seconds - (hours * 3600))
        if leftover_seconds > 60:
            minutes = int(leftover_seconds / 60)
            leftover_seconds = int(leftover_seconds - (minutes * 60))
        if hours >= 10 and minutes >= 10 and leftover_seconds >= 10:
            return f"{hours}:{minutes}:{leftover_seconds}"
        elif hours >= 10 and minutes >= 10 and leftover_seconds < 10:
            return f"{hours}:{minutes}:0{leftover_seconds}"
        elif hours >= 10 and minutes < 10 and leftover_seconds >= 10:
            return f"{hours}:0{minutes}:{leftover_seconds}"
        elif hours < 10 and minutes >= 10 and leftover_seconds >= 10:
            return f"0{hours}:{minutes}:{leftover_seconds}"
        elif hours >= 10 and minutes < 10 and leftover_seconds < 10:
            return f"{hours}:0{minutes}:0{leftover_seconds}"
        elif hours < 10 and minutes >= 10 and leftover_seconds < 10:
            return f"0{hours}:{minutes}:0{leftover_seconds}"
        elif hours < 10 and minutes < 10 and leftover_seconds >= 10:
            return f"0{hours}:0{minutes}:{leftover_seconds}"
        elif hours < 10 and minutes < 10 and leftover_seconds < 10:
            return f"0{hours}:0{minutes}:0{leftover_seconds}"

    return "00:00:00"


# print("1 minute", make_readable(60))
# print("2 minute 19 seconds", make_readable(139))
# print("59 seconds", make_readable(59))
# print("7271", make_readable(7271))


# def make_readable(sec):
#     m, s = divmod(sec, 60)
#     h, m = divmod(m, 60)
#     print(m, s)
#     print("m", m)
#     print("h", h)
#     return f"{h:02d}:{m:02d}:{s:02d}"


print("60", make_readable(60))
