def main():
    """Get monthly incomes and display a cumulative income report."""
    num_months = int(input("How many months? "))  # Refactored: 'months' to 'num_months'
    incomes = get_incomes(num_months)  # Collect incomes into a list
    print_income_report(incomes)  # Print the report


def get_incomes(num_months):
    """Get incomes from the user and store them in a list."""
    incomes = []
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    """Print the income report with cumulative totals."""
    print("\nIncome Report")
    print("-------------")
    cumulative_total = 0  # Initialize cumulative total

    for month, income in enumerate(incomes, start=1):
        cumulative_total += income  # Update cumulative total
        # Nicely formatted output with f-strings
        print(f"Month {month:2} - Income: ${income:10.2f}   Total: ${cumulative_total:10.2f}")


# Run the program
if __name__ == "__main__":
    main()
