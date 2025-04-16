import datetime
import json
import os

# File to store BMI records
BMI_FILE = "bmi_records.json"

# Load existing data or create an empty list
def load_bmi_data():
    if os.path.exists(BMI_FILE):
        with open(BMI_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

# Save BMI data to file
def save_bmi_data(data):
    with open(BMI_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Determine BMI Category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Add new BMI entry
def add_bmi_entry():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    date = str(datetime.date.today())

    entry = {
        "name": name,
        "date": date,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    }

    data = load_bmi_data()
    data.append(entry)
    save_bmi_data(data)

    print(f"\n{name}, your BMI is {bmi} ({category})\n")

# View all BMI entries
def view_bmi_entries():
    data = load_bmi_data()
    if not data:
        print("No BMI records found.")
        return

    print("\n--- BMI History ---")
    for entry in data:
        print(f"{entry['date']} | {entry['name']} | {entry['weight']}kg | {entry['height']}cm | BMI: {entry['bmi']} ({entry['category']})")
    print("--------------------\n")

# Main menu
def main():
    while True:
        print("===== BMI TRACKER =====")
        print("1. Add BMI Entry")
        print("2. View BMI History")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_bmi_entry()
        elif choice == '2':
            view_bmi_entries()
        elif choice == '3':
            print("Exiting BMI Tracker. Stay healthy!")
            break
        else:
            print("Invalid option. Try again.\n")

# Run the program
if __name__ == "__main__":
    main()
