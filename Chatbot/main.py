import pandas as pd

# Specify the path to the Excel file
excel_file = "C:\\Users\\ukmak\\PycharmProjects\\CMPG313_Chatbot\\ClassTimes.xlsx"

# Read the Excel file into a Pandas DataFrame
dataframe = pd.read_excel(excel_file)

# Convert the DataFrame to a CSV file
dataframe.to_csv("C:\\Users\\ukmak\\PycharmProjects\\CMPG313_Chatbot\\ClassTimes.csv", index=False)
