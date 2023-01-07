# To lazy to write out a list?
# place all items into the file things.txt, run the program and copy the output!
names = []
with open('PythonListMaker/things.txt') as open_file:
    for line in open_file:
        names.append(line.strip())
print(names)