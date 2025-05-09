#here we are making a simple project on file handling
import sys
from pathlib import Path as pt 
import os 
def total_file_present():
    path=pt('')
    item=list(path.rglob('*'))
    for i,file in enumerate(item):
        print(f"{i+1}. {file}")
def create():
    total_file_present()
    name=str(input("Enter the Name and exetension of the file you want to create:-"))
    p=pt(name)
    if not p.exists():
        with open(p,'w') as file:
            print("Now you can enter the data you want and to end writting (press ctrl+z and then Press Enter)")
            file.write(sys.stdin.read())
            print("Your File has been successfully created.")
            file.close()
            main()
    else:
        print("File is already created.")
        main()
def update():
    total_file_present()
    name=str(input("Enter the file name:-"))
    p=pt(name)
    if p.exists() and p.is_file():
            with open(p,'r') as file:
                print("\n")
                l=file.read()
                print(l)
                file.close()
            with open(p,'a') as file:
                print("Now you can enter the data you want and to end writting (press ctrl+z and then Press Enter)\n")
                file.write(sys.stdin.read())
                file.close()
    else:
        print("File does not exists.")
def rewrite():
    total_file_present()
    name=str(input("Enter the file name :-"))
    p=pt(name)
    if p.exists() and p.is_file():
        with open(p,'w')  as file:
            print("Now you can enter the data you want and to end writting (press ctrl+z and then Press Enter)\n")
            file.write(sys.stdin.read())
            file.close()
        main()
    else:
        print("File does not found you want to create new file.\nIf you want to create new file press(Y) and press then enter")
        n=str()
        if(n=='Y' or n=='y'):
            create()
        else:
            main()
def delete():
    total_file_present()
    name=str(input("Enter the file name with extension:-"))
    p=pt(name)
    if p.exists() and p.is_file():
        os.remove(p)
        main()
    else:
        print("File does not found.")
        main()
def fileread():
    total_file_present()
    name=str(input("Enter the file name:-"))
    p=pt(name)
    if p.exists() and p.is_file():
            with open(p,'r') as file:
                print("\n")
                l=file.read()
                print(l)
                file.close()
                main()
    else:
        print("File does not exists.")
        main()
def rename():
    total_file_present()
    name=str(input("Enter the file name with extension:-"))
    p=pt(name)
    if p.exists() and p.is_file():
        new=str(input("Enter the new file name with extension:-"))
        p.rename(new)
        main()
    else:
        print("File does not exist.")
        main()
def main():
    print("                                                                               MENU                                                            \n1.Create new file\n2.Update old file\n3.Rewrite Old file\n4.Delete file\n5.Read file\n6.Rename the file\n7.Exit")
    choice=int(input("Enter the choice:-"))
    if(choice==1):
        create()
    elif(choice==2):
        update()
    elif(choice==3):
        rewrite()
    elif(choice==4):
        delete()
    elif(choice==5):
        fileread()
    elif(choice==6):
        rename()
    else:
        exit()
main()