with open('prison-game.txt', 'w') as file:
  def freedprisoner(l):
    c=1
    if(l[0]==0):
      c=0
    else:
      for i in range(len(l)):
        if(l[i]==0):
          c+=1
          for j in range(len(l)):
            if(l[j]==0):
              l[j]=1
            else:
              l[j]=0
    file.write(f"Freedprisoners({l}) -> {c} \n")

  freedprisoner([1, 1, 0, 0, 0, 1, 0])
  freedprisoner([1, 1, 1])
  freedprisoner([0, 0, 0])
  freedprisoner([0, 1, 1, 1])
file.close()
