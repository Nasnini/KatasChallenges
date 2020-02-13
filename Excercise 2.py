# 2. Exercise: check if a number is even

# prompts user to enter a number and store in 'num' variable
num=int(input("Enter a number for check odd or even: "))
def find_even_odd(num):  #parsing num as the arguement for even_odd function
        
    # Check is num is even or odd
    if(num%2==0):   #condition to check
        print(num," Is an even")
    else:
        print(num," is an odd")
    find_even_odd(num);     # function call
