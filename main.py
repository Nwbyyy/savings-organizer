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

wb.save(file_path) 