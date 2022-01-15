from datetime import *

while True:
    t = input("do you want to convert a date to a time stamp press n to do so")
    if t == "n":
        d = str(input("enter a date in this order(yyyy-mm-dd):"))
        user_date = datetime.strptime(d, "%Y-%m-%d")
        user_timestamp = datetime.timestamp(user_date)
        print("your time stamp is", user_timestamp)
    x = input("do you want to convert a time stampt to a date press y to do so")
    if x == "y":
        timestamp = int(input("enter a time stamp here:"))
        result = date.fromtimestamp(timestamp)
        print(result)
        exit = input("press q to exit if you wish")
        if exit == "q":
            break
    else: break
    
