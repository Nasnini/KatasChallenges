# 5 Excercise: Draw a icosceles triangle

#Defining function
def icos_triangle():

    # Prompt user to enter input
    size = int(input("Please enter the number of rows: "))

    # For loop
    m = (2 * size) - 2
    for i in range(0, size):

        for j in range(0, m):
            print(end=" ")
        m = m - 1    # decrementing m after each loop
        for j in range(0, i + 1):
            # printinh full triangle pyramid using hash
            print("# ", end='')
        print(" ")

# Printing function
print(icos_triangle())

