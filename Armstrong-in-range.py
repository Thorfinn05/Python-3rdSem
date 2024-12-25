beg=int(input("Enter beg: "))
end=int(input("Enter end: "))
for num in range(beg, end+1):
  temp=num
  a=0
  length=len(str(num))
  while num>0:
    r=num%10
    a=a+r**length
    num=num//10
  if(temp==a):
    print(temp, end=" ")

