#Function will have more parameters
'''def multiply(x,y):
    result=x*y
    print(result)
multiply(2,3)
multiply(5,6)'''


'''def calc(x,y,z):
    Add=x+y+z
    sub=x-y
    mul=x*y*z
    Div=x/y
    print("The results are as follows :")
    print(Add)
    print(sub)
    print(mul)
    print(Div)

calc(90,80,10)'''


def multiply(x,y=2,z=7):
    print(x*y*z)
multiply(1,2,3)
multiply(0,2,2)
multiply(2,z=5)
#Pass the value from left to right





