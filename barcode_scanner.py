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
    training = input("What type of training?:")
    if training == 'CLEAR':
        while True:
            protection_prompt = input("Are you sure you want to clear all training?(Y/N):")
            if protection_prompt == "Y" or "y":
                for index, row in df.iterrows():
                    df.loc[df.index[index], 'TRAINING'] = "None"
                break
            elif protection_prompt == "N" or "n":
                assign_training()
            else:
                print("Please only type Y or N.")
    else:
        for index, row in df.iterrows():
            if 'None' not in df.loc[df.index[index], 'TRAINING']:
                df.loc[df.index[index], 'TRAINING'] += ", " + training
            elif 'None' in df.loc[df.index[index], 'TRAINING']:
                df.loc[df.index[index], 'TRAINING'] = df.loc[df.index[index], 'TRAINING'].replace('None', '')
                df.loc[df.index[index], 'TRAINING'] += training


assign_training()

# Printing new data frame.
print(df)

# Exporting new data frame to original CSV file.
df.to_csv(r'employee_database\employee_database.csv', index=False)
