"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is: Language,Typing,Reflection,Year,Pointer Arithmetic
    in_file.readline()  # Skip the header line
    for line in in_file:
        # Strip newline and split into parts
        parts = line.strip().split(',')
        # Reflection and pointer arithmetic are stored as "Yes"/"No" and should be converted to Boolean
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        # Construct a ProgrammingLanguage object with the new field
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        # Add the language object to the list
        languages.append(language)
    in_file.close()

    # Display all languages using their string representations
    for language in languages:
        print(language)


main()


def using_csv():
    """Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()  # Skip header
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    reader = csv.reader(in_file)

    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))


# Uncomment functions below to run alternative versions
# using_csv()
# using_namedtuple()
# using_csv_namedtuple()
