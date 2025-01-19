str="123456789aabcadabcdabc"
sub_str="ab"
nth=int(input("Enter occurence number: "))
indx=-1
for i in range(1, nth+1):
  print(f"Searching {sub_str} from index {indx+1} to {len(str)}", end=" ")
  indx=str.find(sub_str, index+1, len(str))
  print(f"and found at index {indx} -> occurence no {i}")
  if (indx == -1):
    print(f"{sub_str} has not {nth} occurence in the given string {str}")
    break
if (indx != -1):
  print(f"Occurence {nth} of {sub_str} found in {str}")
    
