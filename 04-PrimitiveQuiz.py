#                       Exercise 3: Biography - 25 Mark
# In this exercise, you'll create a simple program that asks the user a question,
#                evaluates their answer, and provides feedback.

#     Steps: 
#     1 Write a program that asks the user "What is the capital of France?" and waits for their response.
#     2 If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#     3 If the answer is incorrect, the program should print a message saying the answer is wrong.

# Advanced Requirements: Ignore Capitalization: Modify your program to accept answers regardless of
# the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct). 
# Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European 
# countries. Provide feedback for each question.

#Program

answer = input("What is the capital of France? ")

if answer.lower() == "paris": #This allows the user to input the word 'paris' in any form (eg: Paris, PaRis)

    print ("The answer you have given is correct ")

else:

    print ("The answer you have given is wrong. ")

#Guess the Capital of Each City

Quiz = [
    ("What is the capital of France?", "Paris"), #1
    ("What is the capital of Germany?", "Berlin"), #2
    ("What is the capital of Italy?", "Rome"), #3
    ("What is the capital of Spain?", "Madrid"), #4
    ("What is the capital of the Netherlands?", "Amsterdam"), #5
    ("What is the capital of Greece?", "Athens"), #6
    ("What is the capital of Portugal?", "Lisbon"), #7
    ("What is the capital of Belgium?", "Brussels"), #8
    ("What is the capital of Switzerland?", "Bern"), #9
    ("What is the capital of Belgium?", "Brussels"), #10
]

#Creates a tuple which acts like a Quiz

print ("Welcome to Guess the Capital of Each City" )

for Quiz, correct_answer in Quiz: # The 'for' loop goes throught each question, asking and checking if the answer is correct
    answer = input(Quiz + " ")
    if answer.lower() == correct_answer.lower(): #This allows the user to input the word 'paris' in any form (eg: Paris, PaRis)

        print ("The answer you have given is correct ")

    else: 
        print("The answer you have given is wrong. ")

print ("That is the end of the quiz, thank you. ")


