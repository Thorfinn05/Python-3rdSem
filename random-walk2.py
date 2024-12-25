import random
x=0
y=0
steps=0
while(abs(x)<8 and abs(y)<8):
  move=random.randint(1,4)
  if(move==0):
    x+=1
    steps+=1
    print("Step:",steps,"Move right",x)
  elif(move==1):
    x-=1
    steps+=1
    print("Step:",steps,"Move left",x)
  elif(move==2):
    y+=1
    steps+=1
    print("Step:",steps,"Move up",y)
  elif(move==3):
    y-=1
    steps+=1
    print("Step:",steps,"Move down",y)
  else:
    print("Invalid step!")
print("Number of steps taken: ",steps)