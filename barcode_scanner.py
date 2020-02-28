import pandas as pd

"""Enter training to barcode data."""

# Scanning barcodes of every person in training session.
f = open("barcodes/demo.txt", "r")
barcodes = []
for line in f:
    barcodes.append(line)
f.close()

filename = "employee_database/employees_database.csv"
df = pd.read_csv(filename)

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
