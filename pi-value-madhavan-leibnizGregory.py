sum=0
for k in range (0, 10000000):
  sum+=((-1**k)/((2*k)+1))
  val=sum*4
print(f"Vale of pi is: {val})
