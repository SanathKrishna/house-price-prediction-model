import pandas as pd

def preprocess_data(input_path="data/housing_raw.csv", output_path="data/housing.csv"):
    df = pd.read_csv(input_path)
    
    # Handle missing values
    df.fillna(df.mean(), inplace=True)
    
    # Convert categorical variables
    df = pd.get_dummies(df, drop_first=True)
    
    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()