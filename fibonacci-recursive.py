def fibonacci(n):
  if (n<=1):
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

n=int(input("Enter No.: "))
print("Fibonacci series: ",end= " ")
i=0
for i in range(n):
  if((fibonacci(i))>n):
    break
  print(fibonacci(i), end=" ")
print()
