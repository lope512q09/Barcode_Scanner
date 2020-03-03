import pandas as pd
import csv

# Open data base using pandas data frame.
filename = "employee_database/employee_database.csv"
df = pd.read_csv(filename)
print(df)

# Writing lines to dictionaries.
with open('employee_database/employee_database.csv', newline='') as employee_csv:
    reader = csv.DictReader(employee_csv)

    # Scanning barcodes and adding them to a new file.
    scans = []
    temp_employee_dicts = []
    active = True
    while active:
        scan = input("Scan employee's barcode:")
        print("Adding employee to list...")
        scans.append(scan)
        temp_employee_dict = {'BARCODE': scan, 'NAME': ''}
        temp_employee_dicts.append(temp_employee_dict)
        continue_scanning_prompt = input("Would you like to add another employee? (Y/N):")
        if continue_scanning_prompt.title() == 'Y':
            continue
        elif continue_scanning_prompt.title() == 'N':
            print("These employees have been added to the training session:\n")

            # Linking scanned barcode to employee name
            for row in reader:
                for temp_dict in temp_employee_dicts:
                    if row['BARCODE'] == temp_dict['BARCODE']:
                        temp_dict['NAME'] = row['NAME']
                    else:
                        continue
                    print(f"{temp_dict['BARCODE']}, {temp_dict['NAME']}")
            active = False

employee_csv.close()

# Assigning training to each employee.


def assign_training():
    """Asks for input of training type and confirms with user.
     Also adds training to each employee in the data frame based on the barcodes scanned earlier."""
    training = input("What type of training?:")
    training_confirm = input(f"You want add '{training}'? (Y/N):")
    if training_confirm.upper() == 'Y':
        for temp_dict in temp_employee_dicts:
            for index, row in df.iterrows():
                if str(df.loc[df.index[index], 'BARCODE']) == temp_dict['BARCODE']:
                    if 'None' not in df.loc[df.index[index], 'TRAINING']:
                        df.loc[df.index[index], 'TRAINING'] += ", " + training
                    elif 'None' in df.loc[df.index[index], 'TRAINING']:
                        df.loc[df.index[index], 'TRAINING'] = df.loc[df.index[index], 'TRAINING'].replace('None', '')
                        df.loc[df.index[index], 'TRAINING'] += training
    elif training_confirm.upper() == 'N':
        print("Please re-enter the type of training.")
        assign_training()


assign_training()

# Printing new data frame.
print(df)

# Exporting new data frame to original CSV file.
df.to_csv(r'employee_database\employee_database.csv', index=False)
