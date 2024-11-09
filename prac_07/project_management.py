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

def filter_projects_by_date(projects):
    """Filter projects based on a start date."""
    date_input = input("Enter a date (dd/mm/yyyy) to filter projects: ")
    filter_date = datetime.strptime(date_input, "%d/%m/%Y")
    filtered_projects = [p for p in projects if p.start_date >= filter_date]

    print(f"Projects started on or after {filter_date.strftime('%d/%m/%Y')}:")
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Enter project name: ")
    start_date_input = input("Enter project start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date_input, "%d/%m/%Y")
    priority = int(input("Enter project priority: "))
    estimate = float(input("Enter project cost estimate: "))
    completion = int(input("Enter project completion percentage: "))

    new_project = Project(name, start_date, priority, estimate, completion)
    projects.append(new_project)
    print("Project added successfully.")

def update_project(projects):
    """Update an existing project's details."""
    name = input("Enter the project name to update: ")
    project_to_update = None
    for project in projects:
        if project.name.lower() == name.lower():
            project_to_update = project
            break

    if project_to_update:
        new_name = input(f"Enter new name (or press Enter to keep '{project_to_update.name}'): ") or project_to_update.name
        new_start_date_input = input(f"Enter new start date (or press Enter to keep '{project_to_update.start_date.strftime('%d/%m/%Y')}'): ") or project_to_update.start_date.strftime('%d/%m/%Y')
        new_start_date = datetime.strptime(new_start_date_input, "%d/%m/%Y")
        new_priority = input(f"Enter new priority (or press Enter to keep '{project_to_update.priority}'): ")
        new_priority = int(new_priority) if new_priority else project_to_update.priority
        new_estimate = input(f"Enter new estimate (or press Enter to keep '{project_to_update.estimate}'): ")
        new_estimate = float(new_estimate) if new_estimate else project_to_update.estimate
        new_completion = input(f"Enter new completion percentage (or press Enter to keep '{project_to_update.completion}'): ")
        new_completion = int(new_completion) if new_completion else project_to_update.completion

        project_to_update.name = new_name
        project_to_update.start_date = new_start_date
        project_to_update.priority = new_priority
        project_to_update.estimate = new_estimate
        project_to_update.completion = new_completion
        print("Project updated successfully.")
    else:
        print("Project not found.")

if __name__ == "__main__":
    main()
