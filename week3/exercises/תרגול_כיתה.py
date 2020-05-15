"""def count_records_in_file(path):
    with open(path,'r') as file_handler:
        content = file_handler.readlines()
    return len(content)

print(count_records_in_file("/home/thor/Documents/Python_Course/week3/bank_safe.py"))
"""
"""

def task(sentance2, number_of_times2):
    j = 0
    while j < number_of_times2:
        print(f"               {j}, {sentance2}")
        j += 1


def help_bart(sentance, number_of_times, sentance2, second_total):
    ns = 0
    while ns < number_of_times:
        print(ns, sentance)
        ns += 1
        task(sentance2, second_total)


help_bart("this is my church", 50, "I will stop cheating on my dog",3)"""


def count_records_in_file(path):
    with open(path, 'r') as list_of_names:
        content = list_of_names.readlines()
        things_to_join_by = ""
        content = things_to_join_by.join(content)
        content = content.strip()
    return content


list_of_names2 = count_records_in_file("/home/thor/names.txt")
print(type(count_records_in_file("/home/thor/names.txt")))
print(list_of_names2)
