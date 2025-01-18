def prime_fact(num):
  while (num % 2 == 0):
    print(2, end=" ")
    num//=2
  for i in range(3, int(num//2)+1, 2):
    while (num % i == 0):
      print(i, end=" ")
      num//=i
  if num > 2:
    print(num, end=" ")

num = int(input("Enter No.: "))
print(f"Prime factors of {num} are: ",end=" ")
prime_fact(num)
    

