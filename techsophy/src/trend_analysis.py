import pandas as pd
import matplotlib.pyplot as plt

def plot_trend(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['mood_level'], marker='o', linestyle='-')
    plt.title('Mood Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Mood Level')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('mood_trend.png')

def detect_downward_trend(df, window=5):
    rolling = df['mood_level'].rolling(window).mean()
    return rolling.iloc[-1] < 2.5
