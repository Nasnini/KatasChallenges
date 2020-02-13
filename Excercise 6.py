# 6 Excercise: Find the longest string

# Defigning the function
def longest():

# List to check which string is the longest
test_list = ["the","quick","brown", "fox", "ate", "my", "chickens"] 
  
# Printing original list  
print("The original list : " + str(test_list)) 
  
# Finding the longest element in the list 
# using loop 
max_len = -1
for ele in test_list: 
    if len(ele) > max_len: 
        max_len = len(ele) 
        result = ele 
  
# printing result 
print("The longest string in the list is: " + result)
