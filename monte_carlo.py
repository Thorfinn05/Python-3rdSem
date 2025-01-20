import random
trials = int(input("Enter no. of trials: "))
hits=0
for i in range(trials):
  x=2*random.random() - 1
  y=2*random.random() - 1
  if(x**2 + y**2) <=1:
    hits+=1
pi = 4*(hits/trials)
print(f"Value of pi is: {pi}")
