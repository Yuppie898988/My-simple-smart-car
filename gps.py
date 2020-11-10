import serial
def position():
    ser = serial.Serial("/dev/ttyAMA0", 9600)
    while(1):
        content = ser.readline().decode(errors='ignore').split(',')
        if content[0] == '$GNRMC':
            raw_lon = float(content[5])
            lon = raw_lon // 100 + (raw_lon % 100) / 60 + 0.006462
            raw_lat = float(content[3])
            lat = raw_lat // 100 + (raw_lat % 100) / 60 + 0.001023
            ori = '%.6f' % lon + ',' + '%.6f' % lat
            print(ori)
            return ori