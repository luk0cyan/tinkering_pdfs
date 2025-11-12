#!/usr/bin/env python3
import os
import pathlib

def check_files(year: any, month: str) -> str:
    """
    Looks inside folder if month file present,
    otherwise is made returning the filename.
    """
    path = f"{pathlib.Path().parent.resolve()}\\{year}"
    filename: str = f"{year}_{month}.txt"
    directory = os.listdir(path)

    if filename in directory:
        #Checks for presents of file in directoryS
        try:
            open(f"{path}\\{filename}", "w").close()
            return filename

        except FileNotFoundError:
            print(f"Something is wrong, check Folder in directory.")
    
    return filename

def write_to_file(data: list, year: int, file_name: str) -> str:
    """
    By given data as list and filename requirements,
    if file exists gets populated by each line in list,
    returning the filename wich has been populated.
    """
    path_filename = f"{pathlib.Path().parent.resolve()}\\{year}\\{file_name}"
    path = f"{pathlib.Path().parent.resolve()}\\{year}"
    directory = os.listdir(path)
    try:
        with open(path_filename, "a+", encoding="utf-8") as file:
                for index, line in enumerate(data):  
                    file.write(f"{line}\n")

    except Exception as e:
        print(e)

    return f"{file_name} populated!"

if __name__=='__main__':
    check_files()
    write_to_file()
    print("Outside main!, File run from path ")