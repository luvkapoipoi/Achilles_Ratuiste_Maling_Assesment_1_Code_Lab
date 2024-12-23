#                      Exercise 8: Simple Search - 30 Marks
#     Write a program that searches for a specific string within a list of strings. 
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , 
#                      and your task is to search for "Sam".

#  Optional Requirements:
#  Allow the user to input the search term instead of using a predefined value.
#  Implement the search functionality based on user input.

#Program

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Dave"]

name_search = "Sam"   #This tells the program the name we want to search in the list

#if-else statement checks whether the name is on the list or not
if name_search in list_of_names:
    print(f'{name_search} is in the list.')

else:
    print(f'{name_search} is not in the list.')

# Output:
# When Sam is in the list:
# - "Sam is in the list."
# When Sam is not on the list:
# - "Sam is not in the list."

#Optional Requirement

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Dave"]

ask_user = input("Enter a name you want to search for: ") #This specifically tells the program the name we want to search in the list

#if-else statement checks whether the name is on the list or not
if ask_user in list_of_names:
    print(f'{ask_user} is in the list.')

else:
    print(f'{ask_user} is not in the list.')

#Output: 
# Enter a name you want to search for: Jake
# Jake is in the list.

# Enter a name you want to search for: Achi
# Achi is not in the list.