import pandas as pd
import csv
from tkinter import *

with open('employee_database/employee_database.csv', newline='') as employee_csv:
    reader = csv.DictReader(employee_csv)

    """GUI Setup"""
    # Making the window.
    root = Tk()
    root.title("Barcode Scanner")
    root.geometry('1100x600')
    root.configure(bg='#bfbd92')

    # Making entry widget.
    e = Entry(root, bg='#eeeeee', borderwidth=1)

    temp_employee_dicts = []


    def on_return(*args):
        global temp_employee_dict
        scan = e.get()
        temp_employee_dict = {'BARCODE': scan, 'NAME': ''}
        temp_employee_dicts.append(temp_employee_dict)
        continue_scanning_label = Label(root, text="Would you to add another employee?")
        continue_scanning_label.grid(row=0, column=1)

    e.bind("<Return>", on_return)

    e.pack()


    def no_command():
        print("These employees have been added to the training session:\n")

        # Linking scanned barcode to employee name
        for row in reader:
            for temp_dict in temp_employee_dicts:
                if row['BARCODE'] == temp_dict['BARCODE']:
                    temp_dict['NAME'] = row['NAME']
                else:
                    continue
                print(f"{temp_dict['BARCODE']}, {temp_dict['NAME']}")


    def more_employees():
        prompt = "Do you want to add another employee?"
        prompt_label = Label(root, text=prompt, bg='#bfbd92')
        prompt_label.pack()
        yes_button = Button(root, text="Yes", bg='white')
        no_button = Button(root, text="No", command=no_command, bg='white')
        yes_button.pack()
        no_button.pack()



    # Creating a button widget.
    my_button = Button(root, text="Enter your name", command=more_employees, bg='white')
    my_button.pack()

    # Creating the loop to keep window open and run the GUI.
    root.mainloop()


    """Data Entry Program"""
    # Open data base using pandas data frame.
    filename = "employee_database/employee_database.csv"
    df = pd.read_csv(filename)
    print(df)





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
