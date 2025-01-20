import random
choices=["rock", "paper", "scissors"]
while True:
  with open("rock_paper_scissors.txt", "w") as file:
    user=input("Enter your choice: ").lower()
    comp=random.choice(choices)
    
    if(user==computer):
      result = "It's a tie."
    elif(user=="paper" and comp=="rock" or user =="rock" and comp=="scissors" or user=="scissors" and comp=="paper"):
      result = "User wins!"
    else:
      result = "Computer wins!"
    file.write(f"User choose {user} and computer choose {comp}. Result -> {result}")
    
    # comp_choice=input("Want to see computer choice?(y/n): ").lower()
    # if(comp_choice=="y"):
    #   print(f"{comp}")
    
    play=input("Play again?(y/n): ").lower()
    if(play=="y"):
      continue
    else:
      break

with open("rock_paper_scissors.txt", "r") as file:
  content = file.read()
  print(content)
