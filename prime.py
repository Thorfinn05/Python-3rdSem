n=int(input("enter n:"))
c=0
if(n>1):
  for i in range(2,(n//2)+1):
    if(n%i==0):
      c+=1
      break
  if(c==0):
    print("Number is prime.")
  else:
    print("Number is nkt prime.")
else:
  print("Number is not prime.")