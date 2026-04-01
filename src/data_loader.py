import pandas as pd
import numpy as np

def generate_synthetic_data(start_date='2023-01-01', end_date='2024-06-30'):
    """
    Generates a synthetic daily dataset mimicking the economic and environmental
    impact of an Iran-USA geopolitical conflict.
    """
    np.random.seed(42)  # For reproducibility
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    n = len(dates)
    
    # Base series
    data = pd.DataFrame({
        'Date': dates,
        'Conflict_Intensity': np.zeros(n),
        'Oil_Price': 75.0 + np.cumsum(np.random.normal(0, 0.5, n)),
        'Stock_Index': 4000.0 + np.cumsum(np.random.normal(0.5, 10, n)),
        'Gold_Price': 1800.0 + np.cumsum(np.random.normal(0.2, 2, n)),
        'CO2_Emissions': 35.0 + np.sin(np.linspace(0, 4*np.pi, n)) + np.random.normal(0, 0.1, n), # MtCO2/day proxy
        'Inflation': 3.0 + np.cumsum(np.random.normal(0, 0.01, n)), # Annualized %
        'Exchange_Rate': 42000.0 + np.cumsum(np.random.normal(10, 50, n)) # Mock IRR rate proxy
    })
    
    # Define major events
    events = {
        '2023-04-10': ('Airstrikes', 60),
        '2023-08-15': ('Oil facility attacks', 85),
        '2023-11-20': ('Strait closure threats', 70),
        '2024-02-10': ('Major naval standoff', 90)
    }
    
    data['Event_Flag'] = 'None'
    
    for event_date_str, (event_name, intensity_spike) in events.items():
        try:
            event_idx = data[data['Date'] == pd.to_datetime(event_date_str)].index[0]
            # Conflict intensity spike
            data.loc[event_idx, 'Conflict_Intensity'] = intensity_spike
            data.loc[event_idx, 'Event_Flag'] = event_name
            
            # Impact window (decay over 30 days)
            for i in range(1, 40):
                if event_idx + i < n:
                    decay = np.exp(-i / 10.0)
                    data.loc[event_idx + i, 'Conflict_Intensity'] += intensity_spike * decay
                    
                    # Oil spikes immediately and decays slowly
                    data.loc[event_idx + i, 'Oil_Price'] += (intensity_spike / 10.0) * decay
                    
                    # Stocks drop
                    data.loc[event_idx + i, 'Stock_Index'] -= (intensity_spike * 1.5) * decay
                    
                    # Gold rises (safe haven)
                    data.loc[event_idx + i, 'Gold_Price'] += (intensity_spike / 2.0) * decay
                    
                    # Inflation creeps up slightly later
                    data.loc[event_idx + i, 'Inflation'] += (intensity_spike / 1000.0) * (1 - decay)
                    
                    # CO2 drops due to disrupted logistics/oil burning offset
                    data.loc[event_idx + i, 'CO2_Emissions'] -= (intensity_spike / 50.0) * decay
        except IndexError:
            pass # Date not in range
            
    # Add random daily noise to conflict intensity, clip to 0-100
    data['Conflict_Intensity'] += np.random.normal(5, 5, n)
    data['Conflict_Intensity'] = data['Conflict_Intensity'].clip(0, 100)
    
    return data

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv('../data/mock_conflict_data.csv', index=False)
    print("Synthetic dataset generated: mock_conflict_data.csv")
