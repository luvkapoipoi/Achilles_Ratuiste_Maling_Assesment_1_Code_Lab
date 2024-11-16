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
        print ("Incorrect Password, please try again: ")

# Explanation: In this program, it presents a password system in which asks the user for their password to log them in to their system or to whatever 
#              to they are trying to get access to. It showcases a python loop (infinite while loop) as it gives the user infinite chances in attempting
#              to input their password. 

# Output:
#  Enter Your Password: 232
#  Incorrect Password, please try again: 
#  Enter Your Password: 12345
#  Logged In! Please wait...



    