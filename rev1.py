n=int(input("Enter n: "))
print("Original number: ",n)
a=0
while n>0:
  r=n%10
  a=r+10*a
  n=n//10
print("Reversed number: ",a)