import xml.etree.ElementTree as ET
import phono

file_name = input("File: ")

def convert_file(file):
    file.seek(0)

    writeLength = 0
    file.seek(0)
    for i, char in enumerate(file.read()):
        if char == '<' and not writeLength:
            file.seek(i)
            writeLength = i
        if writeLength and char == '\0':
            writeLength = i - writeLength - 1
            break
    
    writeFile = open('data/xml/'+file_name+'.xml', 'w')
    writeFile.write(file.read(writeLength))

    writeFile.close()
    file.close()

    #print(file.read())

def convert_to_wav():
    tree = ET.parse('data/xml/'+file_name+'.xml')
    root = tree.getroot()

    data = [[],[]]

    for i, dataSet in enumerate(root.find('DataSet').findall('DataColumn')):
        #print(dataSet.find('DataObjectName').text + dataSet.find('ColumnCells').text)
        tmpString = ""
        for char in dataSet.find('ColumnCells').text[1:]:
            if char == "\n":
                data[i].append(float(tmpString))
                tmpString = ""
            else:
                tmpString += char
        #print(child.tag, child.attrib)
        #print(data)
        #print("")
    phono.generate_file(file_name, data)

convert_file(open('data/'+file_name+'.gambl', 'r'))
convert_to_wav()