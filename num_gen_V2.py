#imports

import re
import itertools
import csv
import random
import string
import time


#Global variables and Preparations

sequence = input("Enter a number sequence like 12x456x78 in which 'x's are the unknown numbers: ").lower()

sep = ''
out_list = []
b = []
out = []
extension = ''
fieldnames = [
    "Name", "Given Name", "Additional Name", "Family Name", "Yomi Name",
    "Given Name Yomi", "Additional Name Yomi", "Family Name Yomi",
    "Name Prefix", "Name Suffix", "Initials", "Nickname", "Short Name",
    "Maiden Name", "File As", "Birthday", "Gender", "Location",
    "Billing Information", "Directory Server", "Mileage", "Occupation",
    "Hobby", "Sensitivity", "Priority", "Subject", "Notes", "Language",
    "Photo", "Group Membership", "Phone 1 - Type", "Phone 1 - Value",
    "Phone 2 - Type", "Phone 2 - Value", "Phone 3 - Type", "Phone 3 - Value",
    "Organization 1 - Type", "Organization 1 - Name", "Organization 1 - Yomi Name",
    "Organization 1 - Title", "Organization 1 - Department", "Organization 1 - Symbol",
    "Organization 1 - Location", "Organization 1 - Job Description"
]


#Functions

def count_consecutive_xs(input_string):
    # Split the input string into groups of 'x' characters
    groups = re.findall(r'(x+|\W+)', input_string)
    
    # For each group, count the number of 'x' characters
    counts = [group.count('x') for group in groups if group.strip('x') == '']
    
    return counts


def consecutive(digits, character):
    rang = ""
    for zero in range(digits):
        rang += character
    return rang


def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def ask_ext():
    a = input("Output file format? (T=txt C=Google CSV): ").lower()
    return a


def main():
    if extension == 't':
        file = open('output.txt', 'w')
    else:
        csvfile = open('output.csv', 'w', newline='')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    for mid_num in range(int(consecutive(x_len, "9")) + 1):
        digits = x_len - len(str(mid_num))
        generated_numbers = str(mid_num)
        if digits > 0:
            generated_numbers = consecutive(digits, "0") + str(mid_num)
        x_numbers = list(generated_numbers)
        it = iter(x_numbers)
        some_list = [[next(it) for _ in range(size)] for size in x_group]
        for x in range(len(some_list)):
            b.append(sep.join(some_list[x]))
        if x_at_start:
            if(len(numbers)>len(b)):
                for i in range(len(numbers)):
                    out_list.append(numbers[i])
                    if(len(b)>i):
                        out_list.append(b[i])
            else:
                for i in range(len(b)):
                    out_list.append(b[i])
                    if(len(numbers)>i):
                        out_list.append(numbers[i])
        else:
            if(len(b)>len(numbers)):
                for i in range(len(b)):
                    out_list.append(b[i])
                    if(len(numbers)>i):
                        out_list.append(numbers[i])
            else:
                for i in range(len(numbers)):
                    out_list.append(numbers[i])
                    if(len(b)>i):
                        out_list.append(b[i])
        out.append(sep.join(out_list))
        print(out)
        if extension == 't':
            file.write(out[0]+"\n")
        else:
            row = {field: '' for field in fieldnames}
            row['Name'] = generate_random_name(10)
            row['Given Name'] = row['Name']
            row['Group Membership'] = '* myContacts'
            row['Phone 1 - Type'] = 'Mobile'
            row['Phone 1 - Value'] = out[0]
            writer.writerow(row)
        b.clear()
        out_list.clear()
        out.clear()


#Main

if sequence[0] == 'x':
    x_at_start = True
else:
    x_at_start = False

numbers = sequence.split('x')
numbers[:] = [x for x in numbers if x]

x_group = count_consecutive_xs(sequence)

x_len = sum(x_group)

while True:
    extension = ask_ext()
    if extension == 'c' or extension == 't':
        break
    
main()


print("File created! The script will close now")
time.sleep(5)
