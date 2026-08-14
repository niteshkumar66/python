from pathlib import Path 

def read_file_and_folder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def create_file():
    try : 
        read_file_and_folder()
        name = input("Please tell your file name : ")
        p = Path(name)
        if not p.exists():
            with open(p , "w") as fs :
                data = input("What you want to write in the file : ")
                fs.write(data)

            print("File Created Successfully !")
        else : 
            print("This file already exists !")

    except Exception as err :
        print(f"An error occured as {err}")



print("1 for creating the file")
print("2 for reading the file")
print("3 for updating the file")
print("4 for deleting the file")

check = int(input("Please tell your response : "))

if check == 1 : 
    create_file()
