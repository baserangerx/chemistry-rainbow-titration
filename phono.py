import wave
import struct
import math
import xml.etree.ElementTree as ET
import gambl_to_xml as GTX
#import turtle

def generate_sine_wave(frequency, duration, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    amplitude = 2**15 - 1  # Max amplitude for 16-bit audio
    wave_data = []
    for i in range(num_samples):
        sample = amplitude * math.sin(2 * math.pi * frequency * (interpolate(i/sample_rate*divider))/14  * i / sample_rate)
        #(interpolate(i/sample_rate*divider))/14 
        wave_data.append(int(sample))
    return wave_data

def save_wav(filename, data, sample_rate=44100):
    with wave.open(filename, 'wb') as writefile:
        writefile.setnchannels(1)  # Mono audio
        writefile.setsampwidth(2)  # 16-bit audio
        writefile.setframerate(sample_rate)
        for sample in data:
            writefile.writeframes(struct.pack('<h', sample)) # '<h' for 16-bit little endian

# Example usage
frequency = 440  # Frequency in Hz
#duration = 2 # Duration in seconds

tree = ET.parse('xml/'+GTX.file_name+'.xml')
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
print(data)
print("")

divider = 5
duration = data[0][len(data[0])-1]/divider
#10mL/Second


#def interpolate(x):
    #sum = 0
    #for i in range(len(data[0])):
        #mult = 1

        #for j in range(len(data[0])):
            #if i != j:
                #print(str(i) + ' ' + str(j))
                #mult *= (x - data[0][j]) / (data[0][i] - data[0][j])
        
        #sum += mult*data[1][i]
    #return sum
def interpolate(x):
    sum = 0.0
    for i in range(len(data[0])):
        #print(i)
        if(data[0][i] <= x < data[0][i+1]):
            sum = data[1][i] + (data[1][i+1]-data[1][i])*(x-data[0][i])/(data[0][i+1]-data[0][i])
            break
    return sum

print(interpolate(5.0))

#turtle.setpos(-350,-300)
#turtle.speed(0)
#turtle.clear()

#for i in range(10000):
    #turtle.setx((i/10000)*600-350)
    #turtle.sety((interpolate(i/10000*30)/14)*600-300)
    #turtle.dot(10,'black')

#input("end?")

sine_wave = generate_sine_wave(frequency, duration)
save_wav('sine_wave.wav', sine_wave)