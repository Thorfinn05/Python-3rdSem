def gcd(a, b):
  if (b==0):
    return a
  else:
      return gcd(b, a%b)

num1 = int(input("Enter no.: "))
num2 = int(input("Enter no.: "))
print(f"GCD of {num1} and {num2} is : ",gcd(num1, num2)
