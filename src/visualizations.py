import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import os
# Create output directories if not exists
os.makedirs('outputs/charts', exist_ok=True)

def set_style():
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams.update({'font.size': 12, 'figure.figsize': (10, 6)})

def plot_time_series_correlation(df, save_path='outputs/charts/A_time_series_correlation.png'):
    """
    A: Plots for Time-series correlation analysis
    - Oil prices vs Stock market
    - Conflict intensity vs Oil price
    - CO2 emissions vs war timeline
    """
    set_style()
    fig, axes = plt.subplots(3, 1, figsize=(14, 18), sharex=True)
    
    # 1. Oil vs Stock
    ax1 = axes[0]
    color = 'tab:red'
    ax1.set_ylabel('Oil Price ($)', color=color)
    ax1.plot(df.index, df['Oil_Price'], color=color, label='Oil Price')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax1_twin = ax1.twinx()
    color2 = 'tab:blue'
    ax1_twin.set_ylabel('Stock Index', color=color2)
    ax1_twin.plot(df.index, df['Stock_Index'], color=color2, label='Stock Index')
    ax1_twin.tick_params(axis='y', labelcolor=color2)
    ax1.set_title('Oil Prices vs Stock Market Index')
    
    # 2. Conflict vs Oil
    ax2 = axes[1]
    color = 'tab:orange'
    ax2.set_ylabel('Conflict Intensity', color=color)
    ax2.plot(df.index, df['Conflict_Intensity'], color=color, label='Conflict Intensity')
    ax2.tick_params(axis='y', labelcolor=color)
    
    ax2_twin = ax2.twinx()
    color2 = 'tab:red'
    ax2_twin.set_ylabel('Oil Price ($)', color=color2)
    ax2_twin.plot(df.index, df['Oil_Price'], color=color2, label='Oil Price', linestyle='--')
    ax2_twin.tick_params(axis='y', labelcolor=color2)
    ax2.set_title('Conflict Intensity vs Oil Price')
    
    # 3. CO2 vs Timeline
    ax3 = axes[2]
    ax3.plot(df.index, df['CO2_Emissions'], color='green', label='CO2 Emissions')
    ax3.set_ylabel('CO2 Emissions proxy')
    ax3.set_title('CO2 Emissions over War Timeline')
    
    # Highlight events
    events = df[df['Is_Event_Day'] == 1].index
    for event_d in events:
        ax3.axvline(x=event_d, color='red', alpha=0.3, linestyle='--')
        
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_multi_axis(df, save_path='outputs/charts/B_multi_axis.png'):
    """
    B: Multi-axis visualization
    Y1: Oil, Y2: Stock, Y3: CO2
    """
    set_style()
    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    # Axis 1
    color1 = 'tab:red'
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Oil Price ($)', color=color1)
    line1, = ax1.plot(df.index, df['Oil_Price'], color=color1, label='Oil Price')
    ax1.tick_params(axis='y', labelcolor=color1)
    
    # Axis 2
    ax2 = ax1.twinx()
    color2 = 'tab:blue'
    ax2.set_ylabel('Stock Index', color=color2)
    line2, = ax2.plot(df.index, df['Stock_Index'], color=color2, label='Stock Index')
    ax2.tick_params(axis='y', labelcolor=color2)
    
    # Axis 3
    ax3 = ax1.twinx()
    # Offset the right spine of ax3
    ax3.spines['right'].set_position(('outward', 60))  
    color3 = 'tab:green'
    ax3.set_ylabel('CO2 Emissions', color=color3)
    line3, = ax3.plot(df.index, df['CO2_Emissions'], color=color3, label='CO2', linestyle='-.')
    ax3.tick_params(axis='y', labelcolor=color3)
    
    fig.tight_layout()
    plt.title('Multi-Axis: Oil Price vs Stock Index vs CO2 Emissions')
    # Add legend
    plt.legend(handles=[line1, line2, line3], loc='upper left')
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_geospatial(save_path='outputs/charts/C_geospatial_map.png'):
    """
    C: Geospatial visualization.
    Generates a static conceptual map using Matplotlib to guarantee 0-second load times
    and avoid heavy HTML/JS iframe delays.
    """
    set_style()
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Conceptual boundary for the Middle East (roughly Lon 40-60, Lat 20-40)
    ax.set_xlim(40, 65)
    ax.set_ylim(22, 40)
    
    # Draw simple grid and styling
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_facecolor('#e8f4f8') # Water color conceptual
    
    # Annotate Land conceptually
    ax.fill_between([40, 65], 22, 40, color='#fdfbf7', alpha=0.8) # Land color
    
    cities = {
        'Tehran (Command Center)': (51.3890, 35.6892, 'red', 800),
        'Strait of Hormuz (Chokepoint)': (56.2500, 26.5667, 'darkorange', 1200),
        'Khuzestan (Oil Fields)': (48.6940, 31.3273, 'purple', 900),
        'Isfahan (Industrial)': (51.6660, 32.6539, 'brown', 600)
    }
    
    for name, (lon, lat, color, size) in cities.items():
        ax.scatter(lon, lat, s=size, c=color, alpha=0.6, edgecolors='black', linewidth=1.5, label=name)
        ax.text(lon + 0.5, lat + 0.5, name, fontsize=11, fontweight='bold', 
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.3'))
                
    plt.title('Geospatial Conceptual View: Iran-USA Conflict Zones & Key Oil Routes', fontsize=14, fontweight='bold')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(loc='lower left', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, facecolor='#f8f9fa')
    plt.close()


def plot_heatmap(df, save_path='outputs/charts/D_heatmap_correlation.png'):
    """
    D: Heatmap correlation matrix
    Among: Oil, Stock, Gold, Inflation, CO2, Exchange Rate, Conflict Intensity
    """
    cols = ['Oil_Price', 'Stock_Index', 'Gold_Price', 'Inflation', 'CO2_Emissions', 'Exchange_Rate', 'Conflict_Intensity']
    corr = df[cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap of the Macroeconomic and Conflict Variables')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_event_impact(df, save_path='outputs/charts/E_event_impact.png'):
    """
    E: Event impact visualization
    Annotate major events on the primary variable (e.g., Oil Price or Conflict Index)
    """
    set_style()
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['Conflict_Intensity'], color='#e74c3c', label='Conflict Intensity', linewidth=1.5)
    plt.plot(df.index, df['Oil_Price'] - df['Oil_Price'].mean() + 20, color='#f39c12', label='Oil Price (centered for viz)')
    
    y_max = df['Conflict_Intensity'].max() + 25
    plt.ylim(-5, y_max)
    
    events = df[df['Event_Flag'] != 'None']
    for idx, row in events.iterrows():
        plt.axvline(x=idx, color='gray', alpha=0.6, linestyle='--')
        plt.text(idx, y_max - 2, f"  {row['Event_Flag']}  ", rotation=90, fontsize=10, 
                 ha='center', va='top', color='#2c3e50', fontweight='bold',
                 bbox=dict(facecolor='#ecf0f1', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.3'))
        
    plt.title('Impact of Major Geopolitical Events on Conflict & Oil', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Intensity / Normalized Price')
    plt.legend(loc='upper right', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_lag_analysis(df, save_path='outputs/charts/F_lag_analysis.png'):
    """
    F: Causal / lag analysis
    Lag plots or cross-correlation charts for Oil -> Stock, Conflict -> Inflation.
    """
    set_style()
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # 1. Cross correlation: Oil vs Stock
    # Instead of ccf (which needs statsmodels), we manually compute correlations at different lags
    lags = range(-10, 11)
    
    oil = df['Oil_Price']
    stock = df['Stock_Index']
    
    corr_oil_stock = [stock.corr(oil.shift(lag)) for lag in lags]
    
    axes[0].bar(lags, corr_oil_stock, color='purple')
    axes[0].set_title('Cross-Correlation: Oil Price & Stock Index (Lag)')
    axes[0].set_xlabel('Lag (Days/Weeks)')
    axes[0].set_ylabel('Correlation Coefficient')
    axes[0].axvline(0, color='black', linestyle='--', linewidth=0.5)
    
    # 2. Cross correlation: Conflict vs Inflation
    conflict = df['Conflict_Intensity']
    inflation = df['Inflation']
    
    corr_conf_inf = [inflation.corr(conflict.shift(lag)) for lag in lags]
    
    axes[1].bar(lags, corr_conf_inf, color='brown')
    axes[1].set_title('Cross-Correlation: Conflict Intensity & Inflation (Lag)')
    axes[1].set_xlabel('Lag (Days/Weeks)')
    axes[1].set_ylabel('Correlation Coefficient')
    axes[1].axvline(0, color='black', linestyle='--', linewidth=0.5)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def generate_all_visuals(df):
    print("Generating Time Series Correlation...")
    plot_time_series_correlation(df)
    print("Generating Multi-Axis Chart...")
    plot_multi_axis(df)
    print("Generating Geospatial Map...")
    plot_geospatial()
    print("Generating Heatmap...")
    plot_heatmap(df)
    print("Generating Event Impact...")
    plot_event_impact(df)
    print("Generating Lag Analysis...")
    plot_lag_analysis(df)
    print("All visualizations successfully generated in /outputs/")
