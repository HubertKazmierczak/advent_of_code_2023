data = ''''''
with open("input.txt") as f:
    data = data + f.read() + "\n"



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
    for i in lines:
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