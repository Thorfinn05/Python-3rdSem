n=int(input("Enetr n: "))
a=0
temp=n
for i in range (len(str(n))):
  r=n%10
  a=a+(r**(len(str(temp))))
  n=n//10
if(a==temp):
  print("Okay")
else:
  print("Not okay")