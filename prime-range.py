def chkprime(n):
  c=0
  if(n>=1):
    for i in range(2, (n//2)+1):
      if(n%i==0):
        c+=1
        break
    if(c==0):
      return 1
    else:
      return 0

lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))
print("Prime numbers from",lower,"to",upper,"are:")
for i in range(lower, upper+1):
  if(chkprime(i)==1):
    print(i, end=" ")