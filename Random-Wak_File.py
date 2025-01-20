import random
x=0
y=0
steps=0
with open("random_walk.txt", "w") as a file:
  while(abs(x)<10 and abs(y)<10):
    move=random.randint(1,4)
    if (move==1):
      print("Right")
      x+=1
      steps+=1
    elif (move==2):
      print("Left")
      x-=1
      steps+=1
    elif (move==3):
      print("Up")
      y+=1
      steps+=1
    elif (move==4):
      print("Down")
      y-=1
      steps+=1
    # else:
    #   print("Invalid step!")
    file.write(f"Step {steps}: {move}\n")
  file.write(f"Total no. of steps taken {steps}.")

# Reading the random_walk.txt file and displaying its contents
with open("random_walk.txt", "r") as file:
    content = file.read()
    print(content)
