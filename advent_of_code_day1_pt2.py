data = ''''''
with open("input.txt") as f:
    data = data + f.read() + "\n"

digits = ["one","two","three","four","five","six","seven","eight","nine"]
dictionary = {}
for i in range(0,9):
    dictionary[digits[i]] = i + 1

def separate_lines(lines):
    string = ""
    list1 = []
    for i in range(len(lines)):
        if lines[i] == "\n":
            list1.append(string)
            string = ""
        else:
            string = string + lines[i]

    return list1
lines = separate_lines(data)
def separate_numbers(lines):
    string = ""
    returned = []
    new_lines = []
    for i in lines:
        for z in digits:
            i = i.replace(z,str(str(z[0]) +str(dictionary[z]) + str(z[-1])))
        new_lines.append(i)
    for i in new_lines:
        for y in range(len(i)):
            if i[y].isnumeric():
                string = string + i[y]
        returned.append(string)
        string = ""
    return returned
lines = separate_numbers(lines)
string = ""
number = 0
for i in lines:
    if not i == "":
        string = i[0] + i[-1]
        number += int(string)
    
print(number)



