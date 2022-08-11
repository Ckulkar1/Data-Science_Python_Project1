# Write a program to create a new string made of the middle three characters of an input string.

string = "AwesomeCodep"


def find_mid_3_char(arg):
    if len(arg) % 2 == 1:
        n = len(arg) + 1
        n = int(n / 2 - 1)
        print(arg[n - 1:n + 2])
    else:
        n = int(len(arg) / 2)
        print(arg[n - 1:n + 2])


find_mid_3_char(string)

# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "BetterSa"
s2 = "Call"


def insert_str_mid(arg1, arg2):
    if len(arg1) % 2 == 1:
        n = len(arg1) + 1
        n = int(n / 2 - 1)
        print(s1[0: n] + arg2 + s1[n:len(arg1)])
    else:
        n = int(len(arg1) / 2)
        print(s1[0: n] + arg2 + s1[n:len(arg1)])


insert_str_mid(s1, s2)

# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle,
# and last characters.

string1 = "America"
string2 = "Japan"


def find_fml_char(arg):
    f = arg[0]
    l = arg[-1]
    if len(arg) % 2 == 1:
        n = len(arg) + 1
        n = int(n / 2 - 1)
    else:
        n = int(len(arg) / 2)
    m = arg[n]

    arg_char = f + m + l
    return arg_char


def combine_fml_char(*args):
    string3 = []
    for arg in args:
        fml_args = (find_fml_char(arg))
        i = 0
        while i < len(fml_args):
            string3.append(fml_args[i])
            i += 1
            str_string3 = ''.join(string3)
            print(str_string3)


combine_fml_char(string1, string2)

# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
# characters in the s1 are present in s2. The character’s position doesn’t matter.

stringA1 = "gold"
stringA2 = "gtr"


def check_string_balance(arg1, arg2):
    arg1_set = set(())
    arg2_set = set(())
    result = False
    for x in arg1:
        arg1_set.add(x)
    for x in arg2:
        arg2_set.add(x)
    if arg1_set.issubset(arg2_set) or arg2_set.issubset(arg1_set):
        result = True
    print(result)


check_string_balance(stringA1, stringA2)

# Write a program to split a given string on hyphens and display first and last substring.

stringB1 = "Emma-is-a-data-scientist"


# result = Emma, scientist

def split_string(arg):
    first_hyphen_int = arg.find("-")
    last_hyphen_int = arg.rfind("-")
    first_word = arg[0: first_hyphen_int]
    last_word = arg[last_hyphen_int + 1: len(arg)]
    result = first_word + ", " + last_word
    print(result)


split_string(stringB1)

# Reverse a given string
# Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."


def reverse(x):
    return x[::-1]


reverse_text = reverse(str1)
print(reverse_text)

last_emma_index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index" + str(last_emma_index))

