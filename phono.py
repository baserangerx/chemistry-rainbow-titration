import wave
import struct
import math
import xml.etree.ElementTree as ET

def generate_sine_wave(frequency, duration, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    amplitude = 2**15 - 1  # Max amplitude for 16-bit audio
    wave_data = []

    for i in range(num_samples):
        #sample = amplitude * math.sin(2 * math.pi * frequency * i/sample_rate)
        sample = amplitude * math.sin(2 * math.pi * frequency * (i/sample_rate + getArea(i/sample_rate*divider)/14/divider))
        wave_data.append(int(sample))
        if (i % sample_rate) == 0:
            print(i/sample_rate)

    return wave_data

def save_wav(filename, data, sample_rate=44100):
    with wave.open('output/'+filename, 'wb') as writefile:
        writefile.setnchannels(1)  # Mono audio
        writefile.setsampwidth(2)  # 16-bit audio
        writefile.setframerate(sample_rate)
        for sample in data:
            writefile.writeframes(struct.pack('<h', sample)) # '<h' for 16-bit little endian

def interpolate(x):
    sum = 0.00
    for i in range(len(data[0])):
        #print(i)
        if(data[0][i] < x <= data[0][i+1]):
            sum = data[1][i] + (x-data[0][i])*(data[1][i+1]-data[1][i])/(data[0][i+1]-data[0][i])
            break
    return sum

def getArea(x):
    sum = 0.00
    for i in range(len(data[0])):
        if x > data[0][i+1]:
            sum += area[i]
        else:
            sum += (x-data[0][i])*data[1][i] + (x-data[0][i])*(interpolate(x)-data[1][i])/2
            break
    return sum


frequency = 220  # Frequency in Hz
#duration = 2 # Duration in seconds

data = [[],[]]
#data[0] -> time : X
#data[1] -> pH : Y

divider = 6
duration = 0
#time in seconds

area = []

def generate_file(file_name, _data):
    global data, area, duration
    data = _data
    duration = data[0][len(data[0])-1]/divider
    area = []

    for i in range(len(data[0])-1):
        area.append((data[0][i+1]-data[0][i])*data[1][i] + (data[0][i+1]-data[0][i])*(data[1][i+1]-data[1][i])/2)

    sine_wave = generate_sine_wave(frequency, duration)
    save_wav(file_name+'.wav', sine_wave)
    print(file_name+'.wav complete')

#print("file completed")