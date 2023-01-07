# To lazy to write out a list?
# place all items into the file things.txt, run the program and copy the output!
things = []
with open('PythonListMaker/things.txt') as open_file: # Rename parent folder to PythonListMaker for this to work
    for line in open_file:
        things.append(line.strip())
print(things)
