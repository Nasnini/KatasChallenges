# 3 Excercise: Draw a square

# Defining square function
def square():
    side = int(input("Please Enter any Side of a Square  : ")) # Prompt user input

    print("Square Hash Pattern") 

    # For loop to print square
    for i in range(side):
        for i in range(side):
            print('#', end = '  ')

# Printing the square function
print(square())
