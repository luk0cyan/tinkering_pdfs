#!/usr/bin/env python3
import re
import pathlib

from .datatojson import getDictionary
#.datatojson works when imported otherwise "." has to be removed for local testing



def simplify_data(string) -> list:
    raw: str = string.split(f" {int}")
    form: str = re.findall("\\d*\D+", str(raw)) #
    formed = str(form).replace(",", "\n") 

    return formed.splitlines()

def indexes_reform(data: list, start_point: int, end_point: int) -> list:
    """
    Replaces the first index lower than 10 with spaces needed
    to keep the same format inside the file
    """
    for line in range(start_point, end_point):
        if int(data[line][2:4]) < 10:
            data[line] = data[line].replace(data[line][2:4], data[line][2:4] + " " )
    else:
        pass

    return data

def type_reform(datas: list, start_point: int, end_point: int, divider_len = 9) -> list:
        """
            Looks for type inside string and replace the same data with spaces - len of item!
            If no item present spaces will be implemented as specified input len 
            !! note: divider_len shouldnt be lower than 6 !!
        """
        cache = []
        result = []
        path = pathlib.Path().parent.resolve()
        waste_type_dictionary: str = getDictionary(path, "waste_type.json")
        legend_types: str = waste_type_dictionary.get("template")

        datas[end_point -1] = f"{str(datas[end_point - 1]).replace(legend_types, "")}"

        for num in range(start_point, end_point):
            found = False
            for index, item in enumerate(waste_type_dictionary):
                if item in datas[num][4:40] and len(cache) == 0:
                    found = True
                    #Using cache to append the 2 values if more than one is found
                    cache = item
                    difference = len(item) -1
                    divider_no_item: int = divider_len - difference
                    datas[num] = f"{datas[num][:7]} {item}{divider_no_item * ' '}{datas[num][7:].replace(item, "")}"

                    break
            if not found:
                datas[num] = f"{datas[num][:7]} {divider_len * " "} {datas[num][8:]}"

            cache = ""
            
        for numba in range(start_point, end_point):
            result.append(datas[numba])
        return result

if __name__=='__main__':
    #In order to run it trough file without import .datatojson has to become
    data = [" '1  Tu UO Tonawanda Del-Ton Plaza Astoria Ditmars '", " '3  Th S Queens Steinway St '"]
    t = type_reform(data, 0, len(data), 9)
    print(f"{t}\n")
    print("Outside main!, File run from path ")