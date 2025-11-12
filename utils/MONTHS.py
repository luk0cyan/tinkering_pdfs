#!/usr/bin/env python3
import locale
import calendar

def month_available() ->  list:
    #Config file has to be set in order to be able to choose different Location/language
    """
        Function used to obtain a list of available months in the specified language/location.
    """
    locale.setlocale(locale.LC_ALL, "en_EN") 
    datas = [x.lower() for x in list(calendar.month_name)]
    result = []

    for data in datas:
        result.append(data)
    return result 

if __name__=='__main__':
    month_available("may")
    print("Outside main!, File run from path ")