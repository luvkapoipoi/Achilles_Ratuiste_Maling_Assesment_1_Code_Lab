#                          Exercise 6: Brute Force Attack - 30 Marks
#  Write a program that simulates a password entry system. The correct password is defined as 12345. 
#  The program should keep asking the user to enter the password until they provide the correct one.

#  Basic Requirements:
#   1. Define the correct password.
#   2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#   3. Output an appropriate message when the correct password is entered.

#  Optional Requirements:
#  Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, 
#  inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user 
#  that the authorities have been alerted.

# Program

correct_password = "12345"

while True: # The 'while true' creates an infinite loop as it will keep asking for the user's correct password
    enter_password = input ("Enter Your Password: ")

    if  enter_password == correct_password: 
        print ("Logged In! Please wait...")

        break   #This break exits the loop. This means the user has entered the correct password.

    else:
        print ("Incorrect Password, please try again :(")

# Explanation: In this program, it presents a password system in which asks the user for their password to log them in to their system or to whatever 
#              to they are trying to get access to. It showcases a python loop (infinite while loop) as it gives the user infinite chances in attempting
#              to input their password. 

# Output:
#  Enter Your Password: 232
#  Incorrect Password, please try again: 
#  Enter Your Password: 12345
#  Logged In! Please wait...

# Advanced Program

correct_password = "12345"

maximum_attempts = 5
attempts = 0
# This shows how many attempts the user can make

while attempts < maximum_attempts:
    enter_password = input("Enter Your Password: ")
    attempts += 1 #This makes the attempts lessen everytime the user enters the wrong password

    if enter_password == correct_password:
        print("Logged In! Please wait...")
        break
    
    else:
        remaining_attempts = maximum_attempts - attempts
        
        if remaining_attempts > 0:
            print(f"The password is incorrect . You have {remaining_attempts} attempt(s) left")
        
        else:
            print(f"You have no more remaining attempts, authorities have been alerted")

# This program uses a while loop with an if-else statement as the while loop repeats until the user either gets the 
# password right or uses all the attempts. 

# Output:
# Enter Your Password: 12345 
# Logged In! Please wait...
# Enter Your Password: 12  
# The password is incorrect . You have 4 attempt(s) left
# Enter Your Password: 234
# The password is incorrect . You have 3 attempt(s) left
# Enter Your Password: 34
# The password is incorrect . You have 2 attempt(s) left
# Enter Your Password: 34
# The password is incorrect . You have 1 attempt(s) left
# Enter Your Password: 3
# You have no more remaining attempts, authorities have been alerted





    