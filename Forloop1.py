"""for letter in "banana":
    print(letter)
print("DONE")

fruit = "banana"
for letter in fruit:
    print(letter)
    if letter == 'n':
        fruit="letter"
        print(fruit)"""

"""for i in range(10,100,1000):
    print(i)"""


"""for i in range(4):
    print(i)
for j in range(i+1,4):
    print("({},{})".format(i,j))
print(i)
print(j)"""

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(("({},{},{})").format(i,j,k))
