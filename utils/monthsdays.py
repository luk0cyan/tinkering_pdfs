#!/usr/bin/env python3

def splitbydays(list) -> list:
    """
        Function returns 2 list with 2 values each
        containing the start and end of the month days
        wich can be iterated trough the data given
    """
    #Indexes are added inside the list as element[0] first index, element[1] second index
    indexes_first = []
    indexes_second = []
    cache = ''
    #Iterating trough the full list 
    for index, data in enumerate(list):
        #Looking for the 1st day inside the indexes of the list 
        if "1 " in data[2:4]:  
            indexes_first.append(index)
    
    #Iterating trough th first list days
    for nums in range(indexes_first[0], indexes_first[1]):
        indexes_second.append(indexes_first[1])
        pass

        if int(list[nums][2:4]) == int(list[nums-1][2:4])+1:
            #updated second index of first list with last number of the month founded
            indexes_first[1] = list.index(list[nums]) + 1
        else:
            pass

    indexes_second = [indexes_second[0], indexes_second[1]]
    #Iterating through the second list day 
    for tnums in range(indexes_second[0], len(list)):

        if int(list[tnums][2:4]) == int(list[tnums-1][2:4])+1:
            cache = list.index(list[tnums]) + 1
          
        continue
    indexes_second[1] = cache
    return indexes_first ,indexes_second  

if __name__=="__main__":
    #Example to to run on file 
    exmpl = ["['april'", " '2025'", " '9 eco'", " '11 '", " '1 Tu '", " '2 We '", " '3 Th '",
             " '4 Fr UO '", " '5 Sa '", " '6 Su '", " '7 Mo '", " '8 Tu UO VR '", " '9 We '",
             " '10 Th '", " '11 Fr '", " '12 Sa '", " '2025 rac'", " '9 eco'", " '11  '",
             " '1 Th '", " '2 Fr '", " '3 Sa '", " '4 Su '", " '5 Mo '", " '6 Tu '", " '7 We '",
             " '8 Th '", " '9 Fr '", " '10 Sa '", " '11 Su  '", " '12 Mo '", ' "18\']"]']

    n, m = splitbydays(exmpl)
    print("working on file")