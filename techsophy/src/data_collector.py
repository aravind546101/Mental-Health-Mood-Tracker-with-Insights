import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])
    df = df.sort_values('date')
    return df

def preprocess_data(df):
    df['mood_level'] = df['mood_level'].fillna(df['mood_level'].mean())
    df['notes'] = df['notes'].fillna('')
    return df
