from itertools import islice

def l33t_code(filepath):
    with open(filepath,"r") as writefile:
        filedata = writefile.read()
        filedata = filedata.replace('o', '0')
        filedata = filedata.replace('O', '0')
        filedata = filedata.replace('a', '4')
        filedata = filedata.replace('A', '4')
        filedata = filedata.replace('e', '3')
        filedata = filedata.replace('E', '3')
        filedata = filedata.replace('i', '1')
        filedata = filedata.replace('I', '1')
    with open(filepath, 'w') as file:
        file.write(filedata)

directory = "/home/fazil/Documents/FizzBuzz-Fazil/"


filepath = directory + input("Enter filename: ")
if filepath.endswith('.txt') == False:
    raise ValueError("Invalid file name only txt accepted")

try:
    numberofpages = int(input("Enter number of pages "))
except ValueError:
    print("The Number of pages must be integer only")
    exit()

numberoflines = int(numberofpages) * 25

with open("/home/fazil/Documents/FizzBuzz-Fazil/mainfile.txt", "r") as myfile:
    linesList = list(islice(myfile,numberoflines))

with open(filepath,'w+') as writefile:
    for item in linesList:
        writefile.write(item)

l33t_code(filepath)