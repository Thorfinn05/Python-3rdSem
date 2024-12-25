n=int(input("Enter n: "))
temp=n
s=0
#150->150//10=15,0    len(str(n))
while(n>0):
# for i in range (len(str(n))):
  r=n%10
  s=r+10*s
  n=n//10
if(s==temp):
  print("Okay")
else:
  print("not okay")



