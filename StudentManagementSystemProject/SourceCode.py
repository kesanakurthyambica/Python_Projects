
# Import necessary modules
import os
import platform

# Define a global list to store student names
global listStd
listStd = ["Yaseen", "Vishesh", "Ajden", "Gopi"]  # Initial list of students

# Define the main function for the student management system
def manageStudent():
    global listStd
    # Display a welcome message
    print("""
=================================================
       Welcome To Student Management System       
=================================================
Enter 1 : To View Student's List
Enter 2 : To Add New Student
Enter 3 : To Search Student
Enter 4 : To Remove Student
Enter 5 : To Exit
=================================================
    """)
    try:
        # Take user input
        userInput = int(input("Please select an option from the above: "))
        if userInput == 1:
            # View student list
            print("\nStudent List:")
            for index, student in enumerate(listStd, start=1):
                print(f"{index}. {student}")
        elif userInput == 2:
            # Add a new student
            newStudent = input("Enter the name of the new student: ")
            if newStudent:
                listStd.append(newStudent)
                print(f"{newStudent} has been added to the list.")
            else:
                print("Invalid input. Name cannot be empty.")
        elif userInput == 3:
            # Search for a student
            searchName = input("Enter the name of the student to search: ")
            if searchName in listStd:
                index = listStd.index(searchName)  # Get the index of the student
                print(f"{searchName} is present in the list at position {index + 1}.")  # Add 1 for human-readable position
            else:
                print(f"{searchName} is not found in the list.")
        elif userInput == 4:
            # Remove a student
            removeName = input("Enter the name of the student to remove: ")
            if removeName in listStd:
                listStd.remove(removeName)
                print(f"{removeName} has been removed from the list.")
            else:
                print(f"{removeName} is not found in the list.")
        elif userInput == 5:
            # Exit the system
            print("Thank you for using the Student Management System. Goodbye!")
            exit()
        else:
            print("Invalid option! Please choose a valid number.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Run the student management system in a loop
while True:
    manageStudent()