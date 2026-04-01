# Multimodal Visual Analytics of Geopolitical Conflict

**Author:** Krishna Sikheriya  
**Roll Number:** IIT2023139

This repository contains the full end-to-end Python solution for the Multimodal Visual Analytics assignment evaluating the impact of the Iran-USA War on financial markets and environmental indicators.

## Project Structure
- `data/`: Extracted raw and processed synthetic datasets.
- `outputs/`: Output charts (A-F), CSV unified dataset, and the generated Report (`report.md`).
- `src/`: Core Python modules for generating data, preprocessing, feature engineering, and visualization.
- `main.py`: The orchestrator script.

## System Requirements
- Python 3.8+
- Required libraries are included in the environment setup: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`.

## How to Run
1. Ensure you have Python installed.
2. Open a terminal in the project root directory (`Assignment 6`).
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install pandas numpy matplotlib seaborn plotly
   ```
4. Run the main orchestrator script to generate the static files:
   ```bash
   python main.py
   ```
5. **(New) Run the interactive Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```
6. Navigate to the `outputs/` folder to view the generated static PNG/HTML visualizing charts and the `report.md`.

## Features
- **Reproducible Data**: Uses a realistic, fully procedural synthetic timeline spanning 2023-2024 to mimic Iran-USA conflict events without requiring paid live API keys.
- **Complete Pipeline**: Includes daily time alignment, missing value interpolation, rolling volatility tracking, and 7-day impact lags.

*Note: As per assignment guidelines, realistic demo data has been utilized to ensure the project runs seamlessly offline for evaluation without the risk of API deprecation or rate limits.*
