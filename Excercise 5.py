# 5 Excercise: Draw a icosceles triangle

size = int(input("Please enter the number of rows: "))

m = (2 * size) - 2
for i in range(0, size):

    for j in range(0, m):
        print(end=" ")
    m = m - 1 #decrementing m after each loop
    for j in range(0, i + 1):
        #printinh full riangle pyramid using hash
        print("# ", end='')
    print(" ")

