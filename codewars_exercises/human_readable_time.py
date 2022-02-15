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

# this is number 1 answer revealed
# divmod - The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder.
# https://www.geeksforgeeks.org/divmod-python-application/#:~:text=The%20divmod()%20method%20in,of%20their%20quotient%20and%20remainder.&text=Explanation%3A%20The%20divmod()%20method,is%20treated%20as%20the%20denominator.
def make_readable_n1(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


largest_divider, remainder = divmod(90, 4)
print("expecting 22:", largest_divider)
print("Expecting 2:", remainder)

print("60", make_readable_n1(60))
