a=input("Enter the value to be checked for type : ")

print(type(a))

if isinstance(a,int):
    print("integer")
elif isinstance(a,float):
    print("Float")
elif isinstance(a,str):
    print("String")
else:
    print("Other")
