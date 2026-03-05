import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# load dataset
data = pd.read_csv("../dataset/sample_bus_inspection_data.csv")

X = data.drop("passed_fc", axis=1)
y = data["passed_fc"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "fc_model.pkl")

print("Model trained and saved.")
