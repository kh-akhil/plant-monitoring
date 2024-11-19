import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


data = pd.read_csv('data.csv')
X = data.drop(['Water_pump_actuator_ON'], axis = 1)
y = data['Water_pump_actuator_ON']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

clf = GradientBoostingClassifier(random_state=42)
clf.fit(X_train, y_train)
test = [41,59,100]
input = np.array(test).reshape(1, -1)
ans = clf.predict(input)
print(ans[0])


