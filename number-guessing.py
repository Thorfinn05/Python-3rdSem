import random
lr=int(input("Enter lower range: "))
ur=int(input("Enter upper range: "))
comp=random.randint(lr,ur)
c=0
for i in range(3):
  user=int(input("Guess a number: "))
  if(user==comp):
    print("Correct Guess!")
    break
  else:
    print("Wrong guess!")
    c+=1
if(c==3):
  print(f"All chances are over! Computer has chosen {comp}")
