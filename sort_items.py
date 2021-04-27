import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    with open (file_name, "r", encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter='\t')

        for line in reader:
            data = [int(number) for number in line]
    return data


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    with open(file_name, encoding = 'uft-8') as file:
        # csv má čárky autoamaticky - nemusí být delimiter
        reader = csv.reader(file)

        for idx, line in enumerate(reader):
            if idx == line:
                data = [int(number) for number in line]
        return data

def selection_sort(number_array, direction = "ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
# vzestupně

    for i in range(len(number_array)):
        minimum = i
        for j in range(i+1, len(number_array)):
            if direction == "ascending":
                if number_array[j] < number_array[minimum]:
                    minimum = j
            elif direction == "descending":
                if number_array[j] > number_array[minimum]:
                    minimum = j
        number_array[i], number_array[minimum] = number_array[minimum], number_array[i]
    return number_array

    # for number in hodnoty:
    #     if min(number):
    #         seznam_cisel.append(number)
    #         hodnoty.extend(number)
    #     else:
    #         continue
    # return seznam_cisel


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """


def main():
    hodnoty_soubor = read_row("numers_one.cvs")
    serazeni = selection_sort(hodnoty_soubor)
    rozsireni_radku = read_rows("numbers_two.csv", 1)
    # Ukol: Selection Sort


    # Ukol: Selection Sort - se smerem razeni
    

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

