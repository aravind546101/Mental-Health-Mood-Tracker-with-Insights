def generate_recommendation(df):
    bad_days = df[df['mood_level'] <= 2]
    if len(bad_days) >= 3:
        return "⚠️ Multiple low mood days detected. Consider speaking to a mental health professional."
    
    if df['anomaly'].iloc[-1] == -1:
        return "❗ Recent mood entry is unusual. Reflect on possible triggers."

    return "✅ Mood is stable. Keep up your self-care routine!"
