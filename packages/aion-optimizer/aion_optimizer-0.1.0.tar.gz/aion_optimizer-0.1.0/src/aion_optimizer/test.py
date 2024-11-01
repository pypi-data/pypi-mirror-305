from optimizer import EnhancedSequentialOptimizer
import pandas as pd
from sklearn.model_selection import train_test_split

# Path to your local dataset
dataset_path = "C:/Users/lalit.lohani/Downloads/mushrooms.csv"

print("\n=== Testing===")

# Load the dataset from a CSV file
df = pd.read_csv(dataset_path)

try:
    # Initialize optimizer
    optimizer = EnhancedSequentialOptimizer(
        task_type='classification',
        target_column='class', 
        generations=5,
        cv_folds=5,
        random_state=42,
        n_jobs=-1,
        verbosity=2,
        categorical_threshold=10
    )

    # Split data for final evaluation
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Fit the optimizer
    optimizer.fit(train_df)

    # Get the best model parameters and print them
    results = optimizer.best_model_params(test_df)
    print(results)

except Exception as e:
    print(f"An error occurred: {str(e)}")
    raise
