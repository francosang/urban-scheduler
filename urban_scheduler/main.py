import time

from datetime import datetime, timedelta

from urban_scheduler import api

ignore_classes = [
    73754911,
]

def search_classes(day):
    # 1. Get clases
    # 2. Filter for strenght classes
    # 3. Filter for classes that are not booked
    # 4. Filter for classes that have free spots
    # 5. Filter for classes that do not start at 20:00
    # 6. Book the class

    print("Day:", day)

    resp = api.get_classes(day)

    classes = resp["data"]["classes"]

    for c in classes:
        print(c["title"])
        print("\tId:", c["id"])
        print("\tStart time:", c["startTime"])
        print("\tEnd time  :", c["endDateTimeUTC"])
        
        if c["title"] == "Strenght" and c["freeSpots"] > 0 and c["booking"] is None and c["startTime"] != "20:00:00" and c["id"] not in ignore_classes:
            print("\t--> BOOKING <--")
            api.book_class(c["id"])

def start():
    print("Getting classes...")
    current_date = datetime.now()
    for i in range(14):
        new_date = current_date + timedelta(days=i)
        day = new_date.strftime("%Y-%m-%d")

        print("**************************")
        search_classes(day)
        time.sleep(2)

     
