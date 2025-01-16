import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        return ValueError("invalid format")
    
    starthour, startminute, startampm, endhour, endminute, endampm = match.groups()

    startminute = int(startminute) if startminute else 0
    endminute = int(endminute) if endminute else 0
    starthour = int(starthour)
    endhour = int(endhour)

    if not (0 <= starthour <= 12) or not (0 <= startminute <=59):
        return ValueError("invalid start time")
    if not (0 <= endhour <= 12) or not (0 <= endminute <=59):
        return ValueError("invalid end time")   
    
    if startampm == "PM" and starthour != 12:
        starthour += 12
    elif startampm == "AM" and starthour == 12:
        starthour = 0

    if endampm == "PM" and endhour != 12:
        endhour += 12
    elif endampm == "AM" and endhour == 12:
        endhour = 0

    return f"{starthour:02}:{startminute:02} to {endhour:02}:{endminute:02}"



if __name__ == "__main__":
    main()