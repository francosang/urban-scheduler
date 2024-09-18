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
            api.book_class(c["id"])

def print_summary(classes):
    for c in classes:
        print_class(c, include_booking=True)

def filter_classes(classes):
    # only Strenght classes
    filtered = filter(lambda c: c["title"] == "Strenght", classes)
    # only classes without booking
    filtered = filter(lambda c: c["booking"] is None, filtered)
    # only classes not in ignore_hours
    filtered = filter(lambda c: c["startTime"] not in ignore_hours, filtered)
    #  only classes not in ignore_classes
    filtered = filter(lambda c: c["id"] not in ignore_classes, filtered)
    return list(filtered)

def start():
    print("Getting classes...")
    current_date = datetime.now()
    for i in range(2):
        new_date = current_date + timedelta(days=i)
        day = new_date.strftime("%Y-%m-%d")

        print("*********** Day:", day, "***********")

        classes = search_classes(day)
        book(classes)

        print("")

        time.sleep(2)

     
