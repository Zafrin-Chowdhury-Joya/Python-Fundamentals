import pandas as pd
data = {
    "Name": ["Zafrin", "Joya", "Zoei"],
    "Age": [25, 26, 27]
}


df = pd.DataFrame(data)

df.to_excel("/Users/zafrinchowdhury/Desktop/GTA Automation/Project/Python/07_Data_Structures/05_FileHandling/FileHandlingUsingExcelFile/WriteData.xlsx", index=False)