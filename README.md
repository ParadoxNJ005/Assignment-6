# Multimodal Visual Analytics of Geopolitical Conflict

**Author:** Krishna Sikheriya  
**Roll Number:** IIT2023139

This project performs a multimodal visual analysis of how the Iran-USA geopolitical conflict (Jan 2023 – Jun 2024) impacts financial markets and environmental indicators, using a hybrid data pipeline and an interactive Streamlit dashboard.

## Project Structure
```
Assignment 6/
├── app.py                  # Streamlit dashboard (interactive UI)
├── main.py                 # Pipeline orchestrator
├── requirements.txt        # Python dependencies
├── src/
│   ├── data_loader.py      # Hybrid data fetcher (Yahoo Finance + synthetic)
│   ├── preprocess.py       # Time alignment & imputation
│   ├── features.py         # Feature engineering pipeline
│   └── visualizations.py   # Chart generation (6 visualizations)
├── data/                   # Generated datasets
├── outputs/                # Charts (PNG) + report (MD) + unified CSV
└── Course/                 # Lecture notes & study materials
```

## Data Sources (Hybrid Strategy)

| Data Variable | Source | Type |
|--------------|--------|------|
| Oil Price (WTI Crude) | Yahoo Finance (`CL=F`) | **Real** |
| S&P 500 Index | Yahoo Finance (`^GSPC`) | **Real** |
| Gold Futures | Yahoo Finance (`GC=F`) | **Real** |
| Conflict Intensity | Procedurally generated | Synthetic (ACLED requires OAuth) |
| CO2 Emissions | Procedurally generated | Synthetic (annual data only) |
| Inflation (CPI) | Procedurally generated | Synthetic (monthly data only) |
| Exchange Rate (IRR) | Procedurally generated | Synthetic (unreliable on Yahoo) |

> **Graceful Fallback:** If Yahoo Finance is unreachable (no internet), all variables automatically fall back to synthetic data.

## How to Run

### 1. Install Dependencies
```bash
python -m venv .venv
.\.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 2. Generate Data & Charts
```bash
python main.py
```
This fetches real financial data from Yahoo Finance and generates all 6 visualizations in `outputs/`.

### 3. Launch the Interactive Dashboard
```bash
streamlit run app.py
```

## Visualizations
1. **Geospatial Map** — Interactive Plotly map of conflict zones & oil chokepoints
2. **Time-Series Correlation** — 3-panel synchronized analysis (Oil vs Stocks vs CO2)
3. **Multi-Axis Dynamics** — Triple Y-axis plot (Oil, Stocks, CO2 on unified timeline)
4. **Correlation Heatmap** — Pearson correlation matrix across all variables
5. **Event Impact Timeline** — Annotated conflict events overlaid on oil prices
6. **Lag & Causal Analysis** — Cross-correlation bar charts for temporal lag detection

## Tech Stack
- **Data Fetching:** `yfinance` (Yahoo Finance API)
- **Data Processing:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`, `plotly`
- **Dashboard:** `streamlit`
