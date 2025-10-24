# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

# Authour : Zepora Lilly
# Date: 10/24/2025

def course_info():
    # Dictionary to store course ID and name pairs
    courses = {}

    # Input course ID and name pairs
    while True:
        course_id = input("Enter course ID (or 'done' to finish): ").strip()
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name: ").strip()
        courses[course_id] = course_name

    # Ask user for a subject
    subject = input("Enter subject code to search for (e.g., 'COS'): ").strip().upper()

    #Display matching courses
    print(f"\nCourses with subject '{subject}':")
    found = False
    for course_id, course_name in courses.items():
        if course_id.upper().startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True

    if not found:
        print("No course found with that subject.")

# Run the program 
course_info()
