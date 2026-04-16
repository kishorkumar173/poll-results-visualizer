import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Poll Dashboard", layout="wide")

# -------------------------------
# TITLE
# -------------------------------
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📊 Poll Results Dashboard</h1>",
    unsafe_allow_html=True
)

# -------------------------------
# FILE UPLOAD
# -------------------------------
st.subheader("📂 Upload Your Dataset")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Fix column names (IMPORTANT)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.title()

else:
    st.warning("⚠️ Please upload a CSV file to continue")
    st.stop()
    
required_cols = ["Product", "Region", "Rating", "Recommend"]

for col in required_cols:
    if col not in df.columns:
        st.error(f"Missing column: {col}")
        st.stop()

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("🔍 Data Preview")
st.dataframe(df.head())

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.markdown("## 🎛 Filters")

region = st.sidebar.multiselect(
    "🌍 Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product = st.sidebar.multiselect(
    "📦 Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

# -------------------------------
# FILTER DATA
# -------------------------------
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Product"].isin(product))
]

# -------------------------------
# METRICS
# -------------------------------
st.markdown("## 📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Responses", len(filtered_df))
col2.metric("⭐ Avg Rating", round(filtered_df["Rating"].mean(), 2))

if len(filtered_df) > 0:
    top_product = filtered_df["Product"].value_counts().idxmax()
else:
    top_product = "N/A"

col3.metric("🔥 Top Product", top_product)

# -------------------------------
# COLORS
# -------------------------------
colors = ["#FF6F61", "#6B5B95", "#88B04B"]

# -------------------------------
# BAR CHART (FIXED ERROR)
# -------------------------------
st.markdown("## 📊 Product Popularity")

product_counts = filtered_df["Product"].value_counts().reset_index()
product_counts.columns = ["Product", "Count"]

fig_bar = px.bar(
    product_counts,
    x="Product",
    y="Count",
    color="Product",
    color_discrete_sequence=colors
)

fig_bar.update_layout(plot_bgcolor="#F9F9F9")
st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------------
# PIE CHART
# -------------------------------
st.markdown("## 🥧 Product Share")

fig_pie = px.pie(
    filtered_df,
    names="Product",
    color_discrete_sequence=colors
)

fig_pie.update_traces(textinfo="percent+label")
st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------
# REGION ANALYSIS
# -------------------------------
st.markdown("## 🌍 Region-wise Preference")

fig_region = px.histogram(
    filtered_df,
    x="Region",
    color="Product",
    barmode="group",
    color_discrete_sequence=colors
)

fig_region.update_layout(plot_bgcolor="#F0F8FF")
st.plotly_chart(fig_region, use_container_width=True)

# -------------------------------
# INSIGHTS
# -------------------------------
st.markdown("## 🧠 Insights")

if len(filtered_df) > 0:
    least_product = filtered_df["Product"].value_counts().idxmin()
    avg_rating = round(filtered_df["Rating"].mean(), 2)
    recommend_rate = (filtered_df["Recommend"].value_counts(normalize=True) * 100).get("Yes", 0)

    st.write(f"🔥 Most preferred product: **{top_product}**")
    st.write(f"⚠️ Least preferred product: **{least_product}**")
    st.write(f"⭐ Average rating: **{avg_rating}**")
    st.write(f"👍 Recommendation rate: **{round(recommend_rate, 2)}%**")
else:
    st.warning("No data available for selected filters")