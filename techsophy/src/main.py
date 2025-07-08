from data_collector import load_data, preprocess_data
from trend_analysis import plot_trend, detect_downward_trend
from pattern_detector import detect_anomalies
from recommender import generate_recommendation
from utils import print_insight

def main():
    df = load_data('C:\\Users\\LENOVO T495\\OneDrive\\Desktop\\techsophy\\mood_entries.csv')
    df = preprocess_data(df)

    plot_trend(df)
    print("📈 Mood trend plotted as 'mood_trend.png'")

    df = detect_anomalies(df)
    
    if detect_downward_trend(df):
        print("🔻 Downward trend detected in mood levels.")
    
    recommendation = generate_recommendation(df)
    print_insight(recommendation)

if __name__ == "__main__":
    main()
