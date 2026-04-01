import os
import sys

# Ensure src is in the python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_loader import generate_synthetic_data
from preprocess import align_and_resample
from features import engineer_features
from visualizations import generate_all_visuals

def main():
    print("=====================================================")
    print("Multimodal Visual Analytics of Geopolitical Conflict")
    print("=====================================================")
    
    # 1. Data Ingestion/Preparation
    print("[1/4] Generating synthetic daily data for conflict timeline...")
    raw_data = generate_synthetic_data(start_date='2023-01-01', end_date='2024-06-30')
    raw_data.to_csv('data/raw_data.csv', index=False)
    
    # 2. Daily Time Alignment
    # The assignment required weekly or daily. The generated dataset is daily. 
    # We will resample to daily to ensure maximum granularity for lag plots.
    # Daily resampling is a no-op if it's already daily, but cleans any gaps.
    print("[2/4] Aligning and resampling data (Daily Frequency)...")
    resampled_data = align_and_resample(raw_data, freq='D')
    
    # 3. Feature Engineering
    print("[3/4] Engineering features (Lags, rolling volatilities, indices)...")
    df_features = engineer_features(resampled_data)
    
    # Save the unified dataset
    unified_csv_path = 'outputs/unified_dataset.csv'
    df_features.to_csv(unified_csv_path)
    print(f"      Unified dataset saved to: {unified_csv_path}")
    
    # 4. Visualizations
    print("[4/4] Generating visualizations...")
    generate_all_visuals(df_features)
    
    print("=====================================================")
    print("Pipeline Execution Complete!")
    print("Check the 'outputs/' directory for charts and data.")
    print("=====================================================")

if __name__ == "__main__":
    main()
