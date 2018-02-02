6#the function print takes 0 or more than 1 chars
print ("X","X","X", sep='x')
print('X', end = " ")
print('y',end = " ")
print('Z',end = " Welcome")

# print can get 2 spl parameters...sep & end. sep indicates what should be printed in between the each of the parameter
# End indicates what print function should put after all the parameters have been displayed.

#format fun():

print("The format function :")
print("The first 3 numbers are {:1},{:2} and {:3}.".format("one","two","three"))

print("The first 3 numbers are {:6},{:^8} and {:10}.".format("one","two","three"))


print("Format fuction example")
print("{} divided by {} is {}".format(1,2,3))




