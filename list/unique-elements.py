l1=eval(input("Enter list: "))
l2={}
for i in l1:
  if i not in l2:
    l2[i]=1
  else:
    l2[i]+=1
print("Unique Values: ")
for i in l2:
  if(l2[i]==1):
    print(i, end=' ')
