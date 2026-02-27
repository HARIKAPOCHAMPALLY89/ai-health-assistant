import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("hospital_data.csv")
df.columns = df.columns.str.strip().str.lower()

df = df[["age", "condition", "patient_state", "readmission"]]

le_condition = LabelEncoder()
le_state = LabelEncoder()
le_readmission = LabelEncoder()

df["condition"] = le_condition.fit_transform(df["condition"])
df["patient_state"] = le_state.fit_transform(df["patient_state"])
df["readmission"] = le_readmission.fit_transform(df["readmission"])

X = df[["age", "condition", "patient_state"]]
y = df["readmission"]

model = RandomForestClassifier()
model.fit(X, y)

with open("readmission_model.pkl", "wb") as f:
    pickle.dump((model, le_condition, le_state, le_readmission), f)

print("Model trained and saved successfully!")