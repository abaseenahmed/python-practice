import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('WorldExpenditures.csv')
df.drop(columns=["Unnamed: 0"], inplace=True)
seperator = '='*100

print("="*50)
print("WORLD EXPENDITURES ANALYSIS PROJECT")
print("="*50)

# Phase 1: Dataset Inspection & Cleaning
print("\nPhase 1: Dataset Inspection & Cleaning")
print(seperator)

# Task 1: Remove unnecessary column (already done)
print("Task 1: Removed unnecessary column 'Unnamed: 0'")
print(seperator)

# Task 2: Check duplicate rows
print("\nTask 2: Checking for duplicate rows")
duplicate_count = df.duplicated().sum()
print(f"Total duplicate rows: {duplicate_count}")
if duplicate_count > 0:
    df.drop_duplicates(inplace=True)
    print(f"Removed {duplicate_count} duplicate rows")
    print(f"New shape: {df.shape}")
else:
    print("No duplicates found")
print(seperator)

# Task 3: Check missing values
print("\nTask 3: Handling missing values")
print("Missing values before handling:")
print(df.isnull().sum())

# Handle missing values - fill with median for each column
df['Expenditure(million USD)'].fillna(df['Expenditure(million USD)'].median(), inplace=True)
df['GDP(%)'].fillna(df['GDP(%)'].median(), inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum())
print(seperator)

# Task 4: Rename columns
print("\nTask 4: Renaming columns")
df.rename(columns={
    'Expenditure(million USD)': 'Expenditure_USD_Million',
    'GDP(%)': 'GDP_Percentage'
}, inplace=True)
print("Columns renamed:")
print(df.columns.tolist())
print(seperator)

# Phase 2: Basic Analysis
print("\nPhase 2: Basic Analysis")
print(seperator)

# Question 1: How many unique countries exist?
unique_countries = df['Country'].nunique()
print(f"\nQ1: Number of unique countries: {unique_countries}")

# Question 2: How many sectors exist?
unique_sectors = df['Sector'].nunique()
print(f"\nQ2: Number of unique sectors: {unique_sectors}")

# Question 3: Which years are included?
years = sorted(df['Year'].unique())
print(f"\nQ3: Years included: {years}")

# Question 4: Average government expenditure
avg_expenditure = df['Expenditure_USD_Million'].mean()
print(f"\nQ4: Average government expenditure: {avg_expenditure:,.2f} million USD")

# Question 5: Highest expenditure ever recorded
max_expenditure = df.loc[df['Expenditure_USD_Million'].idxmax()]
print(f"\nQ5: Highest expenditure ever recorded:")
print(max_expenditure)

# Question 6: Lowest expenditure
min_expenditure = df.loc[df['Expenditure_USD_Million'].idxmin()]
print(f"\nQ6: Lowest expenditure ever recorded:")
print(min_expenditure)
print(seperator)

# Phase 3: Country Analysis
print("\nPhase 3: Country Analysis")
print(seperator)

# Question 1: Which country spent the most money overall?
country_total_exp = df.groupby('Country')['Expenditure_USD_Million'].sum().sort_values(ascending=False)
print(f"\nQ1: Country that spent the most overall: {country_total_exp.index[0]}")
print(f"Total expenditure: {country_total_exp.iloc[0]:,.2f} million USD")

# Question 2: Top 10 countries by expenditure
print("\nQ2: Top 10 countries by total expenditure:")
print(country_total_exp.head(10))

# Question 3: Bottom 10 countries
print("\nQ3: Bottom 10 countries by total expenditure:")
print(country_total_exp.tail(10))

# Question 4: Average GDP percentage by country
country_avg_gdp = df.groupby('Country')['GDP_Percentage'].mean().sort_values(ascending=False)
print("\nQ4: Average GDP percentage by country (Top 5):")
print(country_avg_gdp.head(5))

# Question 5: Which country has the highest average GDP spending?
print(f"\nQ5: Country with highest average GDP spending: {country_avg_gdp.index[0]}")
print(f"Average GDP percentage: {country_avg_gdp.iloc[0]:.2f}%")
print(seperator)

# Phase 4: Sector Analysis
print("\nPhase 4: Sector Analysis")
print(seperator)

# Question 1: Which sector receives the highest expenditure?
sector_total_exp = df.groupby('Sector')['Expenditure_USD_Million'].sum().sort_values(ascending=False)
print(f"\nQ1: Sector with highest total expenditure: {sector_total_exp.index[0]}")
print(f"Total expenditure: {sector_total_exp.iloc[0]:,.2f} million USD")

# Question 2: Top 10 sectors
print("\nQ2: Top 10 sectors by expenditure:")
print(sector_total_exp.head(10))

# Question 3: Average expenditure per sector
sector_avg_exp = df.groupby('Sector')['Expenditure_USD_Million'].mean().sort_values(ascending=False)
print("\nQ3: Average expenditure per sector (Top 5):")
print(sector_avg_exp.head(5))

# Question 4: Which sector has the highest GDP percentage?
sector_avg_gdp = df.groupby('Sector')['GDP_Percentage'].mean().sort_values(ascending=False)
print(f"\nQ4: Sector with highest average GDP percentage: {sector_avg_gdp.index[0]}")
print(f"Average GDP percentage: {sector_avg_gdp.iloc[0]:.2f}%")
print(seperator)

# Phase 5: Year Analysis
print("\nPhase 5: Year Analysis")
print(seperator)

# Question 1: How has spending changed every year?
yearly_total_exp = df.groupby('Year')['Expenditure_USD_Million'].sum()
print("\nQ1: Yearly spending trends:")
print(yearly_total_exp)

# Question 2: Which year had the highest total expenditure?
max_year = yearly_total_exp.idxmax()
print(f"\nQ2: Year with highest total expenditure: {max_year}")
print(f"Total expenditure: {yearly_total_exp[max_year]:,.2f} million USD")

# Question 3: Which year had the lowest?
min_year = yearly_total_exp.idxmin()
print(f"\nQ3: Year with lowest total expenditure: {min_year}")
print(f"Total expenditure: {yearly_total_exp[min_year]:,.2f} million USD")

# Question 4: Average expenditure every year
yearly_avg_exp = df.groupby('Year')['Expenditure_USD_Million'].mean()
print("\nQ4: Average expenditure per year (Top 5):")
print(yearly_avg_exp.head(5))
print(seperator)

# Phase 6: Combined Analysis
print("\nPhase 6: Combined Analysis")
print(seperator)

# Question 1: For every country, find the sector with the highest expenditure
print("\nQ1: For every country, sector with highest expenditure (showing first 5):")
top_sector_by_country = df.loc[df.groupby('Country')['Expenditure_USD_Million'].idxmax()]
print(top_sector_by_country[['Country', 'Sector', 'Expenditure_USD_Million']].head(5))

# Question 2: For every year, find the country spending the most
print("\nQ2: For every year, country spending the most (showing first 5):")
top_country_by_year = df.loc[df.groupby('Year')['Expenditure_USD_Million'].idxmax()]
print(top_country_by_year[['Year', 'Country', 'Expenditure_USD_Million']].head(5))

# Question 3: Find countries whose average expenditure is above the global average
global_avg_exp = df['Expenditure_USD_Million'].mean()
country_avg_exp = df.groupby('Country')['Expenditure_USD_Million'].mean()
above_avg_countries = country_avg_exp[country_avg_exp > global_avg_exp]
print(f"\nQ3: Countries with average expenditure above global average ({global_avg_exp:,.2f}):")
print(f"Number of countries: {len(above_avg_countries)}")
print(above_avg_countries.head(10))

# Question 4: Find sectors whose average GDP percentage exceeds 5%
sector_avg_gdp = df.groupby('Sector')['GDP_Percentage'].mean()
high_gdp_sectors = sector_avg_gdp[sector_avg_gdp > 5]
print(f"\nQ4: Sectors with average GDP percentage > 5%:")
print(high_gdp_sectors)
print(seperator)

# Phase 7: Filtering
print("\nPhase 7: Filtering Practice")
print(seperator)

# Various filters
exp_high = df[df['Expenditure_USD_Million'] > 100000]
print(f"\nRecords with expenditure > 100,000 million USD: {len(exp_high)}")

gdp_high = df[df['GDP_Percentage'] > 10]
print(f"\nRecords with GDP percentage > 10%: {len(gdp_high)}")

# Check if Pakistan exists
pakistan_records = df[df['Country'] == 'Pakistan']
if len(pakistan_records) > 0:
    print(f"\nRecords from Pakistan: {len(pakistan_records)}")
else:
    print("\nNo records from Pakistan found")

# Records after 2015
after_2015 = df[df['Year'] > 2015]
print(f"\nRecords after 2015: {len(after_2015)}")

# Sector-specific filters
transport = df[df['Sector'] == 'Transport']
print(f"\nTransport sector records: {len(transport)}")

education = df[df['Sector'] == 'Education']
print(f"Education sector records: {len(education)}")

health = df[df['Sector'] == 'Health']
print(f"Health sector records: {len(health)}")

# Australia specific filters
australia = df[df['Country'] == 'Australia']
print(f"\nAustralia records: {len(australia)}")

australia_after_2010 = australia[australia['Year'] > 2010]
print(f"Australia records after 2010: {len(australia_after_2010)}")

australia_transport = australia[australia['Sector'] == 'Transport']
print(f"Australia Transport sector records: {len(australia_transport)}")
print(seperator)

# Phase 8: Create New Columns
print("\nPhase 8: Creating New Columns - Expenditure_Level")
print(seperator)

def categorize_expenditure(exp):
    if exp > 100000:
        return 'Very High'
    elif exp >= 50000:
        return 'High'
    elif exp >= 10000:
        return 'Medium'
    else:
        return 'Low'

df['Expenditure_Level'] = df['Expenditure_USD_Million'].apply(categorize_expenditure)

print("\nExpenditure Level distribution:")
print(df['Expenditure_Level'].value_counts())
print(seperator)

# Phase 9: Export Reports
print("\nPhase 9: Exporting Reports")
print(seperator)

# Export Top 10 Countries
top_10_countries = country_total_exp.head(10).reset_index()
top_10_countries.columns = ['Country', 'Total_Expenditure_USD_Million']
top_10_countries.to_csv('Top_10_Countries.csv', index=False)
print("✓ Exported: Top_10_Countries.csv")

# Export Top 10 Sectors
top_10_sectors = sector_total_exp.head(10).reset_index()
top_10_sectors.columns = ['Sector', 'Total_Expenditure_USD_Million']
top_10_sectors.to_csv('Top_10_Sectors.csv', index=False)
print("✓ Exported: Top_10_Sectors.csv")

# Export Australia Report
australia_report = australia.sort_values('Year')
australia_report.to_csv('Australia_Report.csv', index=False)
print("✓ Exported: Australia_Report.csv")

# Export Full World Analysis
df.to_csv('World_Analysis.csv', index=False)
print("✓ Exported: World_Analysis.csv")

print(seperator)

# Final Report with Observations
print("\n" + "="*50)
print("FINAL REPORT: KEY OBSERVATIONS")
print("="*50)

observations = [
    "# The United States accounts for the highest government expenditure.",
    "# Transport and Health are consistently among the largest spending sectors.",
    "# Government expenditure generally increased after 2010.",
    "# Some sectors contribute only a very small percentage of GDP.",
    f"# Total number of countries analyzed: {unique_countries}",
    f"# Total number of sectors analyzed: {unique_sectors}",
    f"# Global average expenditure: {global_avg_exp:,.2f} million USD",
    f"# Highest expenditure country: {country_total_exp.index[0]} ({country_total_exp.iloc[0]:,.2f} million USD)",
    f"# Highest expenditure sector: {sector_total_exp.index[0]} ({sector_total_exp.iloc[0]:,.2f} million USD)",
    f"# Year with highest total expenditure: {max_year}",
    f"# Year with lowest total expenditure: {min_year}",
    f"# Number of countries with above-average expenditure: {len(above_avg_countries)}"
]

for obs in observations:
    print(obs)

print("\n" + "="*50)
print("ANALYSIS COMPLETE")
print("="*50)

