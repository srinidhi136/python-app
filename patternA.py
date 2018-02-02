####PROGRAM TO PRINT THE PATTERN A ####

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4)and(row!=0)) or ((row==0) or(row==3)) and ((col>0) and (col<3)):
            print("*",end="")
        else:
            print(end=" ")
    print()

print('\n')

### END OF THE PROGRAM #########

for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or ((row==0) or(row==3)) and ((col>0) and (col<3)):
            print("*",end="")
        else:
            print(end=" ")
    print()
