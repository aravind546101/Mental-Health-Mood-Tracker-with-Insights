from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(df):
    model = IsolationForest(contamination=0.1)
    mood_scores = df[['mood_level']].values
    df['anomaly'] = model.fit_predict(mood_scores)
    return df
