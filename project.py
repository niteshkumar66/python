from pathlib import Path 
import os

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


def read_file():
    try:
        read_file_and_folder()
        name = input("which file you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open (p , "r") as fs :
                data = fs.read()
                print(data)

            print("File Readed Successfully")

        else : 
            print("The file is not exist")

    except:
        print(f"The error is occured as {err}")


def update_file():
    try:
        read_file_and_folder()
        name = input("Tell which file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")

            respone = int (input("Tell your response : "))

            if respone == 1 :
                name2 = input(f"Tell the new file to rename the {name} file")
                p2 = Path(name2)
                p.rename(p2)


            if respone == 2 :
                with open(p, "w") as fs : 
                    data = input("Tell the new content you want to overwrite : ")
                    fs.write(data)
                    

            if respone == 3 :
                with open(p, "a") as fs : 
                    data = input("Tell the new content you want to appned : ")
                    fs.write(" " + data)

    except Exception as err :
        print(f"An error occured as {err}")


def delete_file():
    try:
        read_file_and_folder()
        name = input("Which file you want to delete : ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove()

            print("File Deleted Successfully ")

        else : 
            print("No such file exists ")

    except Exception as err:
        print(f"An error occured as {err}")
            
        

print("1 for creating the file")
print("2 for reading the file")
print("3 for updating the file")
print("4 for deleting the file")

check = int(input("Please tell your response : "))

if check == 1 : 
    create_file()

if check == 2 :
    read_file()

if check == 3 :
    update_file()

if check == 4:
    delete_file()
