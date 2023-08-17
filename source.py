import os # Used to make a directory and a file :)
from openpyxl import Workbook, load_workbook # Used to manage values in excel sheet # https://openpyxl.readthedocs.io/en/stable/index.html
path = os.path.join(os.path.expanduser('~') + "/Documents/","Savings-Docs") #stores values locally for security
file_path = path + "/savings-log.xlsx"

# Create the file directory if it does not exist
# and create the file with user provided values
def create_new():
    
    try:
        os.mkdir(path)
        print("Creating new directory...")
    except OSError as error:
        print("Accessing existing directory...")

    if not os.path.exists(file_path):
        print("Creating new file...")
        wb = Workbook()
        ws = wb.active
        ws['B1'] = "Amount ($)"
        ws['C1'] = "Locked?"
        ws['A2'] = "Total Balance"
        ws['B2'] = float(input("What is your total balance? "))
        ws['C2'] = "false"
        ws['A3'] = "Unaccounted Funds"
        ws['B3'] = ws['B2'].value
        ws['C3'] = "false"
        ws['A4'] = "Num of Categories"
        ws['B4'] = int(input("How many savings categories would you like to have? "))
        ws['C4'] = "false"
        
        for i in range(1,ws['B4'].value + 1):
            if i%10 == 1:
                cat = str(input("What would you like to name your " + str(i) + "st category? "))
            elif i%10 == 2:
                cat = str(input("What would you like to name your " + str(i) + "nd category? "))
            elif i%10 == 3:
                cat = str(input("What would you like to name your " + str(i) + "rd category? "))
            else:
                cat = str(input("What would you like to name your " + str(i) + "th category? "))

            locked = str(input("Is this cell locked? y/n (Exlcuded from fund redistribution feature) "))
            if locked == 'y':
                locked = "true"
            elif locked == 'n':
                locked = "false"
            
            ws['A' + str(5 + i)] = cat
            ws['B' + str(5 + i)] = 0
            ws['C' + str(5 + i)] = locked
        
        wb.save(file_path) 
        print("File creation successful...")  
        
