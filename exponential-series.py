def fact(x):
  if(x<=1):
    return 1
  else:
    return x*(fact(x-1))

sum=0
for r in range(0, 1000):
  sum+=(((-1)**r)/(fact(r)))

print(f"Value of e^(-1) is {sum}")
