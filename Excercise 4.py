# 4 Excercise: Draw a right handed triangle

# Defining function
def right_triangle():

    size = int(input("Please enter the number of rows: "))

    print("Right Angled Triangle: ")
    # While loop to print function
    i = 1
    while(i <= size):
        j = 1
        while(j <= i):
            print('#', end = '  ')
            j = j + 1
            i = i + 1

# Printing function
print(right_triangle())
