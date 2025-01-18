num = int(input("Enter No.: "))
nth = int(input("Enter nth position: "))
temp=num
c=0
while (num>0):
  c+=1
  num=num//10
digit=(temp//(10**(c-nth))%10)
print(f"Nth digit of {temp} is {digit}.")
