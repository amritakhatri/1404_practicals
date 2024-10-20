"""
Wimbledon Champions Data Processing
Estimate: 30 minutes
Actual: 45 minutes
"""

# Read the data from the CSV file
filename = "wimbledon.csv"
champions = []
countries = set()

with open(filename, "r", encoding="utf-8-sig") as in_file:
    next(in_file)  # Skip the header row
    for line in in_file:
        data = line.strip().split(',')
        if len(data) >= 3:  # Check for enough columns
            champion_name = data[1].strip()
            champion_country = data[2].strip()
            champions.append(champion_name)
            countries.add(champion_country)

# Count the number of wins for each champion
champion_count = {}
for champion in champions:
    if champion in champion_count:
        champion_count[champion] += 1
    else:
        champion_count[champion] = 1

# Display the champions and their win counts
print("Wimbledon Champions:")
for champion in sorted(champion_count):
    print(f"{champion} {champion_count[champion]}")

# Display the countries in alphabetical order
print("\nThese countries have won Wimbledon:")
print(", ".join(sorted(countries)))
