#                      Exercise 8: Simple Search - 30 Marks
#     Write a program that searches for a specific string within a list of strings. 
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , 
#                      and your task is to search for "Sam".

#  Optional Requirements:
#  Allow the user to input the search term instead of using a predefined value.
#  Implement the search functionality based on user input.

#Program

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name_search = "Sam"   #This tells the program the name we want to search in the list

#if-else statement checks whether the name is on the list or not
if name_search in list_of_names:
    print(f'{name_search} is in the list.')

else:
    print(f'{name_search} is not in the list')

