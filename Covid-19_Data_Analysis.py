# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Data
# You can replace 'covid_data.csv' with any dataset file path
try:
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
    data = pd.read_csv(url)
    print("Data loaded successfully!")
except:
    print("Failed to load data. Check your URL or file path.")
    exit()

# Step 2: View the Data
print("First 5 rows of the dataset:")
print(data.head())

# Step 3: Analyze Key Statistics
# Select key columns for analysis
columns_of_interest = ["location", "total_cases", "total_deaths", "population"]
covid_data = data[columns_of_interest]

# Remove rows with missing data
covid_data = covid_data.dropna()

# Add a new column: Death rate (deaths per total cases)
covid_data["death_rate"] = (covid_data["total_deaths"] / covid_data["total_cases"]) * 100

# Step 4: Perform Aggregations
# Find the top 10 countries with the most cases
top_countries = covid_data.sort_values(by="total_cases", ascending=False).head(10)

print("\nTop 10 countries with the most cases:")
print(top_countries[["location", "total_cases", "total_deaths", "death_rate"]])

# Step 5: Visualization
# Bar chart: Top 10 countries by total cases
plt.figure(figsize=(10, 6))
plt.bar(top_countries["location"], top_countries["total_cases"], color='skyblue')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line plot: Death rate comparison for the top 10 countries
plt.figure(figsize=(10, 6))
plt.plot(top_countries["location"], top_countries["death_rate"], marker='o', color='red')
plt.title("Death Rate (%) of Top 10 Countries by Cases")
plt.xlabel("Country")
plt.ylabel("Death Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Save the Processed Data
covid_data.to_csv("processed_covid_data.csv", index=False)
print("\nProcessed data saved to 'processed_covid_data.csv'.")
