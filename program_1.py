# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

# Program #1: Initials Extractor
# Author: Zepora Lilly
#Date: 10/24/2025
def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    # Split the name into parts
    name_parts = personsName.strip().split()

    for part in name_parts:
        # Make sure it's not an empty string
        if part:
            personsInitials += part[0].upper() + ". "
            
    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)