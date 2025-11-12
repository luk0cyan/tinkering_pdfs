#!/usr/bin/env python3
from datetime import datetime
import re

def find_month(data: list, values: list) ->list:
    """
        Function checks for value in list and returns it as list with 
        first file value in index 0
        second file value at index 1
    """
    result = []
    num = 0
    for val in values:
        for line in data:
            if val in line:
                #Without checking the len of the value ends up adding useless data
                if len(val) == 0:
                    pass

                elif val not in result:
                    num += 1
                    result.append(val)
            else:
                pass

    return result[1], result[0]

def find_year(data: list) -> list:
    """
        Looks for year(present or past) inside lines of data parsed
        as list, giving the result as list.
    """
    result = []
    present_year = datetime.now().year
    years = [present_year-1, present_year, present_year+1]
    for year in years:
        for line in data:
            if str(year) in line:
                result.append(str(year))
    return result

if __name__=='__main__':
    exmpl = ['nova', 'mini', '2025', 'solar', 'links', 'airy', 'clever', '2026']
    result = find_year(exmpl)
    print(result)
    print("Outside main!, File run from path ")