import  random
choices=["rock", "paper", "scissors"]
while True:
  user=input("Enter your choice: ").lower()
  if user not in choices:
    print('Invalid choice')
    continue
  computer=random.choice(choices)

  if(computer==user):
    print("It's tie")
  elif(user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
    print("User win")
  else:
    print("User lose")
  comp_choice=input("Want to see system's choice(y/n): ").lower()
  if(comp_choice=="y"):
    print(f"{computer}")

  play=input("Play again?(y/n): ").lower()
  if(play!="y"):
    break