#------------------------------------------
# HOW WE ACCESS THE DIFFERENT LISTS IN PYTHON.
#------------------------------------------

#---------------------------------
# 1. ACCESSING THE LIST BY INDEX.
#---------------------------------
fruits = ["apple","banana","berry","mango","orange"] # string of characters.
print(fruits[1])    #1 means 2nd element.
print(fruits[-1])   #-1 means last element.
print(fruits[0])     #0 means 1st element.

#---------------------------------
# 2. SLICING THE LIST BY INDEX.
#---------------------------------
numbers = [1,2,3,4,5,6,7,8,9] # intergers.
print(numbers[1:4])    #1:4 means 2nd to 4th element.
print(numbers[0:4])    #0:4 means 1st to 4th element.
print(numbers[:3])     #:3 means 1st to 3rd element.
print(numbers[3:])     #3: means 3rd to last element.
print(numbers[:])      #[:] means all elements.

#---------------------------------
# 3. ADVANCED SLICING OF THE LIST BY INDEX.
# ---------------------------------
mixed = [1,"apple", 2 ,5.0,"pizza",4, "orange","banana"] #mixed data types. 
print(mixed[1:4:2])   #1:4:2 means 2nd to 4th element with step of 2.
print(mixed[0:4:2])   #0:4:2 means 1st to 4th element with step of 2.
print(mixed[:4:2])    #0:4:2 means 1st to 4th element with step of 2.
print(mixed[3::2])    #3::2 means 3rd to last element with step of 2.
print(mixed[::2])     #0::2 means all elements with step of 2.
print(mixed[::-1])    #0::-1 means all elements in reverse order.
print(mixed[4:2:-2])  #4:2:-2 means 4th to 2nd element with step of -2.  