def analyze_data(df):
    results = {}

    # Product counts
    results["product_counts"] = df["Product"].value_counts()

    # Percentage
    results["product_percentage"] = df["Product"].value_counts(normalize=True) * 100

    # Average rating
    results["avg_rating"] = df["Rating"].mean()

    return results