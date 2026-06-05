# Interactive Churn Dashboard — Level 3, Task 2

The task asks for an interactive dashboard in **Power BI or Tableau**. Neither
Power BI Desktop nor Tableau Desktop runs on Linux, so this dashboard is built with
**Streamlit + Plotly** — the standard open-source equivalent — and fulfils every
objective of the task:

| Task objective | How it's met |
|----------------|--------------|
| Import & clean the dataset | `load_data()` loads + cleans the telecom churn data |
| Interactive visualizations | Plotly pie, bar, scatter, and a US **choropleth map** |
| Filters & slicers | Sidebar: state multiselect, plan radios, account-length slider, churn toggle |
| Publish / share | Runs as a web app; deployable free to Streamlit Community Cloud |

## Run it

```bash
# from the repo root
source /home/magzm/venv/bin/activate        # or your own environment
pip install -r ../../requirements.txt        # if not already installed

cd Level-3/dashboard
streamlit run app.py
```

Then open the URL it prints (default <http://localhost:8501>). Every chart and KPI
updates live as you change the sidebar filters. Use **⬇️ Download filtered data** to
export the current slice as CSV.

## Publishing (optional, for the submission video)
Push this repo to GitHub and connect it at <https://share.streamlit.io> to get a public
shareable link — the equivalent of "publish the dashboard and share it with others."
