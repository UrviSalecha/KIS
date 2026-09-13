# Medical Knowledge Mining using Rough Set Theory and Bayes Theorem

## 📌 Project Overview

This project extracts medical information from a natural-language paragraph, converts it into structured data, analyzes the data using **Rough Set Theory**, resolves ambiguous cases using **Bayes Theorem**, and finally generates **IF-THEN decision rules**.

The project is divided into four tasks:

1. **Data Extraction** – Extract medical attributes from a paragraph and create a CSV file.
2. **Knowledge Discovery** – Use Rough Set Theory to find important attributes and identify ambiguous cases. Bayes Theorem is used to resolve ambiguity.
3. **Rule Generation** – Generate IF-THEN rules from the discovered knowledge.
4. **Project Integration** – Combine all three tasks into a single workflow.

---

## 🎯 Objective

The main objective is to convert unstructured medical information into useful decision rules.

For example:

```text
Age = 52
BMI = High
Glucose = High
Activity = Low
```

can result in a rule such as:

```text
IF Age = 52 AND BMI = High AND Glucose = High AND Activity = Low
THEN Diabetes = Yes
```

---

## 🏗️ Project Structure

```text
medical_project/
│
├── main.py
├── task1.py
├── task2.py
├── task3.py
├── medical_data.csv
├── rules.txt
└── README.md
```

### Files

| File               | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| `main.py`          | Integrates all tasks into one workflow           |
| `task1.py`         | Extracts medical information and creates the CSV |
| `task2.py`         | Performs Rough Set analysis and Bayes resolution |
| `task3.py`         | Generates final IF-THEN rules                    |
| `medical_data.csv` | Structured medical dataset                       |
| `rules.txt`        | Stores generated rules                           |
| `README.md`        | Project documentation                            |

---

## 🔄 Project Workflow

```text
Medical Paragraph
       ↓
   Task 1
       ↓
medical_data.csv
       ↓
   Task 2
       ↓
Rough Set Analysis
       ↓
Core Attributes
       ↓
Ambiguous Cases
       ↓
Bayes Theorem
       ↓
   Task 3
       ↓
IF-THEN Rules
       ↓
   Task 4
       ↓
Complete Integrated Project
```

---

# 📝 Task 1 – Data Extraction

Task 1 takes a medical paragraph as input and extracts relevant attributes.

### Attributes used

* Age
* BMI
* Glucose
* Family History
* Activity
* Diabetes

The extracted information is stored in:

```text
medical_data.csv
```

Example:

```csv
Age,BMI,Glucose,Family_History,Activity,Diabetes
52,High,High,Yes,Low,Yes
52,High,High,Yes,High,No
29,Normal,High,Yes,High,Yes
```

---

# 🔍 Task 2 – Knowledge Discovery

Task 2 reads the CSV file and applies **Rough Set Theory**.

### Main steps

1. Create equivalence classes.
2. Identify the positive region.
3. Calculate the dependency degree.
4. Find the core attributes.
5. Identify ambiguous equivalence classes.
6. Use Bayes Theorem to resolve ambiguity.

### Core attributes obtained

```text
Age
BMI
Glucose
Activity
```

`Family_History` was found to be dispensable for the current dataset.

### Example

An equivalence class may contain:

```text
Age = 52
BMI = Normal
Glucose = Normal
Activity = Low

Decisions = [Yes, No]
```

Since both decisions occur for the same conditions, the class is **ambiguous**.

Bayes Theorem is then used to select the most likely decision.

---

# 📐 Task 3 – Rule Generation

Task 3 uses the core attributes and resolved decisions to generate IF-THEN rules.

Example:

```text
IF Age = 52 AND BMI = High AND Glucose = High AND Activity = Low
THEN Diabetes = Yes
```

Another example:

```text
IF Age = 52 AND BMI = High AND Glucose = High AND Activity = High
THEN Diabetes = No
```

The generated rules form the final knowledge base.

---

# 🔗 Task 4 – Integration

Task 4 combines the complete project.

The user provides the medical paragraph once, and the system performs the following:

```text
Input Paragraph
       ↓
Extract Data
       ↓
Create CSV
       ↓
Rough Set Analysis
       ↓
Find Core
       ↓
Resolve Ambiguity
       ↓
Generate Rules
       ↓
Final Knowledge Base
```

This makes the complete process automatic instead of running each task separately.

---

# 🧠 Techniques Used

### Rough Set Theory

Used to:

* Create equivalence classes
* Find the positive region
* Calculate dependency
* Identify core attributes
* Detect ambiguity

### Bayes Theorem

Used when an equivalence class contains conflicting decisions.

It calculates the probability of each possible decision and selects the decision with the highest posterior probability.

### Rule Generation

The discovered knowledge is converted into simple:

```text
IF condition
THEN decision
```

rules.

---

# 📊 Current Results

For the current dataset:

```text
Original dependency: 0.5
```

Core attributes:

```text
['Age', 'BMI', 'Glucose', 'Activity']
```

Number of ambiguous classes:

```text
3
```

The ambiguous cases were resolved using Bayes Theorem.

The final system generated **9 decision rules**.

---

# 💻 Requirements

The project uses basic Python libraries.

```text
Python 3.x
```

Main libraries used:

```python
csv
collections
```

No external machine-learning framework is required.

---

# ▶️ How to Run

Clone or download the project and open the project folder in the terminal.

Run the integrated program:

```bash
python main.py
```

Alternatively, individual tasks can be executed separately:

```bash
python task1.py
python task2.py
python task3.py
```

---

# 📌 Example Final Rule

```text
IF Age = 52 AND BMI = High AND Glucose = High AND Activity = Low
THEN Diabetes = Yes
```

This demonstrates how the project converts raw medical information into an understandable decision rule.

---

# 🚀 Future Improvements

The project can be extended by:

* Supporting more medical attributes
* Handling more types of medical data
* Improving automatic attribute extraction
* Generating rules automatically for new datasets
* Adding a user interface
* Testing the rules on new patient records

---

## 👥 Project Contributions

The project is divided into four tasks:

* **Task 1:** Data extraction and CSV generation
* **Task 2:** Rough Set Theory and Bayes Theorem
* **Task 3:** Rule generation
* **Task 4:** Integration of all tasks

---

## 📜 Conclusion

This project demonstrates how unstructured medical information can be transformed into structured data, analyzed to discover important attributes, resolved when ambiguity occurs, and converted into simple decision rules.

The final output provides an understandable knowledge base that can be used for medical decision analysis.
