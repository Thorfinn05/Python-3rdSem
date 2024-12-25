#Without using function
n=int(input("Enter no.:"))
if(n%2==0):
  print("Number is even.")
else:
  print("Number is odd.")

#Using Function
def even(n):
    if n%2==0:
        return True
    return False
num=even(7)
print(num)
