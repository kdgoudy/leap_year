#Create variable to check the year
year = int(input("What year would you like to check?: "))

#Create if/else to see if year has a remainder of 0
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")
