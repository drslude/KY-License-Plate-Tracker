import json
import os

# Load counties from counties.json
def load_counties():
    with open("counties.json", "r") as file:
        return json.load(file)["counties"]

# Save seen counties to seen_counties.json
def save_seen_counties(seen_counties):
    with open("seen_counties.json", "w") as file:
        json.dump({"seen_counties": seen_counties}, file)

# Load seen counties from seen_counties.json or create if it doesn't exist
def load_seen_counties():
    if os.path.exists("seen_counties.json"):
        with open("seen_counties.json", "r") as file:
            return json.load(file).get("seen_counties", [])
    else:
        return []

# Mark a county as seen
def mark_county_as_seen(county, counties, seen_counties):
    if county in counties and county not in seen_counties:
        seen_counties.append(county)
        save_seen_counties(seen_counties)
        print(f"{county} marked as seen.")
    elif county in seen_counties:
        print(f"{county} has already been marked as seen.")
    else:
        print("County not found.")

# Display remaining counties
def display_remaining_counties(counties, seen_counties):
    remaining_counties = [county for county in counties if county not in seen_counties]
    print("Remaining counties to see:")
    for county in remaining_counties:
        print(county)
    print(f"\nYou have {len(remaining_counties)} counties left to see out of {len(counties)}.\n")

# Display seen counties
def display_seen_counties(seen_counties):
    if seen_counties:
        print("Counties you've seen:")
        for county in seen_counties:
            print(county)
        print(f"\nYou've seen {len(seen_counties)} counties.\n")
    else:
        print("You haven't marked any counties as seen yet.\n")

# Display progress
def display_progress(counties, seen_counties):
    print(f"You've seen {len(seen_counties)} counties out of {len(counties)}.")
    print(f"Progress: {len(seen_counties) / len(counties) * 100:.2f}%\n")

def main():
    counties = load_counties()
    seen_counties = load_seen_counties()
    
    while True:
        print("\nKentucky License Plate Tracker")
        print("1. Mark a county as seen")
        print("2. Display remaining counties")
        print("3. Display seen counties")  # New option added
        print("4. Show progress")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            county = input("Enter the county name: ").title()
            mark_county_as_seen(county, counties, seen_counties)
        elif choice == "2":
            display_remaining_counties(counties, seen_counties)
        elif choice == "3":
            display_seen_counties(seen_counties)
        elif choice == "4":
            display_progress(counties, seen_counties)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
