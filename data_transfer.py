import pandas as pd
import warnings

# Open data base using pandas data frame.
filename = "employee_database/employees_database.csv"
df = pd.read_csv(filename)

# Scanning barcodes and adding them to a new file.
scans = []
active = True
while active:
    scan = input("Scan employee's barcode and it will be added to the list:")
    scans.append(scan)
    continue_scanning_prompt = input("Would you like to add another employee? (Y/N):")
    if continue_scanning_prompt.title() == 'Y':
        continue
    elif continue_scanning_prompt.title() == 'N':
        print("These employees have been added to the training session:\n")

        # Linking scanned barcode to employee name
        for scan in scans:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                name = df.at[df['BARCODE'].eq(scan).idxmax(), 'NAME']
                print(f"Retrieving {scan}...")
                print(f"{scan}, {name.title()}")
        active = False

barcodes = open(r'barcodes/barcodes.txt', 'w')

for scan in scans:
    barcodes.write(scan)


# Assigning training to each employee.


def assign_training():
    """Asks for input of training type and confirms with user.
     Also adds training to each employee in the data frame."""
    training = input("What type of training?:")
    training_confirm = input(f"You want add '{training}'? (Y/N):")
    if training_confirm.upper() == 'Y':
        for index, row in df.iterrows():
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
df.to_csv(r'employee_database\employees_database.csv', index=False)
