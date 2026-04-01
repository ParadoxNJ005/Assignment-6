# Multimodal Visual Analytics of Geopolitical Conflict

**Author:** Krishna Sikheriya  
**Roll Number:** IIT2023139

---

## Overview
This project performs a multimodal visual analysis of how the Iran-USA geopolitical conflict (Jan 2023 – Jun 2024) impacts financial markets and environmental indicators, using a hybrid real + synthetic data pipeline and an interactive Streamlit dashboard.

## Project Structure
```
├── app.py                          # Streamlit dashboard (entry point)
├── main.py                         # Pipeline orchestrator (entry point)
├── requirements.txt                # Python dependencies
│
├── src/                            # Core pipeline modules
│   ├── __init__.py
│   ├── data_loader.py              # Hybrid data fetcher (Yahoo Finance + synthetic)
│   ├── preprocess.py               # Time alignment & missing value imputation
│   ├── features.py                 # Feature engineering (lags, volatility, shocks)
│   └── visualizations.py           # Chart generation (6 visualizations)
│
├── data/
│   ├── raw/                        # Raw ingested data
│   │   └── raw_data.csv
│   └── processed/                  # Engineered unified dataset
│       └── unified_dataset.csv
│
├── outputs/
│   ├── charts/                     # Generated visualizations (PNG)
│   │   ├── A_time_series_correlation.png
│   │   ├── B_multi_axis.png
│   │   ├── C_geospatial_map.png
│   │   ├── D_heatmap_correlation.png
│   │   ├── E_event_impact.png
│   │   └── F_lag_analysis.png
│   └── report.md                   # Analytical report
│
├── docs/                           # Documentation & screenshots
│   ├── report.md                   # Full analytical report
│   └── screenshots/                # Dashboard screenshots
│
└── .gitignore
```

## Data Sources (Hybrid)

| Variable | Source | Type |
|----------|--------|------|
| Oil Price (WTI Crude) | Yahoo Finance (`CL=F`) | **Real** |
| S&P 500 Index | Yahoo Finance (`^GSPC`) | **Real** |
| Gold Futures | Yahoo Finance (`GC=F`) | **Real** |
| Conflict Intensity | Procedural model | Synthetic |
| CO2 Emissions | Procedural model | Synthetic |
| Inflation (CPI) | Procedural model | Synthetic |
| Exchange Rate (IRR) | Procedural model | Synthetic |

> If Yahoo Finance is unreachable, the pipeline gracefully falls back to synthetic data for all variables.

## Quick Start

```bash
# 1. Create virtual environment & install dependencies
python -m venv .venv
.\.venv\Scripts\activate          # Windows
pip install -r requirements.txt

# 2. Run the pipeline (fetches real data + generates charts)
python main.py

# 3. Launch the interactive dashboard
streamlit run app.py
```

## Visualizations
1. **Geospatial Map** — Interactive Plotly map of conflict zones & oil chokepoints
2. **Time-Series Correlation** — 3-panel synchronized analysis (Oil vs Stocks vs CO2)
3. **Multi-Axis Dynamics** — Triple Y-axis plot on unified timeline
4. **Correlation Heatmap** — Pearson correlation matrix
5. **Event Impact Timeline** — Annotated conflict events overlaid on oil prices
6. **Lag & Causal Analysis** — Cross-correlation bar charts for temporal lag detection

## Tech Stack
| Category | Libraries |
|----------|----------|
| Data Fetching | `yfinance` |
| Data Processing | `pandas`, `numpy` |
| Visualization | `matplotlib`, `seaborn`, `plotly` |
| Dashboard | `streamlit` |
