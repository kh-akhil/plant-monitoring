import serial
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

ser = serial.Serial('/dev/cu.usbserial-14130', 9600)
time.sleep(2)

data = pd.read_csv('data.csv')
X = data.drop(['Water_pump_actuator_ON'], axis = 1)
y = data['Water_pump_actuator_ON']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X_train, y_train)


def predict():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(line)
        input_data = [int(x) for x in line.split(',')]
        input = np.array(input_data).reshape(1, -1)
        ans = clf.predict(input)
        print(ans[0])
        ser.write(ans[0]).encode()
        ser.flush()
    time.sleep(1)

try:
    while True:
        predict()
except KeyboardInterrupt:
    print("Program closed")
    ser.close()