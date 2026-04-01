import pandas as pd
import numpy as np

def align_and_resample(df, freq='W'):
    """
    Aligns the time scale to a common frequency (e.g., 'W' for weekly, 'D' for daily).
    Cleans missing values and standardizes the dataset.
    """
    df = df.copy()
    
    # Ensure Date is datetime
    if not np.issubdtype(df['Date'].dtype, np.datetime64):
        df['Date'] = pd.to_datetime(df['Date'])
        
    df.set_index('Date', inplace=True)
    
    if freq != 'D':
        # Weekly/Monthly resampling logic
        # For numeric columns, take the mean. 
        # For the categorical event flag, keep the most significant event or None.
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        
        # Aggregation dictionary
        agg_dict = {col: 'mean' for col in numeric_cols}
        
        # Special logic for Event_Flag: if any event occurred in the week, mark it
        resampled_df = df.resample(freq).agg(agg_dict)
        
        # Merge event flags
        def get_events(series):
            events = [e for e in series if e != 'None']
            return ' | '.join(events) if events else 'None'
            
        events_resampled = df['Event_Flag'].resample(freq).apply(get_events)
        resampled_df['Event_Flag'] = events_resampled
        
        df = resampled_df
        
    # Missing value handling (forward fill for financial data, interpolate for others if any)
    df.ffill(inplace=True)
    # Just in case ffill leaves first row NaN
    df.bfill(inplace=True) 
    
    return df

if __name__ == "__main__":
    from data_loader import generate_synthetic_data
    import numpy as np
    
    raw_df = generate_synthetic_data()
    print("Raw daily shape:", raw_df.shape)
    
    weekly_df = align_and_resample(raw_df, freq='W')
    print("Weekly resampled shape:", weekly_df.shape)
    weekly_df.to_csv('../data/processed_weekly_data.csv')
