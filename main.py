from source import *

try:
    wb = load_workbook(filename = file_path)
    ws = wb['Sheet']
    deposit(ws)
    withdrawl(ws)
except  FileNotFoundError as error:
    create_new()
    wb = load_workbook(filename = file_path)
    ws = wb['Sheet']

allocate_funds(ws)


#print("What actions would you like to take?")
#ans = input("1. Automatically Redistribute Funds\n2. Manually Redistribute Funds\n")


wb.save(file_path) 