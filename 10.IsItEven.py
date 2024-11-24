#                        Exercise 10: Is it even? - 35 Marks
# Write a program that tests if a value is even or odd. Follow the instructions outlined below:

# Instructions:
# > The program should ask the user for a number from within the main function.
# > The entered number should be passed to a function that determines if the value is even or odd.
# > The function should return a message indicating whether the number is even or odd.
# > The message returned by the function should be printed from within the main function.

# Program

def check_even_odd(number):
    """Checks if a number is even or odd"""
    return "Even" if number %2 == 0 else "Odd"

def main():
    ask_number = int(input("Enter a number: ")) #This asks the user for a number
    result = check_even_odd(ask_number) #This will check whether the user inputs an even or odd number
    print(result) #Program will output either Even or Odd depending on what the user inputted.

if __name__ == "__main__":  
    main()   #Applying this ensures that the program is runned directly, not when its imported

#Output: 
    