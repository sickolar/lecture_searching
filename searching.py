import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
        hod = data.keys()
        for dat in hod:
            if dat == field:
                value = data[field]
                return value
        return None


def linear_search(sekvence, cislo):
    slovnik = {"index": "", "count": ""}
    list = []
    pocet = 0

    for i,cis in enumerate(sekvence):
        if cis == cislo:
            pocet = pocet + 1
            list.append(i)
    slovnik["count"] = pocet
    slovnik["index"] = list
    return slovnik


def pattern_search(sekvence, vzor):
    delka_vzoru = len(vzor)
    delka_sekvence = len(sekvence)
    mnoz = []
    for i in range(delka_sekvence - delka_vzoru + 1):
        window_1 = sekvence[i:i + delka_vzoru]
        if window_1 == vzor:
            mnoz.append(i)

    return mnoz


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    lin = linear_search(sequential_data, 9)
    print(lin)
    sequential_dna = read_data("sequential.json", "dna_sequence")
    part = pattern_search(sequential_dna, "ATA")
    print(part)

if __name__ == '__main__':
    main()