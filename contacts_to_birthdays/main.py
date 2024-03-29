#!/usr/bin/python3
"""This is a Python tool that converts an .vcf and .html from Instagram export to table where birthdays can be put
in.
Then it can be converted to a calendar.
It uses the following modules: bs4 for HTML scraping ics for generating
an ics calendar pandas for reading xlsx files xlwt for writing xlsx files datetime for date and time operations The
main function in this code is main().
The main() function checks the command line arguments and calls other functions
based on the arguments.
The get_names_from_vcf(file) function reads a vcf file and returns a list of names from the
file.
The get_names_from_insta(file) function reads a html file from Instagram export and returns a list of names
from the file.
The generate_xlsx_file(names) function takes a list of names as input and generates an Excel sheet
from it.
The create_calendar(file_path) function reads data from an Excel sheet, creates events for birthdays and
saves the calendar in ics format.
It is assumed that the functions get_names_from_vcf(file), get_names_from_insta(
file), generate_xlsx_file(names) and create_calendar(file_path) are defined and have the necessary functionality.
The
--convert flag converts .vcf and .html to table the --to_calendar flag converts .xlsx to ics calendar"""
import datetime
import sys
from datetime import datetime

import pandas as pd
import xlwt
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
from ics import Calendar, Event


def get_names_from_vcf(file: str):
    """
  file: str
  This function is reading all contacts from simple contacts app .vcf format and converts are as an array
  """
    names = []  # array
    readLines = open(file).readlines()  # convert it to line arrays
    for line in readLines:
        if line.find("FN") > -1:  # found fn in .vcr fn means begin string where username is writen
            name = (line.replace("FN:", ""))  # remove FN: header
            if name != "":  # check is name not empty
                names.append(name.rstrip())  # append to array and strip name to delete all grabbed such next lines etc
    return names  # return value


def get_names_from_insta(file: str):
    """
    file: str
    This function is reading .html file from insta export and gets and names.
    """
    names = []  # array
    file = open(file).read()  # open file, but not as array
    soup = BeautifulSoup(file, 'html.parser')  # make bs4 instance and run html.parser
    blog_titles = soup.findAll('div', attrs={
        "class": "pam _3-95 _2ph- _a6-g uiBoxWhite border"})  # find all div`s with set class`
    for title in blog_titles:  # go through all got dev's`
        names.append(title.text)  # write each one to array
    return names  # return value


def generate_xlsx_file(names, xlsx):
    """
    names: array[]
    this function take an array of names and writes them in .xlsx file
    """
    book = xlwt.Workbook()  # create exel workbook
    sh = book.add_sheet("Дни рождения")  # create a new sheet
    sh.write(0, 0, "Имя или никнейм человека")  # in the first array write what it means
    sh.write(0, 1, "его день рождения")  # in second array write a what it means
    counter = 0  # make counter
    for name in names:  # go through all names in the list
        sh.write(counter + 1, 0, name)  # write in Excel table
        counter = counter + 1  # update counter
    book.save(xlsx)  # save Excel file


pass


def create_calendar(file_path: str, ics: str) -> None:
    """
    function reads data from an Excel sheet, creates events for birthdays and saves the calendar in ics format.

    :param file_path: path of the Excel sheet ics: path of ics file
    :type file_path: str
    :return: None

    """

    # Initializing the Calendar
    c = Calendar()
    # Loading the workbook
    data_frame = pd.read_excel(file_path)
    # Iterating through the name list
    for a in range(0, len(data_frame['Имя или никнейм человека'])):
        try:
            # Creating a new Event
            e = Event()
            # Assigning the name of the event as "День рождения у <name>"
            e.name = f"День рождения у {data_frame['Имя или никнейм человека'][a]}"
            # Converting the date string to a datetime object
            date_object = datetime.datetime.strptime(data_frame['его день рождения'][a], '%d.%m.%y')
            # Assigning the start and end time of the event
            e.begin = date_object
            e.end = date_object + relativedelta(hours=2)
            # Adding the event to the Calendar
            c.events.add(e)
        except Exception as inst:
            print(inst)

    # Saving the Calendar in ics format
    with open(ics, 'w') as my_file:
        my_file.writelines(c.serialize_iter())


def main():
    """
    Function is the entry point of the program.
    It calls other functions based on the command line arguments
    provided.
    Code snippet is using the sys.argv list to extract command-line arguments that were passed to the
    script.
    Sys.argv[2] is the third argument passed to the script, sys.argv[3] is the fourth argument passed to the
    script.

It then calls two functions get_names_from_vcf(vcr) and get_names_from_insta(html) with the extracted arguments,
these functions may read and parse the contents of the files passed as arguments and extract names from them.

The variable names_vcf will contain a list of names extracted from the file passed as the third argument to the
script.
The variable names_html will contain a list of names extracted from the file passed as the fourth argument to
the script.

Then it concatenates both lists names_vcf and names_html and stores it in variable together

Finally, it uses the set() function to convert together into a set and then back into a list, which will remove any
duplicate names and store the result in the together variable.
  
  """

    if len(sys.argv) < 2:
        print("This program expects the following keys to be provided while running:")
        print("--convert: To convert the contact.vcf and index.html files from resources directory to xlsx file")
        print("--to_calendar: To convert the xlsx file to ics file")
        print("Example usage: python <program_name> --convert contact.vcf index.html contact.xlsx")
        print("or for convert option")
        print("This program expects the following key to be provided while running:")
        print("--to_calendar: To convert the xlsx file to ics file")
        print("Example usage: python <program_name> --to_calendar contact.xlsx")
        sys.exit(0)

    if sys.argv[1] == "--convert":
        print(
            "Put two .vcf file and .html from instagram export and put in in resources dir and call them as "
            "contact.vcf and index.html")
        vcr = sys.argv[2]
        html = sys.argv[3]
        xlsx = sys.argv[4]
        names_vcf = get_names_from_vcf(vcr)
        names_html = get_names_from_insta(html)
        together = names_vcf + names_html
        together = list(set(together))
        generate_xlsx_file(together, xlsx)
    if sys.argv[1] == "--to_calendar":
        file_path = sys.argv[2]
        ics = sys.argv[3]
        create_calendar(file_path, ics)


if __name__ == '__main__':
    main()
