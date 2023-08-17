import os #file path "C:\Program Files\Savings-Docs"

path = os.path.join("C:/Program Files/","Savings-Docs")

try:
    os.mkdir(path)
    print("Creating mnew directory...")
except OSError as error:
    print("Accessing existing directory...")

print(path)