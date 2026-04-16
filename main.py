from src.data_loader import load_data
from src.analysis import analyze_data
from src.visualization import (
    plot_product_distribution,
    plot_pie_chart,
    plot_region_analysis
)

def main():
    # Load data
    df = load_data("data/raw/survey_data_1000.csv")

    # Analyze
    results = analyze_data(df)

    print("\n📊 Product Counts:\n", results["product_counts"])
    print("\n📊 Product Percentage:\n", results["product_percentage"])
    print("\n⭐ Average Rating:", results["avg_rating"])

    # Visualization
    plot_product_distribution(df)
    plot_pie_chart(df)
    plot_region_analysis(df)
    
    # Insight
    top_product = results["product_counts"].idxmax()
    print(f"\n🔥 Most preferred product is: {top_product}")

if __name__ == "__main__":
    main()
    
print("\n📊 ===== INSIGHTS =====")

# Top Product
top_product = results["product_counts"].idxmax()
print(f"🔥 Most preferred product is: {top_product}")

# Least Product
least_product = results["product_counts"].idxmin()
print(f"⚠️ Least preferred product is: {least_product}")

# Average Rating
avg_rating = round(results["avg_rating"], 2)
print(f"⭐ Average rating is: {avg_rating}")

# Recommendation Rate
recommend_rate = (df["Recommend"].value_counts(normalize=True) * 100)["Yes"]
print(f"👍 Recommendation rate: {round(recommend_rate, 2)}%")