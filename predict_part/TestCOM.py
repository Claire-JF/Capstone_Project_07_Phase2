import serial
import re
import pymysql
import time
import pandas as pd
from datetime import datetime

retract = pd.DataFrame()
serialPort = "COM8"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("Parameter setting:COM=%s ，baudRate=%d" % (serialPort, baudRate))

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='pass123',
                             db='tempandhum',
                             charset='utf8')
cursor = connection.cursor()
print("Successfully connected to database!")
retract = pd.DataFrame(columns=["Temperature (Celsius)","Humidity","Update Time"])
i = 0
while   True:
# while i<112:
    while i <32:
        str = ser.readline().decode('utf-8')
        if str.strip() != '':
                # print(str)

            temperature_pattern = r"Temperature:\s*([\d\.]+℃)"
            humidity_pattern = r"Humidity:\s*([\d\.]+%)"

            temperature_match = re.search(temperature_pattern, str)
            humidity_match = re.search(humidity_pattern, str)

            if temperature_match:
                temperature = temperature_match.group(1)
                # print(type(temperature))

            if humidity_match:
                humidity = humidity_match.group(1)
                # print(humidity)
            
            # time_now = datetime.now()
            # current_time = 1
            update_time = time.asctime()

            # retract = retract.append({'Temperature (Celsius)': temperature},{'Humidity':humidity},{'Update Time':update_time})
            retract.loc[i] = [temperature, humidity, update_time]
            sql = 'insert into rain(temperature,humidity,updata_time)VALUES(%s,%s,%s)'
            cursor.execute(sql, [temperature, humidity, update_time])
            connection.commit()
            print(retract)
        i = i+1
    print("finish")
    retract.to_csv(path_or_buf="updateDate.csv", na_rep='', float_format=2,index=False)
    i=0
# retract.to_csv(path_or_buf="updateDate", na_rep='', float_format=2,index=True, index_label="index")




