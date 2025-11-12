#!/usr/bin/env python3
#import os

def getMonthData(list) -> list:
    """
    Simple function iterates trough the list data to check
    for unwanted characters and cleans the strings.
    """
    new_list = []
    for index, item in enumerate(list):
        #Extracting the data from the pdf as strings formatted
        for y in range(len(list)):
            #Cleaning the lines from unwanted characters
            new_list.append(list[y].replace("\\n", " ").replace("\\", ""))
        
        return new_list
    
if __name__=='__main__':
    getMonthData()
    print("Outside main!, File run from path ")