##
## Mouhamadou Niang PROJECT, 2022
## function for data list
## File description:
## function for data list
##

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
    print("   On the following `N` lines: the correction time of the 3 copies of each partici\
pant, separated by a space\n\n")
    print("Return :")
    print(" - False` if one of the juries cannot finish on time\n - True' if all juries can f\
inish on time")
