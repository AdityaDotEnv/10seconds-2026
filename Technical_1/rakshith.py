def next_day(day_num):
    week = {
        1: "Monday", 
        2: "Tuesday", 
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    next_day_num = (day_num % 7) + 1
    
    return week[next_day_num]

print(next_day(7))