"""
Frist  go through the students' list, calculate their average grades, and save their information to a file.
Secondly open the file and read each student's information and their average grades.
Then Check if any student's average grade is below the set limit; if yes, add their name to a list.
Later on Make sure the program handles file errors properly to avoid crashes.
Finally print the names of students who need improvement."""

#Lets create a dictonary list
students = [
    {"name": "Alice", "ID": "1001", "grades": [85, 90, 78]},
    {"name": "Bob", "ID": "1002", "grades": [70, 68, 65]},
    {"name": "Charlie", "ID": "1003", "grades": [95, 92, 88]},
    {"name": "David", "ID": "1004", "grades": [60, 64, 58]},
]

filename = "student_averages.txt"
threshold = 70


def calculate_average(grades):
    if len(grades) == 0:  # Here we will Check if the list is empty
        return 0
    total = sum(grades)  # Lets Sum up all the grades
    return total / len(grades)  # Divide total by the number of grades


def write_to_file(students, filename):
    try:
        with open(filename, 'w') as file:  # Now we will open the file in write mode so that we can use it as a context manager
            for student in students:  # Lets go through each student
                average_grade = calculate_average(student['grades'])  # Get the average grade
                # Lets write the student's information into the file
                file.write(f"{student['name']} (ID: {student['ID']}) - Average Grade: {round(average_grade, 2)}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_and_identify(filename, threshold):
    below_threshold = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    name_part, grade_part = line.rsplit("- Average Grade: ", 1)
                    avg_grade = float(grade_part.strip())
                    if avg_grade < threshold:
                        name = name_part.split(" (ID:")[0].strip()
                        below_threshold.append(name)
                except ValueError:
                    print(f"Invalid line format: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return below_threshold


# Lets  write students data into a file
write_to_file(students, filename)

# Lets identify students who are below the threshold value
students_below_threshold = read_and_identify(filename, threshold)

# finally lets  print t the result
print("Students needing improvement:", students_below_threshold)
