# Reverse a given list in python

info = ['karl', '100', 'Red', 'Mangoes']
info.reverse()
print("reversed list: " + str(info))

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new
# list.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


def create_string(arg1, arg2):
    index_arg1 = []
    for x in arg1:
        index_arg1.append(arg1.index(x))
    string_list = []
    for x in index_arg1:
        string_list.append(arg1[x] + arg2[x])
        print(string_list)


create_string(list1, list2)

# Write a Python program to find the second largest number in the given list.

listA1 = [10, 20, 4]


def second_largest_number(arg):
    i = len(arg)
    while i != 0:
        if arg[i - 1] > arg[i - 2]:
            arg[i - 1] = arg[i - 2]
            i -= 1
        else:
            
            print(i)


second_largest_number(listA1)
