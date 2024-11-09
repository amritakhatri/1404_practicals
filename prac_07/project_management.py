"""
project_management.py
Time Estimate: 90 minutes
This module handles the main functionality of the Project Management Program.
"""

from project import Project
from datetime import datetime

DEFAULT_FILE = 'projects.txt'
def main():
    """Main function to run the Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    choice = ''
    while choice != 'Q':
        display_menu()
        choice = input("Choose an option: ").upper()
        if choice == 'L':
            filename = input("Enter filename to load: ") or DEFAULT_FILE
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save to: ") or DEFAULT_FILE
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            print("Thank you for using the Project Management Program.")
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    """Displays the main menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion = parts
            project = Project(name, datetime.strptime(start_date, "%d/%m/%Y"), int(priority), float(cost_estimate), int(completion))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [p for p in projects if p.completion < 100]
    completed_projects = [p for p in projects if p.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=Project.get_priority):
        print(project)

    print("Completed projects:")
    for project in sorted(completed_projects, key=Project.get_priority):
        print(project)









if __name__ == "__main__":
    main()

