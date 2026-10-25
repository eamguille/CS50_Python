
def main():
    time = input("What time is it? ")
    time = time.strip()

    time_ = convert(time)

    if time_ >= 7 and time_ < 8:
        print("breakfast time")
    elif time_ >= 12 and time_ < 13:
        print("lunch time")
    elif time_ >= 18 and time_ < 19:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)

    if (hours < 0 or hours > 23) or (minutes < 0 or minutes > 59):
        return "Error: Enter a valid time!"

    return hours + (minutes / 60)


if __name__ == "__main__":
    main()