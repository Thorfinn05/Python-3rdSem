l1=eval(input("Enter list: "))
l2=[]
for i in l1:
  if i not in l2:
    l2.append(i)
print(l2)
