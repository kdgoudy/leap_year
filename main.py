#create variable to provide input
year = int(input("Enter a year: "))

#use if/elif statement to check if year is leap year or not 
if year % 4 == 0:
  print("Leap year")
elif year % 100 == 0:
  print("Leap year")
elif year % 400 == 0:
  print("Leap year")
else:
  print("Not a leap year")
