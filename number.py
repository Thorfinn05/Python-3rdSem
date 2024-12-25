import random
a=int(input("Enter lr: "))
b=int(input("Enter ur: "))
guess=random.randint(a,b)
print("Computer: ",guess)
while True:
  try:
    u=int(input("Enter some: "))
    if(u==guess):
      print("Congo")
      break
    elif(u<guess):
      print("Too low")
    elif(u>guess):
      print("Too high")
  except:
    print('Invalid')
    

