import task1
import task2
import task3


def main():

    print("=" * 60)
    print("MEDICAL DATA ANALYSIS SYSTEM")
    print("=" * 60)

    # TASK 1 
    print("TASK 1: DATA EXTRACTION")

    # Run Task 1 to create medical_data.csv
    task1.create_csv()

    print("Task 1 completed successfully.")
    print("Medical data has been extracted and saved to medical_data.csv")

    # TASK 2 
    print("TASK 2: ROUGH SET & BAYES ANALYSIS")

    task2.run_task2()

    # TASK 3 
    print("TASK 3: RULE GENERATION")

    task3.run_task3()

    print("\n\n" + "=" * 60)
    print("Task 4: All combined")
    print("ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()