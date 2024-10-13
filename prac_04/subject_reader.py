"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data from file and display it."""
    subjects = load_data()  # Load data as a list of lists
    display_subject_details(subjects)  # Display the subject details neatly


def load_data():
    """Read data from the file and return a nested list of subject details."""
    subjects = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()  # Remove any trailing whitespace or newlines
            parts = line.split(',')  # Split the line into code, lecturer, students
            parts[2] = int(parts[2])  # Convert student count to integer
            subjects.append(parts)  # Store each subject's data as a list
    return subjects  # Return the nested list


def display_subject_details(subjects):
    """Display the subject details in the required format."""
    for subject in subjects:
        code, lecturer, student_count = subject  # Unpack the subject details
        print(f"{code} is taught by {lecturer} and has {student_count} students")


if __name__ == "__main__":
    main()



main()