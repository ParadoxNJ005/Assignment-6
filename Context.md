# Project Context: Multimodal Visual Analytics of Geopolitical Conflict

**Author:** Krishna Sikheriya (IIT2023139)
**Course Assignment:** Data Visualization Assignment 6
**Scenario Analyzed:** The cascading impact of the Iran-USA geopolitical conflict (January 2023 - July 2024) on macroeconomic variables (Oil, S&P 500, Gold, Inflation, Exchange Rate) and proxy environmental indicators (local CO2 emissions).

---

## 1. Core Decisions & Philosophy
When an AI agent interacts with this workspace, it must understand the core architectural intent:
*   **Zero-Dependency Data (Synthetic API Bypass):** To ensure this project is 100% runnable offline by grading evaluators without requiring paid API keys or hitting live rate-limits, we procedurally generated a realistic daily timeline.
*   **Time-Alignment Engine:** Financial markets trade 5 days a week (excluding holidays), while environmental data (CO2) is typically 7-day continuous or weekly. We enforced a strict daily timeline index using forward-filling (`ffill()`) and backward filling to ensure structural continuity before computing correlations.
*   **Modern Interactive Dashboarding:** The final deliverable is an aesthetic, glass-morphism Streamlit Application (`app.py`) built to house the visualizations seamlessly alongside the written analytical report.
*   **Warning Handling:** The project uses `plotly.express.scatter_map` explicitly (not the deprecated `scatter_mapbox`), and specifies Streamlit `width="stretch"` instead of the deprecated `use_container_width`.

---

## 2. File & Directory Architecture
The repository strictly adheres to a modular Data Science framework:

*   **`main.py`**: The overarching pipeline orchestrator. It triggers data loading, preprocessing, feature extraction, and finally the static chart builder.
*   **`app.py`**: The Streamlit user interface. This is the entry point for viewing the interactive dashboard. Requires `streamlit run app.py` to start.
*   **`src/`**: The core computational modules.
    *   **`data_loader.py`**: The procedural data generation engine. It simulates baseline trends, injects specific geopolitical shocks (e.g., Airstrikes, Strait of Hormuz closure threats), applies geometric decay to the shocks, and generates the raw metrics.
    *   **`preprocess.py`**: Handles datetime alignment and interpolation (NaN bridging).
    *   **`features.py`**: Extracts high-level analytical variables including 7-day rolling market volatility, binary `Oil_Shock` flags, and time-lagged variables (`Lag_1` to `Lag_7`).
    *   **`visualizations.py`**: Houses the strict Matplotlib/Seaborn plotting logic for the static PNGs. (The map visualization logic was extracted to Streamlit directly to make it interactive).
*   **`outputs/`**: The target director for all generated artifacts. Contains the `unified_dataset.csv`, the 6 requested `.png` charts, and the `report.md`.

---

## 3. The 6 Multi-modal Visualizations
To fulfill the assignment criteria, the dashboard relies on 6 rigorously defined charts:
1.  **Geospatial Analysis (Interactive)**: An interactive Plotly `scatter_map` charting conflict zones (Tehran, Isfahan) and choke points (Strait of Hormuz). *Note: The background tile server is completely dynamically selectable (Dark/Light/Street carto tiles) by the user in Streamlit to prevent stylistic clashing.*
2.  **Time-Series Correlation (`outputs/A_time_series_correlation.png`)**: A structurally stacked 3-pane plot graphing Oil vs. Stock Indices, Conflict vs. Oil, and CO2 emissions over the war timeline.
3.  **Multi-Axis Dynamics (`outputs/B_multi_axis.png`)**: A perfectly synchronized graph scaling Oil, Stocks, and CO2 against a single unified x-axis utilizing multi-spine Matplotlib formatting.
4.  **Correlation Heatmap (`outputs/D_heatmap_correlation.png`)**: A Pearson correlation matrix defining the inverse relationships between macroeconomic anchors and conflict spikes.
5.  **Event Impact Timeline (`outputs/E_event_impact.png`)**: Conflict events strictly tracked via vertical lines (`axvline`). *Note: Event labels are pinned to the absolute top of the y-axis (`y_max`) and rotated 90 degrees strictly vertically within white frosted bounding boxes (`bbox`) to guarantee absolutely no overlap/clipping.*
6.  **Lag & Causal Analysis (`outputs/F_lag_analysis.png`)**: Cross-correlation bar charts mapping the delayed lag effects of kinetic impacts on variables like Inflation.

---

## 4. Current State for Future AI Assistance
If you are reading this as a fresh AI in a new conversation: 
*   The project is **100% complete**, heavily debugged, and functioning beautifully. 
*   Do not overwrite `src/visualizations.py` with generic code mapping or old depreciated syntax (`scatter_mapbox`). 
*   The virtual environment structure operates heavily under PowerShell; on Windows, remember the user's venv was detected under `.venv\bin\Activate.ps1` (Unix-like subsystem) rather than the standard `Scripts` folder. 
*   If instructed to modify the dashboard UI (`app.py`), ensure changes align with a highly professional, dark/light aware aesthetic.
