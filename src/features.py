import pandas as pd
import numpy as np

def engineer_features(df):
    """
    Computes essential analytical features like lags, volatility, and conflict impact factors.
    Assumes df is already time-aligned (e.g., daily or weekly).
    """
    df = df.copy()
    
    # 1. Market Volatility Measure (Rolling Standard Deviation)
    window_size = 7 # 7 days if daily, 4 weeks if weekly. Adjust as needed.
    df['Market_Volatility_Measure'] = df['Stock_Index'].rolling(window=window_size).std()
    
    # 2. Oil Shock Indicator (Percentage Change threshold)
    df['Oil_Return'] = df['Oil_Price'].pct_change()
    df['Oil_Shock'] = (df['Oil_Return'] > 0.05).astype(int) # 5% jump
    
    # 3. Lag Features (e.g., Oil causing Stock changes 3-5 days later)
    df['Oil_Lag_3'] = df['Oil_Price'].shift(3)
    df['Oil_Lag_5'] = df['Oil_Price'].shift(5)
    df['Conflict_Lag_7'] = df['Conflict_Intensity'].shift(7)
    
    # 4. Environmental Impact Score (Normalized CO2 inverse, assuming lower CO2 is positive environmental, but indicates economic slowdown)
    # We create a simple robust scaled version of CO2 emissions.
    co2_mean = df['CO2_Emissions'].mean()
    df['Environmental_Impact_Score'] = (df['CO2_Emissions'] / co2_mean) * 100
    
    # 5. Rolling means
    df['Oil_Rolling_Mean'] = df['Oil_Price'].rolling(window=window_size).mean()
    df['Conflict_Smoothing'] = df['Conflict_Intensity'].rolling(window=window_size).mean()
    
    # 6. Event Window Indicator (Active if an event happened recently)
    # If the Event_Flag is not 'None', mark it 1.
    df['Is_Event_Day'] = (df['Event_Flag'] != 'None').astype(int)
    # Create an event window using rolling sum (if any event in past window days, it's an event window)
    df['Event_Active_Window'] = df['Is_Event_Day'].rolling(window=window_size, min_periods=1).max()
    
    # Fill NAs introduced by rolling/shifting
    df.bfill(inplace=True)
    df.fillna(0, inplace=True)
    
    return df

if __name__ == "__main__":
    from preprocess import align_and_resample
    from data_loader import generate_synthetic_data
    
    raw_df = generate_synthetic_data()
    weekly_df = align_and_resample(raw_df, freq='W')
    
    featured_df = engineer_features(weekly_df)
    print("Features created:", featured_df.columns.tolist())
    featured_df.to_csv('../data/featured_dataset.csv')
