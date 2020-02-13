# 7 Excercise: Combine two lists/arrays

#function taking 2 parameters
def combineList(list1, list2): 
    return [sub[item] for item in range(len(list2))  #altenating between list1 and list2
                      for sub in [list1, list2]] 
      
# Driver code 
list1 = [11, 22, 33] 
list2 = [1, 2, 3] 
print(combineList(list1, list2))     #Print the function with the arguements parse in list1 and list2
