#!/usr/bin/env python3
import argparse

import pathlib
import pypdf

from utils.FORMAT import simplify_data, indexes_reform, type_reform
from utils.MONTHS import month_available
from utils.datafrompdf import getMonthData
from utils.monthsdays import splitbydays
from utils.recognitionmonthyear import find_month, find_year
from utils.folders_checker import pathfolders
from utils.files_presence import check_files, write_to_file

def main(data):

    listings = simplify_data(data)

    months = [x for x in month_available()]
    
    datas = getMonthData(listings)

    name2, name1 = find_month(datas, months)

    first, second = splitbydays(datas)

    year_2, year_1 = find_year(datas)

    #Checking if year folder already present
    #If not folder will be made
    pathfolders(year_1)
    pathfolders(year_2)

    filename1 = check_files(year_1, name1)
    filename2 = check_files(year_2, name2)

    formatted_line_first_file = indexes_reform(datas, first[0], first[1])       
    formatted_line_second_file = indexes_reform(datas, second[0], second[1]) 

    final_file_one = type_reform(formatted_line_first_file, first[0], first[1])
    final_file_two = type_reform(formatted_line_second_file, second[0], second[1])

    write_to_file(final_file_one, year_1, filename1) #final_file_one, year_2, filename2)
    write_to_file(final_file_two, year_2, filename2) #final_file_two, year_1, filename1)

if __name__=="__main__":
    
    path = pathlib.Path(__file__).parent.resolve()
    parser = argparse.ArgumentParser(description="PDF file should contain only pages with the tables")
    parser.add_argument("file_pdf", type=pathlib.Path, help="Path to the PDF file")
    args = parser.parse_args()

    if not args.file_pdf.exists():
        parser.error(f"File not found: {args.file_pdf}")

    with open(args.file_pdf, "rb") as pdf:
        reader = pypdf.PdfReader(pdf)
        available_pages = [x for x in range(reader.get_num_pages())]
        for page in available_pages:
            main(reader.pages[page].extract_text())

