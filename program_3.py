# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

# Author : Zepora Lilly
# Date: 10/24/2025

import random

def capital_quiz():
    # Dictionary of U.S states and their capitals
    states_and_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Minnesota": "Saint Paul",
        "New York": "Albany",
        "Texas": "Austin",
        "Washington": "Olympia",
        "Wisconsin": "Madison"
    }

    correct = 0
    incorrect = 0

    # Shuffle the states for random quiz order
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    for state in states:
        user_answer = input(f"What is the capital of {state}? ").strip()
        if user_answer.lower() == states_and_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! The capital of {state} is {states_and_capitals[state]}.")
            incorrect += 1
        
    print("\nQuiz Complete!")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

# Run the quiz
capital_quiz()
