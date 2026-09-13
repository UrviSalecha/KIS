import csv
from collections import defaultdict


# Read CSV
def read_csv(filename):
    with open(filename, "r") as file:
        return list(csv.DictReader(file))


# Create equivalence classes
def equivalence(data, attrs):
    classes = defaultdict(list)

    for i, row in enumerate(data):
        key = tuple(row[a] for a in attrs)
        classes[key].append(i)

    return classes


# Generate rules
def generate_rules(data, core, decision):

    classes = equivalence(data, core)

    rules = []

    print("\n--- GENERATED RULES ---")

    for conditions, indexes in classes.items():

        decisions = {data[i][decision] for i in indexes}

        # Certain class
        if len(decisions) == 1:

            result = list(decisions)[0]

            rule = "IF "

            for i, attr in enumerate(core):
                rule += f"{attr} = {conditions[i]}"

                if i < len(core) - 1:
                    rule += " AND "

            rule += f" THEN {decision} = {result}"

            rules.append(rule)
            print(rule)

        # Ambiguous class
        else:

            # Count Yes and No
            yes_count = sum(
                1 for i in indexes
                if data[i][decision] == "Yes"
            )

            no_count = sum(
                1 for i in indexes
                if data[i][decision] == "No"
            )

            # Simple Bayesian-style decision
            if no_count >= yes_count:
                result = "No"
            else:
                result = "Yes"

            rule = "IF "

            for i, attr in enumerate(core):
                rule += f"{attr} = {conditions[i]}"

                if i < len(core) - 1:
                    rule += " AND "

            rule += f" THEN {decision} = {result}"

            rules.append(rule)

            print(rule, "(Ambiguous → resolved)")


    return rules


def run_task3():

    data = read_csv("medical_data.csv")

    # Taken directly from Task 2
    core = ["Age", "BMI", "Glucose", "Activity"]

    decision = "Diabetes"

    rules = generate_rules(data, core, decision)

    print("\n--- FINAL RULE SET ---")

    for rule in rules:
        print(rule)


if __name__ == "__main__":
    run_task3()