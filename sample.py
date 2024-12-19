import pandas as pd
import random

# Define sample data
data = {
    "SrNo": list(range(1, 11)),
    "Customer Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"],
    "Sales": [round(random.uniform(50, 500), 2) for _ in range(10)],
    "Product Name": ["Product A", "Product B", "Product C", "Product D", "Product E"] * 2,
    "Discount": [round(random.uniform(5, 50), 2) for _ in range(10)],
    "Unit Price": [round(random.uniform(10, 100), 2) for _ in range(10)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate descriptive statistics
description = df.describe()

# Save descriptive statistics to output.csv
description.to_csv("output.csv")

print("Sample data generated and descriptive statistics saved to output.csv")
