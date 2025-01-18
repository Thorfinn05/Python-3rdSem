str="ABCDEFGHIJKLMNOP"
nth=int(input("Enter position to delete: "))
sub_str_len=int(input("Enter length of string to delete: "))
str_new=str[:nth] +str[nth+sub_str_len:]
print(str_new)
