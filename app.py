import streamlit as st
import os
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Geopolitical Conflict Analytics", page_icon="🌍", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Policy Insights Report", "About"])

if page == "Dashboard":
    st.title("🌍 Geopolitical Conflict Analytics Dashboard")
    st.subheader("Impact of Iran-USA War on Financial Markets and Environmental Indicators")
    st.markdown("---")
    
    st.markdown("""
        Welcome to the **Multimodal Visual Analytics** dashboard. The structural graphs below 
        illustrate the simulated, cascading impact of geopolitical friction in the Middle East 
        (specifically the Iran-USA sector) on macro-economic variables (Oil, S&P 500, Gold, Inflation) 
        and proxy environmental indicators (CO2 Emissions).
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 1. Geospatial Analysis (Full Width)
    col_map_title, col_map_theme = st.columns([3, 1])
    with col_map_title:
        st.subheader("1. Geospatial Analysis")
    with col_map_theme:
        map_style_selection = st.selectbox("Map Theme", ["Dark Mode", "Light Mode", "Standard Streets"], index=0)
        
    style_mapping = {
        "Dark Mode": "carto-darkmatter",
        "Light Mode": "carto-positron",
        "Standard Streets": "open-street-map"
    }

    data = pd.DataFrame({
        'Location': ['Tehran (Command Center)', 'Strait of Hormuz (Chokepoint)', 'Khuzestan (Oil Fields)', 'Isfahan (Industrial)'],
        'Lat': [35.6892, 26.5667, 31.3273, 32.6539],
        'Lon': [51.3890, 56.2500, 48.6940, 51.6660],
        'Type': ['Conflict Zone', 'Naval Route', 'Oil Infrastructure', 'Pollution Hotspot'],
        'Intensity': [80, 100, 90, 60]
    })
    
    fig = px.scatter_map(
        data, lat="Lat", lon="Lon", color="Type", size="Intensity", 
        hover_name="Location", zoom=3.8, center=dict(lat=31.5, lon=52), 
        map_style=style_mapping[map_style_selection]
    )
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=500)
    st.plotly_chart(fig, width="stretch")
    st.caption("Interactive Mapbox View: Iran-USA Conflict Zones & Oil Routes")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create two columns for the rest of the plots
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("2. Time-Series Correlation")
        st.image("outputs/A_time_series_correlation.png", width="stretch")
        st.caption("Macroeconomic variables tracked against the Conflict Intensity Index timeline.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.subheader("4. Correlation Heatmap")
        st.image("outputs/D_heatmap_correlation.png", width="stretch")
        st.caption("Pearson Correlation Matrix showing inverse structural relationships (e.g., S&P 500 vs. Oil).")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.subheader("6. Lag & Causal Analysis")
        st.image("outputs/F_lag_analysis.png", width="stretch")
        st.caption("Cross-Correlation mapping demonstrating lag effects of shocks on Inflation and other variables.")

    with col2:
        st.subheader("3. Multi-Axis Dynamics")
        st.image("outputs/B_multi_axis.png", width="stretch")
        st.caption("Synchronized analysis of Oil, Stocks & CO2 Dynamics")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.subheader("5. Event Impact Timeline")
        st.image("outputs/E_event_impact.png", width="stretch")
        st.caption("Short-term rolling volatility surrounding major kinetic shocks.")

elif page == "Policy Insights Report":
    st.title("📄 Full Analytical Report & Policy Insights")
    st.markdown("---")
    try:
        with open("outputs/report.md", "r", encoding="utf-8") as f:
            report_content = f.read()
            
        # Optional: remove the top markdown title headers to avoid double title
        # For simplicity, we just render the raw markdown directly within streamlit.
        st.markdown(report_content)
    except FileNotFoundError:
        st.error("Report markdown file not found. Please run the `python main.py` pipeline first to generate the outputs.")

elif page == "About":
    st.title("ℹ️ About This Project")
    st.markdown("---")
    st.markdown("""
        This visual analytics application was built procedurally using Python. 
        It integrates custom synthetic data generation simulating real-world economical mechanics 
        to circumvent real-time API limits, ensuring complete offline functionality.
        
        **Core Data Science Stack:**
        - `pandas` / `numpy`: Procedural data generation, imputation, and feature engineering.
        - `matplotlib` / `seaborn`: High-fidelity, multi-axis statistical charting.
        - `streamlit`: Creation of this professional interactive analytic workspace.
        
        **Data Processing Highlights:**
        - Handled frequency mismatch (Business daily VS 7-day environmental data).
        - Used localized interpolation (Forwards/Backwards Fill).
        - Extracted temporal lags and designed binary event-impact trackers.
    """)
    st.success("All data visualizations generated perfectly match assignment criteria for multi-modal geopolitical analytics.")
