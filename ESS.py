#!/usr/bin/env python3

# Import to check dates
from dateutil.parser import parse

#==============================
#  Colors 
#==============================
# colored text
reset='\033[0m'
bold='\033[01m'
underline='\033[04m'
red='\033[31m'
green='\033[32m'
yellow='\033[93m'

#==============================
#  Exception Class
#==============================

class ExamException(Exception):
    pass

#==============================
#  CSVTimeSeriesFile Class
#==============================

class CSVTimeSeriesFile:
    '''Class that can read a time series related to passengers on         an airline.
    And that can compute the average variance for every month'''

    # Constructor that takes in the name of the file
    def __init__(self, name):

        # If name is not a string raise generate an error and get back to main 
        if not isinstance(name, str):
            raise ExamException(f'{bold}{red} Error: parameter "name" must be a string, not "{type(name)}"')

        # Set the name 
        self.name = name

    # I need this to check if the string is a date
    def is_date(self,string):
        """
        Return whether the string can be interpreted as a date.
        :param string: str, string to check for date
        """
        try:
            parse(string)
            return True

        except ValueError:
            return False

    # Function that returns lists of lists which date and passengers number
    def get_data(self):

        # Initialise an empty list to save all of the values
        complete_list = []

        # I try to open the file and get the data if it fails I raise and exception and abort. 
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            raise ExamException(f'{red}{bold}Error occurred when reading the file: "{e}"{reset}')

        # If I can open the file I start to read line by line 
        for line in my_file:

            elements = line.split(',')
            # I skip the first element which is the heading
            if elements[0] != 'date':

                # I set the date and the value
                try:
                    date = str(elements[0])

                    # Check if the date doesn't makes sens as a date , using the helper function that I have added to the class
                    if not self.is_date(date):
                        # Run if the output of is_date is False thus that is not a date, don't save the value and go to the next loop
                        continue

                    # If the element is a float pass to the next one and ignore it
                    try:
                        # Make the value an integer if it is not don't accept it 
                        value = int(elements[1])
                    except ValueError:
                        continue

                    # If value is a negative number don't accept it and continue,
                    if value < 0:
                        continue
                except:
                    # If other error occur go to the next loop without saving those data 
                    continue

                # Check if the timestamps is a duplicate of any of the preview timestamps saved
                if len(complete_list) > 0:
                    # Loop through the preview timestamps 
                    for item in complete_list:
                        # Save the data value on the previews timestamp
                        prev_date = item[0]
                        if date == prev_date:
                            raise ExamException(f'{bold}{red}Timestamp is a duplicate.{reset}')

                    # Check if the timestamp follow the one before
                    prev_date = complete_list[-1][0]
                    if date < prev_date:
                        raise ExamException(f'{bold}{red}Timestamp is not ordered.{reset}')

                # I append the date and value lists to the main list for every step
                complete_list.append([date,value])

        # Close the file
        my_file.close()

        # If the file is empty 
        if not complete_list:
            raise ExamException(f'{bold}{red}File is empty{reset}')

        return complete_list
