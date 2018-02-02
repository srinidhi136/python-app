#SIMPLE CALCULATOR BY SIMPLE FUNCTIONS
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
def Mod(x,y):
    return x%y

print("Select the required operations:")
print("1.Add")
print("2.Sub")
print("3.Multiply")
print("4.Modulous")

choice = input("Enter the choice 1,2,3 or 4 : ")
x = int(input("Enter the first number :"))
y = int(input("Enter the second number :"))
z = int(input("Enter the third number :"))

if choice =="1" :
    print("Addition = ",(add(x,y)))

elif choice =="2" :
    print("Subtraction = ",(sub(x,y)))
elif choice =="3" :
    print ("Multiplication = " , (mul(x,y)))
elif choice =="4" :
    print ("Modulus = ", (Mod(x,y)))
else:print("INVALID SELECTION, Please try with some other input")



