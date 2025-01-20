import random
list=[random.randint(1,20) for i in range(10)]
print(list)
c=3 #int(input("Enter nth: "))
list2=[]
i=0
while i < len(list):
  list2.append(list[i:i+c])
  i=i+c
print(list2)
