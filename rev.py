#Process 1
n=int(input("Enter n:"))
for i in range(len(str(n))):
  r=n%10
  print(r,end="") #end= restricts the printing output to print in a new line...generally used to add a string.
  n=n//10

#Process 2
n=int(input("\nEnter n:"))
rev=0
for i in range(len(str(n))):
  r=n%10
  rev=rev*10+r
  n=n//10  
print("The reversed number is:",rev)