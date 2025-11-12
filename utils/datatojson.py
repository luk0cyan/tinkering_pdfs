#!/usr/bin/env python3
import os
import json

import pathlib

def getDictionary(path_new: str,filename: str) -> dict:
    """
    Function loads .json file as dictionary ready to be used.
    """
    #Gotta be resolved how to find the path
    path_new = f"{pathlib.Path(__file__).parent.resolve()}"

    if filename in os.listdir(path_new):
        #Dictionary gets loaded if present!
        with open(f"{path_new}\\{filename}", "r") as file:
            data = json.load(file)

    else:
        print("No filename found!")

    return data

if __name__=='__main__':
    #main()
    print("Outside main!, File run from path_new ")