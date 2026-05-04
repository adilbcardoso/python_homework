

#Task2
import csv
import sys

def read_employees ():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
            data["rows"] = rows
    
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)

    return data

employees = read_employees()


print(employees)

#Task3
def column_index(column_header):
   return employees["fields"].index(column_header)

print(column_index("last_name"))

employee_id_column = column_index("employee_id")

print(employee_id_column)


#Task4

def first_name(row_number):
    first_name_col = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_col]

print(first_name(2))
print("INDEX first_name:", column_index("first_name"))
print("ROW:", employees["rows"][2])

#task5

def employee_find(integer):
    def employee_match(row):
      return int(row[employee_id_column]) == integer
    
    matches=list(filter(employee_match, employees["rows"]))

    return matches
    
print(employee_find(3))


#Task6

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

print(employee_find_2(4))

#Task7

def sort_by_last_name():
    last_name_index = column_index("last_name")

    employees["rows"].sort(key=lambda row: row[last_name_index])

    return employees["rows"]

print(f'a:',sort_by_last_name())


#Task8

def employee_dict(row):
    keys = employees["fields"][1:]
    values = row[1:]
    return dict(zip(keys, values))


print(employee_dict(employees["rows"][1]))

#Task9

def all_employees_dict():
    result_dict = {}
    for row in employees["rows"]:
        keys = row[employee_id_column]
        result_dict[keys] = employee_dict(row)

    return result_dict

print(all_employees_dict())





#task10

import os

def get_this_value():
    return os.getenv("THISVALUE")


print(get_this_value())


#Task11
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)



set_that_secret("love")

print(custom_module.secret)


#Task12
def read_minutes1(path):
    data = {}
    rows = []

    try:
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row

                else: 
                    rows.append(tuple(row))

        data["rows"] = rows
        return data 
    
    except Exception as e:
        print("Error readimg file:", path)
        print(e)
        sys.exit(1)


def read_minutes():
    minutes1 = read_minutes1("../csv/minutes1.csv")
    minutes2= read_minutes1("../csv/minutes2.csv")
    return minutes1, minutes2
    

minutes1, minutes2 = read_minutes() 
print(read_minutes())

#Task13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"]) 
    return set1.union(set2)

minutes_set = create_minutes_set()

print(minutes_set)

#Task14

from datetime import datetime 

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted = list( map (lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    return converted

minutes_list = create_minutes_list()
print(minutes_list) 

#Task15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    convert_sort_minutes_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list ))

    with open("./minutes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(convert_sort_minutes_list)
    return convert_sort_minutes_list

sorted_minutes = write_sorted_list()

print(sorted_minutes)


#pytest -v -x assignment2-test.py


    






