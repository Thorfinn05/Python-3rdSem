nt=int(input("Enter no. till: "))
nt=int(input("Enter no. till: "))
n1, n2 = 0, 1
count = 0
if nt == 1:
  print("Fiboacci series upto",nt,":",n1)
else:
  print("Fiboacci series upto",nt,":",end=' ')
  while(n1<20):
    print(n1, end=' ')
    print("-> Count: ",count)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
