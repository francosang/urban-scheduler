import time

from datetime import datetime, timedelta

from urban_scheduler import api

ignore_classes = [
    73754911,
]

ignore_hours = [
    "09:30:00",
    "20:00:00"
]

ignore_weekdays = [
    0, # Monday
]

def search_classes(day):
    resp = api.get_classes(day)
    classes = resp["data"]["classes"]

    print_summary(classes)

    filteredClases = filter_classes(classes)
    return filteredClases

def print_class(c, include_booking=False):
    print(c["title"])
    print("\t", "Id:", c["id"])
    print("\t", "Start time:", c["startTime"])
    print("\t", "End time  :", c["endTime"])
    if include_booking:
        print("\t", "Booking   :", c["booking"])

def book(classes):
    print("")

    if not classes:
        print("-----------   NO BOOKINGS   -----------")
    else:
        print("-----------     BOOKING     -----------")
        for c in classes:
            print_class(c)
            print(c)
            # api.book_class(c["id"])

def print_summary(classes):
    for c in classes:
        print_class(c, include_booking=True)

def filter_classes(classes):
    def is_strenght(c):
        return c["title"] == "Strenght" or c["title"] == "Strength"
    
    def has_free_spots(c):
        return c["freeSpots"] > 0
    
    def is_not_booked(c):
        return c["booking"] is None
    
    def is_not_in_ignore_hours(c):
        return c["startTime"] not in ignore_hours
    
    def is_not_in_ignore_classes(c):
        return c["id"] not in ignore_classes

    def is_not_in_ignore_weekdays(c):
        print("--------------------------")
        start_date_time_utc = c["startDateTimeUTC"]

        print("start_date_time_utc:", start_date_time_utc)

        # Parse the date string into a datetime object
        dt = datetime.fromisoformat(start_date_time_utc)

        print("dt:", dt)

        print("dt.weekday():", dt.weekday())
        
        # Check if the day is Monday (weekday() returns 0 for Monday)
        return dt.weekday() not in ignore_weekdays
    
    filtered = filter(is_strenght, classes)
    filtered = filter(has_free_spots, filtered)
    filtered = filter(is_not_booked, filtered)
    filtered = filter(is_not_in_ignore_hours, filtered)
    filtered = filter(is_not_in_ignore_classes, filtered)
    filtered = filter(is_not_in_ignore_weekdays, filtered)

    return list(filtered)

def start():
    print("Getting classes...")
    current_date = datetime.now()
    for i in range(14):
        new_date = current_date + timedelta(days=i)
        day = new_date.strftime("%Y-%m-%d")

        print("*********** Day:", day, "***********")

        classes = search_classes(day)
        book(classes)

        print("")

        time.sleep(2)

     
