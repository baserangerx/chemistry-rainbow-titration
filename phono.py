import wave
import struct
import math
import xml.etree.ElementTree as ET

# Converts the data into a sin wave and stores it in an array
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

# Writes the sin wave array to a .wav file
def save_wav(filename, _data, sample_rate=44100):
    with wave.open('output/'+filename, 'wb') as writefile:
        writefile.setnchannels(1)  # Mono audio
        writefile.setsampwidth(2)  # 16-bit audio
        writefile.setframerate(sample_rate)
        for sample in _data:
            writefile.writeframes(struct.pack('<h', sample)) # '<h' for 16-bit little endian

# Returns the linearly interpolated value of Y
def interpolate(x):
    '''
        y = y_offset + (x)(slope)
    '''
    y = 0.00
    for i in range(len(data[0])):
        #print(i)
        if(data[0][i] < x <= data[0][i+1]):
            y = data[1][i] + (x-data[0][i]) * (data[1][i+1]-data[1][i])/(data[0][i+1]-data[0][i])
            break
    return y

# Returns the area under the graph from 0 -> X
def getArea(x):
    sum = 0.00
    for i in range(len(data[0])):
        if x > data[0][i+1]:
            sum += area[i]
        else:
            sum += (x-data[0][i])*data[1][i] + (x-data[0][i])*(interpolate(x)-data[1][i])/2
            break
    return sum

# Main function - converts _data into an audible .wav
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


frequency = 220  # Frequency in Hz
#duration = 2 # Duration in seconds

# Stores a set of data points collected from the dataset
data = [[],[]]
#data[0] -> time : X
#data[1] -> pH : Y

# Divides the horizonal unit, shortening the duration of the wav file
#   (Example: 180s / 6 -> 30s of audio)
divider = 6
duration = 0

# Used for getArea() optimizations
area = []


