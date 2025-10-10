import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
from schemas import WorkEntryResponse

def train_dummy_model():
    file = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    df = pd.DataFrame(file)
    drop = df.dropna()
    df_encoded = pd.get_dummies(df,columns=["Attrition", "BusinessTravel", "Department", "EducationField", "Gender"
        ,"JobRole", "MaritalStatus", "Over18", "OverTime"])
    encoded_dataframe = pd.DataFrame(df_encoded)
    x = encoded_dataframe.drop( ["Attrition_No", "Attrition_Yes"],axis=1)
    y = encoded_dataframe[["Attrition_No", "Attrition_Yes"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    fitness = model.fit(x_train,y_train)
    joblib.dump(model,"model.joblib")

def load_model():
    loaded_model = joblib.load("model.joblib")

def predict_from_entry(WorkEntryResponse):
    model = load_model()
    features = [[WorkEntryResponse.amount_of_work, WorkEntryResponse.duration_seconds]]
    if model is None:
        # fallback: naive rule-based prediction
        avg_rate = WorkEntryResponse.amount_of_work / (WorkEntryResponse.duration_seconds/3600) if entry.duration_seconds else 0
        if avg_rate > 10:
            return "high_productivity"
        elif avg_rate > 3:
            return "medium_productivity"
        else:
            return "low_productivity"
    else:
        y_pred = model.predict(features)
        return str(y_pred[0])
