import re
import csv


def create_csv():

    with open("paragraph.txt", "r") as file:
        paragraph = file.read()

    patients = re.split(r"Patient \d+", paragraph)
    patients = [p.strip() for p in patients if p.strip()]

    data = []

    for patient in patients:

        # Age
        age = re.search(r"(\d+) years old", patient)
        age = age.group(1) if age else ""

        # BMI
        bmi = "High" if "high BMI" in patient else "Normal"

        # Glucose
        if "high blood glucose" in patient:
            glucose = "High"
        elif "normal blood glucose" in patient:
            glucose = "Normal"
        else:
            glucose = ""

        # Family history
        if "family history of diabetes" in patient:
            family_history = "Yes"
        elif "no family history of diabetes" in patient:
            family_history = "No"
        else:
            family_history = ""

        # Physical activity
        if "low physical activity" in patient:
            activity = "Low"
        elif "high physical activity" in patient or "regularly exercised" in patient:
            activity = "High"
        else:
            activity = ""

        # Target
        if "diagnosis was Diabetes" in patient:
            diabetes = "Yes"
        elif "diagnosis was No Diabetes" in patient:
            diabetes = "No"
        else:
            diabetes = ""

        data.append([
            age,
            bmi,
            glucose,
            family_history,
            activity,
            diabetes
        ])

    features = [
        "Age",
        "BMI",
        "Glucose",
        "Family_History",
        "Activity",
        "Diabetes"
    ]

    with open("medical_data.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(features)
        writer.writerows(data)

    print("CSV file created successfully.")


if __name__ == "__main__":
    create_csv()