import csv
import sys
from collections import defaultdict

''' 
Parse csv file and return 'cookie_dict' dictionary with 'cookie' as keys and 'timestamps' as a list of values
'''
with open('cookie_log.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    date_input = sys.argv[len(sys.argv) - 1]
    cookie_dict = defaultdict(list)
    for row in csv_reader:
        cookie_dict[row["cookie"]].append(row["timestamp"])


''' 
A method that takes in cookie_dict and returns a new dictionary 'new_cookie_dict' with its values being the 
# of times the input_date has been read. This enables an easy loop to organize cookies with set timestamps.
'''
def counter(input_dict, date):
    new_cookie_dict = {}
    for cookie, dates in input_dict.items():
        date_count = 0
        for date in dates:
            if date[0:10] == date_input:
                date_count += 1
        new_cookie_dict[cookie] = date_count
    return new_cookie_dict

'''
Find max value within values to see if any duplicates exist and loop to print each cookie. 
Will return all cookies if no cookies with input date exists.
'''
cookie_value_dict = (counter(cookie_dict, date_input))
max_cookie_value = max(cookie_value_dict.items(), key=lambda x : x[1])

for key, value in cookie_value_dict.items():
    if value == max_cookie_value[1]:
        print(key)


