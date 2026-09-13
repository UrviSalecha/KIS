import csv
from collections import defaultdict

# Read CSV file
def read_csv(filename):
    with open(filename, "r") as file:
        return list(csv.DictReader(file))

# Create equivalence classes
def equivalence(data, attrs):
    classes = defaultdict(list)
    for i, row in enumerate(data):
        classes[tuple(row[a] for a in attrs)].append(i)
    return classes

# Find positive region
def positive_region(data, attrs, decision):
    pos = set()
    for indexes in equivalence(data, attrs).values():
        decisions = {data[i][decision] for i in indexes}
        if len(decisions) == 1:
            pos.update(indexes)
    return pos

# Calculate dependency degree
def dependency(data, attrs, decision):
    return len(positive_region(data, attrs, decision)) / len(data)

# Find core attributes
def find_core(data, attrs, decision):
    original = dependency(data, attrs, decision)
    core = []

    print("\n--- CORE ANALYSIS ---")
    print("Original dependency:", round(original, 4))

    for attr in attrs:
        reduced = [a for a in attrs if a != attr]
        new = dependency(data, reduced, decision)

        print(f"Removing {attr}: dependency = {new:.4f}")

        if new < original:
            core.append(attr)
            print(f"{attr} -> CORE")
        else:
            print(f"{attr} -> DISPENSABLE")

    return core

# Display equivalence classes and find ambiguity
def show_classes(data, attrs, decision):
    classes = equivalence(data, attrs)
    ambiguous = []

    print("\n--- EQUIVALENCE CLASSES ---")

    for n, (key, indexes) in enumerate(classes.items(), 1):
        decisions = [data[i][decision] for i in indexes]

        print(f"E{n}: {key} -> {decisions}", end=" ")

        if len(set(decisions)) == 1:
            print("CERTAIN")
        else:
            print("AMBIGUOUS")
            ambiguous.append(indexes)

    return ambiguous

# Resolve ambiguity using Bayes theorem
def bayes(data, attrs, decision, indexes):
    target = data[indexes[0]]
    decisions = set(row[decision] for row in data)
    total = len(data)
    scores = {}

    for d in decisions:
        rows = [r for r in data if r[decision] == d]
        prior = len(rows) / total
        likelihood = 1

        for attr in attrs:
            match = sum(r[attr] == target[attr] for r in rows)
            values = len({r[attr] for r in data})
            likelihood *= (match + 1) / (len(rows) + values)

        scores[d] = prior * likelihood

    total_score = sum(scores.values())
    posterior = {d: p / total_score for d, p in scores.items()}
    result = max(posterior, key=posterior.get)

    print("\n--- BAYES RESOLUTION ---")
    print("Conditions:", tuple(target[a] for a in attrs))

    for d, p in posterior.items():
        print(f"P({d}|conditions) = {p:.4f}")

    print("Bayesian decision:", result)

# Main program
def run_task2():
    data = read_csv("medical_data.csv")

    attrs = ["Age", "BMI", "Glucose", "Family_History", "Activity"]
    decision = "Diabetes"

    ambiguous = show_classes(data, attrs, decision)
    core = find_core(data, attrs, decision)

    print("\n--- CORE KNOWLEDGE ---")
    print("Core attributes:", core)

    if ambiguous:
        print("\nAmbiguous classes:", len(ambiguous))
        for indexes in ambiguous:
            bayes(data, attrs, decision, indexes)
    else:
        print("\nNo ambiguity found.")

    pos = positive_region(data, attrs, decision)
    gamma = dependency(data, attrs, decision)

    print("\n--- ROUGH SET RESULTS ---")
    print("Positive region:", [i + 1 for i in pos])
    print("Dependency degree:", round(gamma, 4))

if __name__ == "__main__":
    run_task2()


'''
--- EQUIVALENCE CLASSES ---
E1: ('52', 'High', 'High', 'Yes', 'Low') -> ['Yes'] CERTAIN
E2: ('52', 'High', 'High', 'Yes', 'High') -> ['No'] CERTAIN
E3: ('29', 'Normal', 'High', 'Yes', 'High') -> ['Yes'] CERTAIN
E4: ('29', 'Normal', 'High', 'Yes', 'Low') -> ['No'] CERTAIN
E5: ('29', 'Normal', 'Normal', 'Yes', 'High') -> ['No'] CERTAIN
E6: ('52', 'Normal', 'Normal', 'Yes', 'Low') -> ['Yes', 'No'] AMBIGUOUS
E7: ('29', 'High', 'High', 'Yes', 'Low') -> ['Yes', 'No'] AMBIGUOUS
E8: ('52', 'High', 'Normal', 'Yes', 'High') -> ['No', 'Yes'] AMBIGUOUS
E9: ('29', 'Normal', 'Normal', 'Yes', 'Low') -> ['No'] CERTAIN

--- CORE ANALYSIS ---
Original dependency: 0.5
Removing Age: dependency = 0.3333
Age -> CORE
Removing BMI: dependency = 0.4167
BMI -> CORE
Removing Glucose: dependency = 0.2500
Glucose -> CORE
Removing Family_History: dependency = 0.5000
Family_History -> DISPENSABLE
Removing Activity: dependency = 0.1667
Activity -> CORE

--- CORE KNOWLEDGE ---
Core attributes: ['Age', 'BMI', 'Glucose', 'Activity']

Ambiguous classes: 3

--- BAYES RESOLUTION ---
Conditions: ('52', 'Normal', 'Normal', 'Yes', 'Low')
P(Yes|conditions) = 0.3599
P(No|conditions) = 0.6401
Bayesian decision: No

--- BAYES RESOLUTION ---
Conditions: ('29', 'High', 'High', 'Yes', 'Low')
P(Yes|conditions) = 0.4837
P(No|conditions) = 0.5163
Bayesian decision: No

--- BAYES RESOLUTION ---
Conditions: ('52', 'High', 'Normal', 'Yes', 'High')
P(Yes|conditions) = 0.4676
P(No|conditions) = 0.5324
Bayesian decision: No

--- ROUGH SET RESULTS ---
Positive region: [1, 2, 3, 4, 5, 12]
Dependency degree: 0.5
'''