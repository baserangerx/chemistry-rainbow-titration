import csv

file = input("Filename: ")

data = [[],[]]

with open('data/'+file) as csvfile:
    filereader = csv.reader(csvfile)
    for i in filereader:
        if(i[1]==''):break
        data[0].append(i[0])
        data[1].append(i[1])

print('gloob')