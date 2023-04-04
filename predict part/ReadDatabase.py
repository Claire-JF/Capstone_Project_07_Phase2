import csv
import datetime
import re
import mysql.connector
import pandas as pd


def readDB(days: int):
    """
    read DB and write into csv files
    :param days: How many days to read from the DB
    :return: None
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ni2310",
        database="tempandhum"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM rain")

    myresult = mycursor.fetchall()

    i = days - 1
    Date_i = datetime.datetime.today() - datetime.timedelta(days=i)
    start = False
    for x in myresult:
        if start is False and re.match(Date_i.strftime("%a %b %d"), x[3]):
            with open(Date_i.strftime("%a %b %d") + '.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Temperature', 'Humidity', 'Date/Time'])
                start = True
        if start:
            if re.match(Date_i.strftime("%a %b %d"), x[3]):
                with open(Date_i.strftime("%a %b %d") + '.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(x)
            else:
                i = i - 1
                Date_i = datetime.datetime.today() - datetime.timedelta(days=i)
                with open(Date_i.strftime("%a %b %d") + '.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['ID', 'Temperature', 'Humidity', 'Date/Time'])
                    writer.writerow(x)


def write_localdata(days: int):
    """
        读取DB中的数据，找到 从 days天前起 到 今天的最高温和最低温数据，写入local_data.csv
        :param days: How many days to read from the DB
        :return: None
        """
    readDB(days)

    f = open('local_data.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Max_t", "Min_t"])

    i = days - 1
    Date_i = datetime.datetime.today() - datetime.timedelta(days=i)

    while i >= 0:
        df = pd.read_csv(Date_i.strftime("%a %b %d") + '.csv')

        df['Temperature'] = df['Temperature'].str.rstrip('℃').astype(float)

        # 找到温度列中的最大和最小值
        max_temperature = df['Temperature'].max()
        min_temperature = df['Temperature'].min()

        csv_writer.writerow([max_temperature, min_temperature])

        print(Date_i.strftime("%a %b %d"))
        print('最高温度：', max_temperature)
        print('最低温度：', min_temperature)

        i = i - 1
        Date_i = datetime.datetime.today() - datetime.timedelta(days=i)


if __name__ == '__main__':
    write_localdata(7)
