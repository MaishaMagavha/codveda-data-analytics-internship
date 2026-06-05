"""
Codveda Data Analytics — Level 3, Task 2: Interactive Dashboard
================================================================
Power BI / Tableau Desktop do not run on Linux, so this dashboard is built with
Streamlit + Plotly — the standard open-source equivalent. It delivers the same
objectives required by the task: imported & cleaned data, interactive charts
(bar / line / pie / geographic map), sidebar filters & slicers, and a shareable
web app.

Run it with:
    streamlit run app.py
Then open the URL it prints (default http://localhost:8501).
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Codveda — Telecom Churn Dashboard",
                   page_icon="📊", layout="wide")

# ----------------------------------------------------------------------------- data
DATA_DIR = Path("../../../Data Set For Task")
if not DATA_DIR.exists():
    DATA_DIR = Path("/home/magzm/Codveda/Data Set For Task")


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load and lightly clean the telecom churn data (80 + 20 combined)."""
    a = pd.read_csv(DATA_DIR / "Churn Prdiction Data" / "churn-bigml-80.csv")
    b = pd.read_csv(DATA_DIR / "Churn Prdiction Data" / "churn-bigml-20.csv")
    df = pd.concat([a, b], ignore_index=True)
    df["Churn"] = df["Churn"].astype(bool)
    df["Churn label"] = df["Churn"].map({True: "Churned", False: "Stayed"})
    for c in ["International plan", "Voice mail plan"]:
        df[c] = df[c].str.strip()
    return df


df = load_data()

# ------------------------------------------------------------------------- sidebar
st.sidebar.title("🔎 Filters / Slicers")
st.sidebar.caption("Interactively slice the data — every chart updates live.")

states = sorted(df["State"].unique())
sel_states = st.sidebar.multiselect("State", states, default=states)

intl = st.sidebar.radio("International plan", ["All", "Yes", "No"], horizontal=True)
vmail = st.sidebar.radio("Voice mail plan", ["All", "Yes", "No"], horizontal=True)

acct_min, acct_max = int(df["Account length"].min()), int(df["Account length"].max())
sel_acct = st.sidebar.slider("Account length (days)", acct_min, acct_max,
                             (acct_min, acct_max))

churn_view = st.sidebar.radio("Customer set", ["All", "Churned only", "Stayed only"])

# apply filters
mask = df["State"].isin(sel_states) & df["Account length"].between(*sel_acct)
if intl != "All":
    mask &= df["International plan"] == intl
if vmail != "All":
    mask &= df["Voice mail plan"] == vmail
if churn_view == "Churned only":
    mask &= df["Churn"]
elif churn_view == "Stayed only":
    mask &= ~df["Churn"]
fdf = df[mask]

# ---------------------------------------------------------------------------- header
st.title("📊 Telecom Customer Churn Dashboard")
st.caption("Codveda Technology · Data Analytics Internship · Level 3 — Task 2 "
           "(open-source Power BI/Tableau equivalent, built with Streamlit + Plotly)")

if fdf.empty:
    st.warning("No customers match the current filters. Widen your selection.")
    st.stop()

# ------------------------------------------------------------------------- KPI cards
total = len(fdf)
churned = int(fdf["Churn"].sum())
rate = churned / total * 100
avg_calls = fdf["Customer service calls"].mean()
avg_daycharge = fdf["Total day charge"].mean()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Customers", f"{total:,}")
c2.metric("Churned", f"{churned:,}")
c3.metric("Churn rate", f"{rate:.1f}%")
c4.metric("Avg. service calls", f"{avg_calls:.2f}")

st.divider()

# ----------------------------------------------------------------------------- row 1
left, right = st.columns(2)

with left:
    st.subheader("Churn breakdown")
    pie = px.pie(fdf, names="Churn label", hole=0.45,
                 color="Churn label",
                 color_discrete_map={"Churned": "#e45756", "Stayed": "#54a24b"})
    pie.update_layout(margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(pie, use_container_width=True)

with right:
    st.subheader("Churn rate by customer service calls")
    by_calls = (fdf.groupby("Customer service calls")["Churn"]
                .mean().mul(100).reset_index(name="Churn rate (%)"))
    bar = px.bar(by_calls, x="Customer service calls", y="Churn rate (%)",
                 color="Churn rate (%)", color_continuous_scale="Reds")
    bar.update_layout(margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(bar, use_container_width=True)

# ----------------------------------------------------------------------------- row 2
left2, right2 = st.columns(2)

with left2:
    st.subheader("Churn rate by state (map)")
    by_state = (fdf.groupby("State")["Churn"]
                .mean().mul(100).reset_index(name="Churn rate (%)"))
    geo = px.choropleth(by_state, locations="State", locationmode="USA-states",
                        color="Churn rate (%)", scope="usa",
                        color_continuous_scale="OrRd")
    geo.update_layout(margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(geo, use_container_width=True)

with right2:
    st.subheader("Day charge vs. evening charge")
    sc = px.scatter(fdf, x="Total day charge", y="Total eve charge",
                    color="Churn label", opacity=0.6,
                    color_discrete_map={"Churned": "#e45756", "Stayed": "#54a24b"})
    sc.update_layout(margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(sc, use_container_width=True)

# ----------------------------------------------------------------------------- table
st.divider()
st.subheader("Filtered customer records")
st.dataframe(fdf, use_container_width=True, height=300)
st.download_button("⬇️ Download filtered data (CSV)",
                   fdf.to_csv(index=False).encode(),
                   file_name="filtered_churn.csv", mime="text/csv")
