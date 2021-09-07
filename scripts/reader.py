import csv
import time

with open("/home/arianna/catkin_ws/src/progetto_rana/documents/gps_points.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        line = row[0],row[1]
        print(str(line))
        time.sleep(2)
