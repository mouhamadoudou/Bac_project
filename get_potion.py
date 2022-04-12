#!/usr/bin/env python3
##
## Mouhamadou Niang, 2022
## project_main.py
## File description:
## main file
##

import sys

def get_time(av):
    data = av[0].split()
    return (data)

def get_student(av):
    data = []
    data.append(av[1])
    if int(data[0]) == 0:
        print("True")
        return 0
    return (data)

def get_file(av):
    doc_file = open(av, "r")
    result = doc_file.read()
    doc_file.close()
    data = result.split("\n")
    data.append(None)
    return (data)

def get_col(av, nb_col):
    result = []
    result2 = []
    data = []
    i = 2
    a = 0

    while av[i + 1] != None:
        result = av[i].split(" ")
        result2.append(result)
        data.append(result2[a][nb_col])
        a += 1
        i += 1
    data.append(None)
    return (data)

def get_list(data_str):
    all_col = []

    all_col.append(get_col(data_str, 0))
    all_col.append(get_col(data_str, 1))
    all_col.append(get_col(data_str, 2))
    return (all_col)

def display_flag_h():
    print("USAGE")
    print("   ./get_potion\n")
    print("A TEXT FILE MUST COMPOSED :")
    print("   The first line: the time in minutes given to each jury, separated by a space")
    print("   On the seconde line: the number of `N` participants in the BAC")
    print("   On the following `N` lines: the correction time of the 3 copies of each participant, separated by a space\n\n")
    print("Return :")
    print(" - False` if one of the juries cannot finish on time\n - True' if all juries can finish on time")

def function_calc(data_l, data_time, nb_student):
    result = 0
    i = 0
    a = 0

    while data_l[i] != None:
        a = int(data_l[i])
        result = result + a
        i += 1
    if result <= int(data_time):
        return (0)
    return (-1)
    
def start_analys(list_data, data_time, nb_student):
    res = 0
    check1 = function_calc(list_data[0],data_time[0], nb_student)
    check2 = function_calc(list_data[1],data_time[1], nb_student)
    check3 = function_calc(list_data[2],data_time[2], nb_student)
    res = check1 + check2 + check3

    if res == 0:
        print("True")
    else:
        print("False")
    
def main_start(arg):

    data_str = get_file(arg)
    data_time = get_time(data_str)
    nb_student = get_student(data_str)
    if nb_student == 0:
        return (0)
    data_list_res = get_list(data_str)

    start_analys(data_list_res, data_time, nb_student)
    
def main():
    argc = len(sys.argv)
    i = 1

    if argc == 2:
        if (sys.argv[1][0] == '-' and sys.argv[1][1] == 'h' and len(sys.argv[1]) == 2):
            display_flag_h()
            sys.exit(0)
    while i < argc:
        main_start(sys.argv[i])
        i += 1
    sys.exit(0)

if __name__ == '__main__':
    main()
