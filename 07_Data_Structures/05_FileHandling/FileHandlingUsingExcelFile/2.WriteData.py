# Import pandas library (used for data manipulation)
import pandas as pd

# Create a dictionary (data in key-value format)
data = {
    "Name": ["Zafrin", "Joya", "Zoei"],  # Column 1
    "Age": [25, 26, 27]                 # Column 2
}

# Convert dictionary into a DataFrame (tabular format)
df = pd.DataFrame(data)

# Export DataFrame to an Excel file
# index=False → prevents writing row index in Excel
df.to_excel("WriteData.xlsx", index=False)