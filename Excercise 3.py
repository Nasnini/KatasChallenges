# 3 Excercise: Draw a square

#def square():

side = int(input("Please Enter any Side of a Square  : "))

print("Square Star Pattern") 

for i in range(side):
    for i in range(side):
        print('#', end = '  ')
    print()
