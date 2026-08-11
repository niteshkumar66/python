from pathlib import Path 

def readfile_and_folder():
    path = Path('') 
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items} ")

def createfile():
    try : 
        readfile_and_folder()
        name = input("Please tell your file name : ")
        p = Path(name)
        with open(p,"w") as fs:
            data = input("what do you want to write in the file :  ")
            fs.write(data)

        print("File Created Successfully")

    except Exception as err: 
        print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please Tell your Response : "))

if check == 1 : 
    createfile()