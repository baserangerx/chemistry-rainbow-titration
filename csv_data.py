import csv
import phono

file = input("Filename: ")
dataSet = []

with open('data/'+file) as csvfile:
    filereader = csv.reader(csvfile)
    firstline = next(filereader)
    
    for i in range(len(firstline)-1): 
        dataSet.append([[],[]])
    #data = [[],[]]
    for row in filereader:
        for i in range(len(firstline)-1):
            if(row[i+1]==''):continue
            dataSet[i][0].append(float(row[0]))
            dataSet[i][1].append(float(row[i+1]))
        
for i, data in enumerate(dataSet):
    #print(firstline[i+1])
    phono.generate_file(firstline[i+1], data)
#phono.generate_file(firstline[4+1], dataSet[4])

    #print(dataSet)

print('gloob')