import serial
import re
import pymysql
import time

serialPort = "COM14"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("Parameter setting:COM=%s ，baudRate=%d" % (serialPort, baudRate))

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='00000zyt',
                             db='tempandhum',
                             charset='utf8')
cursor = connection.cursor()
print("Successfully connected to database!")

while True:
    str = ser.readline().decode('utf-8')
    if str.strip() != '':
        print(str)

        temperature_pattern = r"Temperature:\s*([\d\.]+℃)"
        humidity_pattern = r"Humidity:\s*([\d\.]+%)"

        temperature_match = re.search(temperature_pattern, str)
        humidity_match = re.search(humidity_pattern, str)

        if temperature_match:
            temperature = temperature_match.group(1)

        if humidity_match:
            humidity = humidity_match.group(1)

        update_time = time.asctime()

        sql = 'insert into rain(temperature,humidity,updata_time)VALUES(%s,%s,%s)'
        cursor.execute(sql, [temperature, humidity, update_time])
        connection.commit()
