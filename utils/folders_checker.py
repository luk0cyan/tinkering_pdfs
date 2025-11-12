#!/usr/bin/env python3
import os
import pathlib


def pathfolders(year: any) ->bool:
    """
    Called checks the presence of the folder by the name given,
    if not present is made instantly.
    """
    path = pathlib.Path().parent.resolve()
    bool = False
    directory = os.listdir(path)
    try:
        if year in directory:
            #Checks if folder already exists
            bool = True
        else:
            bool = True
            os.mkdir(f"{path}\\{year}")
            print("Folder had to be made!")    
    except Exception as e:
        print(e)
    return bool

if __name__=='__main__':
    pathfolders()
    print("Outside main!, File run from path ")