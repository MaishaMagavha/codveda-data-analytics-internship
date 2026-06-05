# Codveda Technology — Data Analytics Internship

Complete submission for the Codveda Data Analytics internship. **All 9 tasks** across the
three levels are implemented (the brief only requires 2 per level — this repo does every
one). Each level is delivered as a self-contained, fully-executed Jupyter notebook with all
figures also exported as PNGs, plus a separate interactive dashboard for Level 3.

> **Domain:** Data Analytics · **Tools:** Python, pandas, scikit-learn, statsmodels,
> matplotlib/seaborn, nltk/TextBlob, Streamlit + Plotly.

## Structure

```
Submission/
├── README.md                ← you are here
├── requirements.txt
├── Level-1/
│   ├── Level1_Basic.ipynb            # Data cleaning · EDA · Visualization
│   ├── cleaned_sentiment.csv         # output of the cleaning task
│   └── outputs/                      # exported figures (PNG)
├── Level-2/
│   ├── Level2_Intermediate.ipynb     # Regression · Time series · Clustering
│   └── outputs/
└── Level-3/
    ├── Level3_Advanced.ipynb         # Classification · NLP sentiment
    ├── outputs/
    └── dashboard/                    # Task 2: interactive dashboard
        ├── app.py
        └── README.md
```

> **Datasets** live in the sibling `../Data Set For Task/` folder (kept outside the repo
> because the stock-price file is ~24 MB). The notebooks reference it relatively, with an
> absolute-path fallback. Keep that folder next to `Submission/` and everything runs.

## Tasks completed

### Level 1 — Basic → [`Level-1/Level1_Basic.ipynb`](Level-1/Level1_Basic.ipynb)
1. **Data Cleaning & Preprocessing** — sentiment dataset: drop redundant columns, strip
   whitespace, impute missing values, dedup, standardize dates & categorical labels.
2. **Exploratory Data Analysis** — iris: summary stats (mean/median/mode/std), histograms,
   boxplots, correlation heatmap, pairplot.
3. **Basic Visualization** — iris: customized bar, line, and scatter charts exported as PNG.

### Level 2 — Intermediate → [`Level-2/Level2_Intermediate.ipynb`](Level-2/Level2_Intermediate.ipynb)
1. **Regression** — Boston housing linear regression; R²/MSE/RMSE; coefficient
   interpretation; predicted-vs-actual plot.
2. **Time Series** — AAPL stock close: trend/seasonal/residual decomposition (statsmodels)
   and 30/90-day moving-average smoothing.
3. **Clustering (K-Means)** — iris: standardized features, elbow method, k=3 clusters,
   silhouette score, clusters-vs-true-species comparison.

### Level 3 — Advanced → [`Level-3/Level3_Advanced.ipynb`](Level-3/Level3_Advanced.ipynb) + [`Level-3/dashboard/`](Level-3/dashboard/)
1. **Classification** — telecom churn: Logistic Regression, Decision Tree & Random Forest;
   accuracy/precision/recall/F1; confusion matrices; `GridSearchCV` tuning; feature importance.
2. **Dashboard** — interactive **Streamlit + Plotly** churn dashboard with KPI cards,
   charts, a US choropleth map, and sidebar filters/slicers. *(Open-source equivalent of
   Power BI/Tableau, which don't run on Linux — see [dashboard README](Level-3/dashboard/README.md).)*
3. **NLP Sentiment Analysis** — tokenize, remove stopwords, lemmatize (nltk); TextBlob
   polarity classification; sentiment distribution and per-class word clouds.

## How to run

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -c "import nltk; [nltk.download(p) for p in ['punkt','punkt_tab','stopwords','wordnet','omw-1.4']]"

# Notebooks (already executed with outputs embedded; re-run to reproduce):
jupyter notebook            # open any Level-N/Level*.ipynb

# Or execute headless:
jupyter nbconvert --to notebook --execute --inplace Level-1/Level1_Basic.ipynb

# Dashboard:
cd Level-3/dashboard && streamlit run app.py
```

