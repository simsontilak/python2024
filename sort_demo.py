import sort_lib

given_list = sort_lib.get_random_list(30000, 5000, 100000)
print(given_list)
sorted_list = sort_lib.sort_list(given_list)
print(sorted_list)