s=input("Enter string: ")
l=s.split()
c={}
for w in l:
  if (w in c):
    c[w]+=1
  else:
    c[w]=1
print(f"No. of occurene=ces of each word {c}.")
