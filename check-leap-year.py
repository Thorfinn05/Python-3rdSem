y=int(input("Enter year:"))

if(y%4==0 and y%100!=0 or y%400==0):
  print("Year",y,"is a leap year.")
else:
  print("Year",y,"is not a leap year.")