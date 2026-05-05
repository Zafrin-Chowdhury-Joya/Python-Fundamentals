import pandas as pd

df = pd.read_excel("/Users/zafrinchowdhury/Desktop/GTA Automation/Project/Python/07_Data_Structures/05_FileHandling/FileHandlingUsingExcelFile/ReadData.xlsx")

df.at[0, "Name"] = "Hello"

df.to_excel("/Users/zafrinchowdhury/Desktop/GTA Automation/Project/Python/07_Data_Structures/05_FileHandling/FileHandlingUsingExcelFile/WriteData.xlsx", index=False)

print("Excel file updated successfully")