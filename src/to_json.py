import pandas as pd
from datetime import datetime
import json

df = pd.read_csv('LekagulSensorData.csv')

def str_time(string):
    time = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return time

temp = df.values.tolist()

date_count_all = {}
date_count_1 = {}
date_count_2 = {}
date_count_2p = {}
date_count_3 = {}
date_count_4 = {}
date_count_5 = {}
date_count_6 = {}

sensor_count_all = {}
sensor_count_1 = {}
sensor_count_2 = {}
sensor_count_2p = {}
sensor_count_3 = {}
sensor_count_4 = {}
sensor_count_5 = {}
sensor_count_6 = {}

for i in range(len(temp)):
    date_count_all[temp[i][0][:10]] = date_count_all.get(temp[i][0][:10], 0) + 1
    sensor_count_all[temp[i][-1]] = sensor_count_all.get(temp[i][-1], 0) + 1
    if temp[i][2] == "1":
        date_count_1[temp[i][0][:10]] = date_count_1.get(temp[i][0][:10], 0) + 1
        sensor_count_1[temp[i][-1]] = sensor_count_1.get(temp[i][-1], 0) + 1
    elif temp[i][2] == "2":
        date_count_2[temp[i][0][:10]] = date_count_2.get(temp[i][0][:10], 0) + 1
        sensor_count_2[temp[i][-1]] = sensor_count_2.get(temp[i][-1], 0) + 1
    elif temp[i][2] == "2P":
        date_count_2p[temp[i][0][:10]] = date_count_2p.get(temp[i][0][:10], 0) + 1
        sensor_count_2p[temp[i][-1]] = sensor_count_2p.get(temp[i][-1], 0) + 1
    elif temp[i][2] == "3":
        date_count_3[temp[i][0][:10]] = date_count_3.get(temp[i][0][:10], 0) + 1
        sensor_count_3[temp[i][-1]] = sensor_count_3.get(temp[i][-1], 0) + 1
    elif temp[i][2] == "4":
        date_count_4[temp[i][0][:10]] = date_count_4.get(temp[i][0][:10], 0) + 1
        sensor_count_4[temp[i][-1]] = sensor_count_4.get(temp[i][-1], 0) + 1
    elif temp[i][2] == "5":
        date_count_5[temp[i][0][:10]] = date_count_5.get(temp[i][0][:10], 0) + 1
        sensor_count_5[temp[i][-1]] = sensor_count_5.get(temp[i][-1], 0) + 1
    elif temp[i][2] == "6":
        date_count_6[temp[i][0][:10]] = date_count_6.get(temp[i][0][:10], 0) + 1
        sensor_count_6[temp[i][-1]] = sensor_count_6.get(temp[i][-1], 0) + 1



total_date_count_all = []
total_date_count_1 = []
total_date_count_2 = []
total_date_count_2p = []
total_date_count_3 = []
total_date_count_4 = []
total_date_count_5 = []
total_date_count_6 = []

total_sensor_count_all = []
total_sensor_count_1 = []
total_sensor_count_2 = []
total_sensor_count_2p = []
total_sensor_count_3 = []
total_sensor_count_4 = []
total_sensor_count_5 = []
total_sensor_count_6 = []

for key in date_count_all.keys():
    single_date_count = {"date": key, "value": date_count_all[key]}
    total_date_count_all.append(single_date_count)

for key in date_count_1.keys():
    single_date_count = {"date": key, "value": date_count_1[key]}
    total_date_count_1.append(single_date_count)

for key in date_count_2.keys():
    single_date_count = {"date": key, "value": date_count_2[key]}
    total_date_count_2.append(single_date_count)

for key in date_count_2p.keys():
    single_date_count = {"date": key, "value": date_count_2p[key]}
    total_date_count_2p.append(single_date_count)

for key in date_count_3.keys():
    single_date_count = {"date": key, "value": date_count_3[key]}
    total_date_count_3.append(single_date_count)

for key in date_count_4.keys():
    single_date_count = {"date": key, "value": date_count_4[key]}
    total_date_count_4.append(single_date_count)

for key in date_count_5.keys():
    single_date_count = {"date": key, "value": date_count_5[key]}
    total_date_count_5.append(single_date_count)

for key in date_count_6.keys():
    single_date_count = {"date": key, "value": date_count_6[key]}
    total_date_count_6.append(single_date_count)

for key in sensor_count_all.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_all[key]}
    total_sensor_count_all.append(single_sensor_count)

for key in sensor_count_1.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_1[key]}
    total_sensor_count_1.append(single_sensor_count)

for key in sensor_count_2.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_2[key]}
    total_sensor_count_2.append(single_sensor_count)

for key in sensor_count_2p.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_2p[key]}
    total_sensor_count_2p.append(single_sensor_count)

for key in sensor_count_3.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_3[key]}
    total_sensor_count_3.append(single_sensor_count)

for key in sensor_count_4.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_4[key]}
    total_sensor_count_4.append(single_sensor_count)

for key in sensor_count_5.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_5[key]}
    total_sensor_count_5.append(single_sensor_count)

for key in sensor_count_6.keys():
    single_sensor_count = {"sensor": key, "count": sensor_count_6[key]}
    total_sensor_count_6.append(single_sensor_count)


print(sensor_count_all)
to_json_all = json.dumps(total_date_count_all)
to_json_1 = json.dumps(total_date_count_1)
to_json_2 = json.dumps(total_date_count_2)
to_json_2p = json.dumps(total_date_count_2p)
to_json_3 = json.dumps(total_date_count_3)
to_json_4 = json.dumps(total_date_count_4)
to_json_5 = json.dumps(total_date_count_5)
to_json_6 = json.dumps(total_date_count_6)

sensor_to_json_all = json.dumps(total_sensor_count_all)
sensor_to_json_1 = json.dumps(total_sensor_count_1)
sensor_to_json_2 = json.dumps(total_sensor_count_2)
sensor_to_json_2p = json.dumps(total_sensor_count_2p)
sensor_to_json_3 = json.dumps(total_sensor_count_3)
sensor_to_json_4 = json.dumps(total_sensor_count_4)
sensor_to_json_5 = json.dumps(total_sensor_count_5)
sensor_to_json_6 = json.dumps(total_sensor_count_6)

print(to_json_all)

with open("dateValues_all.json", "w") as outfile:
    outfile.write(to_json_all)

with open("dateValues_1.json", "w") as outfile:
    outfile.write(to_json_1)

with open("dateValues_2.json", "w") as outfile:
    outfile.write(to_json_2)

with open("dateValues_2p.json", "w") as outfile:
    outfile.write(to_json_2p)

with open("dateValues_3.json", "w") as outfile:
    outfile.write(to_json_3)

with open("dateValues_4.json", "w") as outfile:
    outfile.write(to_json_4)

with open("dateValues_5.json", "w") as outfile:
    outfile.write(to_json_5)

with open("dateValues_6.json", "w") as outfile:
    outfile.write(to_json_6)

with open("sensorCount_all.json", "w") as outfile:
    outfile.write(sensor_to_json_all)

with open("sensorCount_1.json", "w") as outfile:
    outfile.write(sensor_to_json_1)

with open("sensorCount_2.json", "w") as outfile:
    outfile.write(sensor_to_json_2)

with open("sensorCount_2p.json", "w") as outfile:
    outfile.write(sensor_to_json_2p)

with open("sensorCount_3.json", "w") as outfile:
    outfile.write(sensor_to_json_3)

with open("sensorCount_4.json", "w") as outfile:
    outfile.write(sensor_to_json_4)

with open("sensorCount_5.json", "w") as outfile:
    outfile.write(sensor_to_json_5)

with open("sensorCount_6.json", "w") as outfile:
    outfile.write(sensor_to_json_6)