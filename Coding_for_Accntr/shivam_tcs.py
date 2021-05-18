import re

count = 0

def r_string(string, sub_string):
    # for i in range(0, len(string), len(sub_string)):

    # print(f"ans now is {ans}")
    if re.search(sub_string, string):
        string = string.replace(sub_string, "")
        print(f"sub_string is {sub_string} and ans is {string} and string is {string}")
        r_string(string, sub_string)
    if not re.search(sub_string, string):
        return string


string = input("Enter any string: ")
sub_string = input("Enter any sub_string: ")
print("Required ans is: ", r_string(string, sub_string))
