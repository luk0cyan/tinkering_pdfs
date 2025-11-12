#!/bin/bash/env python3

import unittest
import locale
import calendar
import pathlib
import os 

from utils.datafrompdf import getMonthData
from utils.files_presence import check_files, write_to_file
from utils.folders_checker import pathfolders
from utils.FORMAT import simplify_data, indexes_reform, type_reform
from utils.monthsdays import splitbydays
from utils.recognitionmonthyear import find_month, find_year

class TestFormat(unittest.TestCase):

    def test_monthData(self):
        """
        Returns raw data into cleaner strings and less unwanted characters 
        """
        data = ['2025\\\\ncollector \\\\nordinary\\\\ncollector \\\\nclothes \\\\ntake a look at page. ']
        
        valid_result = ['2025 collector  ordinary collector  clothes  take a look at page. ']
        
        result = getMonthData(data)
        self.assertEqual(result, valid_result)


    def test_check_files(self):
        """
        Test looks if file exists otherwise will make it.
        """
        data = [2025, "april"]
        valid_result = "2025_april.txt"
        result = check_files(data[0], data[1])
        exam = (result == valid_result)
        self.assertTrue(exam)

    def test_write_to_file(self):
        """
        Test writes data to file if files if exists otherwise throws FileExistsError.
        Files will be created and deleted during the test!        
        """
        year: int = 2030 
        file_name = '2030_april.txt'
        path = f"{pathlib.Path().parent.resolve()}\\{year}"
        os.mkdir(f"{path}")
        open(f"{path}\\{file_name}", "w").close()
        data = ['new', 'random', 'words', 'to', 'fill', 'a', 'unittest', 'case', 'scenario.']
        valid_result = f"2030_april.txt populated!"
        result = write_to_file(data, year, file_name)
        exam = (result == valid_result)
        self.assertTrue(exam)
        
        os.remove(f"{path}\\{file_name}")    
        os.rmdir(path)

    def test_path_folders(self):
        """
        Tests if folder in directory otherwise will make it and delete it to sanitize
        """
        path = pathlib.Path().parent.resolve()
        year = "2030"
        valid_result = False
        result = pathfolders(year)
        exam = (result == valid_result)
        self.assertFalse(exam)
        os.rmdir(f"{path}\\{year}")

    def test_simplify_data(self):
        """
        Test that cleans the data from unwanted characters
        """
        data =  "15 Th S Damn street  16 Fr Brooklyn str"
        valid_return = ['["[\'"', " '15 Th S Damn street  '", ' "16 Fr Brooklyn str\']"]']
        result = simplify_data(data)
        self.assertEqual(result, valid_return, "Out put should be the same")

    def test_indexes_reform(self):
        """
        Tests if space get added to the numbers in place lower than 10
        """
        data1 = ['--1','--10','--2','--3','--5','--6','--7','--11']
        valid_return = ['--1 ','--10','--2 ','--3 ','--5 ','--6 ','--7 ','--11']
        result = indexes_reform(data1, 0, len(data1))
        self.assertEqual(result, valid_return, f"It should be right!:{result}")

    def test_typereform(self):
        """
        Checks for type in line and formats it if empty to a specific len
        otherwise subtracts from specific len the len of the type and set       
        in place.
        """
        data = [" '1  Tu UO Tonawanda Del-Ton Plaza Astoria Ditmars '", " '3  Th S Queens Steinway St '"]
        valid_return = [" '1  Tu  UO       Tonawanda Del-Ton Plaza Astoria Ditmars '", " '3  Th  S        Queens Steinway St '"]
        #divider len value if not set correctly can fail test!
        result = type_reform(data, 0, len(data))
        self.assertEqual(result, valid_return, "Type in line should be replaced")

    def test_splitbydays(self):
        """
        Test iterates trough the lines and finds start point and finish
        in list of first month, and goes for the second month piped to
        the second list, returning in each list 2 elements by start and
        finish. 
        """
        data = ["['april'", " '2025'", " '9 eco'", " '11 '", " '1 Tu '", " '2 We '", " '3 Th '",
             " '4 Fr UO '", " '5 Sa '", " '6 Su '", " '7 Mo '", " '8 Tu UO VR '", " '9 We '",
             " '10 Th '", " '11 Fr '", " '12 Sa '", " '2025 rac'", " '9 eco'", " '11  '",
             " '1 Th '", " '2 Fr '", " '3 Sa '", " '4 Su '", " '5 Mo '", " '6 Tu '", " '7 We '",
             " '8 Th '", " '9 Fr '", " '10 Sa '", " '11 Su  '", " '12 Mo '", ' "18\']"]']
        valid_return = [4, 16], [19, 31]
        result = splitbydays(data)
        self.assertEqual(result, valid_return, "The lists should contain those values!")

    def test_find_month(self):
        """
        Test returns as list with index 0,1 if months found in list piped lines
        """
        locale.setlocale(locale.LC_ALL, 'en_EN')
        values = [x.lower() for x in list(calendar.month_name)]
        data = ['october', 'returns', 'comments', 'agreements', 'april']
        valid_return = 'october','april'
        result = find_month(data, values)
        self.assertEqual(result, valid_return)

    def test_find_year(self):
        """
        Test returns year if contained in lines as list 
        """
        data = ['nova', 'mini', '2025', 'solar', 'links', 'airy', 'clever', '2026']
        valid_return = ['2025', '2026']
        result = find_year(data)
        self.assertEqual(result, valid_return)

if __name__ == "__main__":
    unittest.main()