import random
choices=["rock", "paper", "scissors"]
while True:
  with open("rock_paper_scissors.txt", "w") as file:
    user=input("Enter your choice: ").lower()

    rem_choice= [choice for choice in choices if choice != user]
    comp=random.choice(rem_choices)
    if(user=="paper" and comp=="rock" or user =="rock" and comp=="scissors" or user=="scissors" and comp=="paper"):
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
