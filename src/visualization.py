import matplotlib.pyplot as plt
import seaborn as sns

def plot_product_distribution(df):
    plt.figure(figsize=(8,5))
    df["Product"].value_counts().plot(kind="bar")
    plt.title("Product Popularity")
    plt.savefig("outputs/charts/bar_chart.png")
    plt.show()


def plot_pie_chart(df):
    plt.figure(figsize=(6,6))
    df["Product"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Product Share")
    plt.savefig("outputs/charts/pie_chart.png")
    plt.show()


def plot_region_analysis(df):
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, x="Region", hue="Product")
    plt.title("Region-wise Product Preference")
    plt.savefig("outputs/charts/region_chart.png")
    plt.show()