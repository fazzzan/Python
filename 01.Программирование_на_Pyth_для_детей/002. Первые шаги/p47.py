def convert_seconds_in_days(num):
    hours = 24 * num
    minutes = 60
    seconds = hours * minutes *60
    return seconds
    

total_sec = convert_seconds_in_days(1)
print(total_sec)
