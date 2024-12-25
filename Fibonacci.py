range=int(input("Enter range: "))
n1, n2 = 0, 1
count=0
if(range==1):
  print("Fibonacci sequence upto",range,":",n1)
else:
  while count<range:
    print(n1, end=" ")
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1