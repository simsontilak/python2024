# Write a program to generate an list of uniformly distributed random numbers.
import random

def get_random_list(max_size, start_num, end_num):
    a_list = []
    for index in range(max_size):
        a_list.append(int(random.uniform(start_num, end_num)))
    return a_list

def sort_list(a_list):
    for index in range(len(a_list)):
        min_index = index
        for another_index in range(index+1, len(a_list)):
            if a_list[min_index] > a_list[another_index]:
                min_index = another_index
        a_list[index], a_list[min_index] = a_list[min_index], a_list[index]
    return a_list


