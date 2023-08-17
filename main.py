import os #file path C:\Users\nixon\Documents\laptop backup.zip"

path = os.path.join(os.path.expanduser('~') + "/Documents/","Savings-Docs")

try:
    os.mkdir(path)
    print("Creating new directory...")
except OSError as error:
    print("Accessing existing directory...")

try:
    open(path + "/savings-log.txt", "x")
    print("Creating new file...")
    log = (path + "/savings-log.txt", "w")
    log.writelines(["Balance: ","Categories: ","Unsorted Funds: "])
except (OSError, IOError) as error:
    print("Accessing existing file...")
    
file_path = path + "/savings-log.txt"