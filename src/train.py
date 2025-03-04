# train.py - Script to train a simple ML model
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def train_model():
    # Load dataset
    df = pd.read_csv("data/housing.csv")
    X = df.drop("price", axis=1)
    y = df["price"]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    print(f"Model R2 Score: {r2_score(y_test, y_pred):.2f}")
    
    # Save model
    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train_model()
