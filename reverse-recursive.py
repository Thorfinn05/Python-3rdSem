def rev_rec(n, rev=0):
  if n == 0:
    return rev
  else:
    return rev_rec(n//10, rev*10 + n % 10)

num=int(input("Enter No.: "))
print(f"The reverse of the number {num} is {rev_rec(num)}.")
