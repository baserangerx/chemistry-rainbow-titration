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
    
    writeFile = open('xml/'+file_name+'.xml', 'w')
    writeFile.write(file.read(writeLength))

    writeFile.close()
    file.close()

    #print(file.read())

convert_file(open(file_name+'.gambl', 'r'))