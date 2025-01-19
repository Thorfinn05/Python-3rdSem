str="ABCDEJKLMNOP"
nth=int(input("Enter position to insert: "))
sub_str=input("Enter sub_string to insert: ")
str_new=str[:nth] + sub_str + str[nth:]
print(str_new)
