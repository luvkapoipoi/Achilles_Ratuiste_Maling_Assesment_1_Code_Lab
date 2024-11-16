#                   Exercise 7: Some Counting - 20 Marks
# Use your newly acquired knowledge of the for loop to complete the following tasks. 
#                Print all values to the console in each case.

# - Write a loop that counts up from 0 to 50 in increments of 1.
# - Write a loop that counts down from 50 to 0 in decrements of 1.
# - Write a loop that counts up from 30 to 50 in increments of 1.
# - Write a loop that counts down from 50 to 10 in decrements of 2.
# - Write a loop that counts up from 100 to 200 in increments of 5. You may include all loops in a single project

# Program

# 0 to 50 in increments of 1
print("Starting to count up from 0 to 50... ")
for int in range(0, 51): #This will start from 0 to 50
    print (int)
print("Done!")

# 50 to 0 in decrements of 1
print("Starting to count down from 50 to 0...")
for int in range(50, -1, -1): #This will start from 50 going down to 0
    print (int)
print("Done!")

# This loop follows three arguments for the range feature: (x, y, z) 
#   x= starting value
#   y= ending value
#   z= step value

# 30 to 50 in increments of 1
print("Starting to count up from 30 to 50...")
for int in range(30, 51): #This starts at 30 going up to 50
    print (int)
print("Done!")

# 50 to 10 in decrements of 2
print("Starting to count down from 50 to 10...")
for int in range(50, 9, -2): #This starts at 50 ending at 10
    print(int)
print("Done!")

# Why 9 and not 10?
# Placing 9 as an ending value makes the program print 10 as the last number.

# 100 to 200 in increments of 5
print("Starting to count up from 100 to 200 ")
for int in range(100, 201, 5): #This starts from 100 to 200
    print(int)
print("Done!")

# Explanation: From these loops, the range function is used with the for loop
#              simplifying the proess of writing a for loop program