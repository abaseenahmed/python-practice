"""
Weather Data Analysis Project
A simple program that generates and analyzes weather data for a city
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ===================== PART 1: DATA GENERATION =====================

# Set seed for reproducible results
np.random.seed(42)

# Generate weather data for 365 days (one year)
def generate_weather_data():
    """
    Create synthetic weather data for one year
    Returns: DataFrame with daily weather information
    """
    # Create date range
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    
    # Generate temperatures (Celsius) with seasonal pattern
    # Winter: cold, Summer: hot
    day_of_year = np.arange(1, 366)
    seasonal_temp = 15 + 10 * np.sin((day_of_year - 80) * 2 * np.pi / 365)
    
    # Add random variation
    temperatures = seasonal_temp + np.random.normal(0, 5, 365)
    temperatures = np.round(temperatures, 1)
    
    # Generate rainfall (mm)
    # More rain in spring and fall
    rainfall_base = 2 + 3 * np.sin((day_of_year - 100) * 2 * np.pi / 365)**2
    rainfall = rainfall_base + np.random.exponential(1, 365)
    rainfall = np.round(rainfall.clip(0, 20), 1)
    
    # Generate humidity (%)
    humidity = 60 + 20 * np.sin((day_of_year - 120) * 2 * np.pi / 365)
    humidity = humidity + np.random.normal(0, 8, 365)
    humidity = np.round(humidity.clip(20, 100), 1)
    
    # Generate wind speed (km/h)
    wind_speed = 15 + 8 * np.sin((day_of_year - 60) * 2 * np.pi / 365)
    wind_speed = wind_speed + np.random.normal(0, 4, 365)
    wind_speed = np.round(wind_speed.clip(0, 45), 1)
    
    # Generate pressure (hPa)
    pressure = 1013 + 10 * np.sin((day_of_year - 40) * 2 * np.pi / 365)
    pressure = pressure + np.random.normal(0, 5, 365)
    pressure = np.round(pressure, 1)
    
    # Weather conditions based on combination of factors
    conditions = []
    for i in range(365):
        if rainfall[i] > 10 and temperatures[i] < 10:
            conditions.append('Rainy & Cold')
        elif rainfall[i] > 10:
            conditions.append('Rainy')
        elif temperatures[i] > 25 and humidity[i] > 70:
            conditions.append('Hot & Humid')
        elif temperatures[i] > 25:
            conditions.append('Hot')
        elif temperatures[i] < 5:
            conditions.append('Freezing')
        else:
            conditions.append('Pleasant')
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Temperature': temperatures,
        'Rainfall': rainfall,
        'Humidity': humidity,
        'WindSpeed': wind_speed,
        'Pressure': pressure,
        'Condition': conditions
    })
    
    # Add month and season columns
    df['Month'] = df['Date'].dt.month
    df['Season'] = df['Month'].apply(lambda x: 
        'Winter' if x in [12, 1, 2] else
        'Spring' if x in [3, 4, 5] else
        'Summer' if x in [6, 7, 8] else 'Fall'
    )
    
    return df

# Generate the dataset
weather_df = generate_weather_data()

# ===================== PART 2: DATA ANALYSIS =====================

print("=" * 70)
print("WEATHER DATA ANALYSIS PROJECT")
print("=" * 70)

# Basic statistics
print("\n📊 BASIC STATISTICS")
print("-" * 70)
print(f"Total days analyzed: {len(weather_df)}")
print(f"Date range: {weather_df['Date'].min().strftime('%B %d, %Y')} to {weather_df['Date'].max().strftime('%B %d, %Y')}")

# Summary statistics for numerical columns
numeric_cols = ['Temperature', 'Rainfall', 'Humidity', 'WindSpeed', 'Pressure']
print("\n📈 NUMERICAL SUMMARY:")
print(weather_df[numeric_cols].describe().round(2))

# Seasonal averages
print("\n🌡️ SEASONAL AVERAGES:")
seasonal_stats = weather_df.groupby('Season')[numeric_cols].mean().round(2)
print(seasonal_stats)

# Weather condition distribution
print("\n☁️ WEATHER CONDITIONS:")
condition_counts = weather_df['Condition'].value_counts()
print(condition_counts)

# Find extreme weather days
print("\n🌪️ EXTREME WEATHER DAYS:")
print("Hottest day:")
hottest = weather_df.loc[weather_df['Temperature'].idxmax()]
print(f"  {hottest['Date'].strftime('%B %d')}: {hottest['Temperature']}°C")

print("Coldest day:")
coldest = weather_df.loc[weather_df['Temperature'].idxmin()]
print(f"  {coldest['Date'].strftime('%B %d')}: {coldest['Temperature']}°C")

print("Rainiest day:")
rainiest = weather_df.loc[weather_df['Rainfall'].idxmax()]
print(f"  {rainiest['Date'].strftime('%B %d')}: {rainiest['Rainfall']}mm rain")

# Correlation analysis
print("\n🔗 CORRELATION MATRIX:")
correlation = weather_df[numeric_cols].corr().round(3)
print(correlation)

# ===================== PART 3: DATA VISUALIZATION =====================

# Create figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Weather Analysis Dashboard', fontsize=18, fontweight='bold')

# 1. Temperature trend over the year
ax1 = axes[0, 0]
ax1.plot(weather_df['Date'], weather_df['Temperature'], color='red', alpha=0.7, linewidth=1)
ax1.set_title('Temperature Trend', fontsize=12)
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=weather_df['Temperature'].mean(), color='red', linestyle='--', 
            alpha=0.5, label=f"Mean: {weather_df['Temperature'].mean():.1f}°C")
ax1.legend()

# 2. Rainfall distribution
ax2 = axes[0, 1]
ax2.hist(weather_df['Rainfall'], bins=20, color='blue', alpha=0.7, edgecolor='black')
ax2.set_title('Rainfall Distribution', fontsize=12)
ax2.set_xlabel('Rainfall (mm)')
ax2.set_ylabel('Number of Days')
ax2.grid(True, alpha=0.3)

# 3. Weather conditions pie chart
ax3 = axes[0, 2]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
wedges, texts, autotexts = ax3.pie(condition_counts.values, 
                                    labels=condition_counts.index,
                                    autopct='%1.1f%%',
                                    colors=colors[:len(condition_counts)],
                                    startangle=90)
ax3.set_title('Weather Condition Distribution', fontsize=12)

# 4. Monthly averages
ax4 = axes[1, 0]
monthly_avg = weather_df.groupby('Month')['Temperature'].mean()
ax4.bar(monthly_avg.index, monthly_avg.values, color='orange', alpha=0.7, edgecolor='black')
ax4.set_title('Average Temperature by Month', fontsize=12)
ax4.set_xlabel('Month')
ax4.set_ylabel('Temperature (°C)')
ax4.set_xticks(range(1, 13))
ax4.grid(True, alpha=0.3, axis='y')

# 5. Scatter plot: Temperature vs Humidity
ax5 = axes[1, 1]
scatter = ax5.scatter(weather_df['Temperature'], weather_df['Humidity'], 
                      c=weather_df['Rainfall'], cmap='Blues', 
                      s=30, alpha=0.6, edgecolors='black', linewidth=0.5)
ax5.set_title('Temperature vs Humidity (colored by Rainfall)', fontsize=12)
ax5.set_xlabel('Temperature (°C)')
ax5.set_ylabel('Humidity (%)')
ax5.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax5, label='Rainfall (mm)')

# 6. Seasonal boxplot
ax6 = axes[1, 2]
seasonal_data = [weather_df[weather_df['Season'] == s]['Temperature'] for s in ['Winter', 'Spring', 'Summer', 'Fall']]
bp = ax6.boxplot(seasonal_data, labels=['Winter', 'Spring', 'Summer', 'Fall'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['#3498DB', '#2ECC71', '#E74C3C', '#F39C12']):
    patch.set_facecolor(color)
ax6.set_title('Temperature Distribution by Season', fontsize=12)
ax6.set_ylabel('Temperature (°C)')
ax6.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('weather_analysis_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

# ===================== PART 4: SAVE RESULTS =====================

# Save the data to CSV
weather_df.to_csv('weather_data.csv', index=False)
print(f"\n✅ Data saved to 'weather_data.csv'")
print(f"✅ Visualization saved to 'weather_analysis_dashboard.png'")

# Extra: Monthly summary
print("\n📅 MONTHLY SUMMARY:")
monthly_summary = weather_df.groupby('Month').agg({
    'Temperature': ['mean', 'min', 'max'],
    'Rainfall': 'mean',
    'Condition': lambda x: x.mode().iloc[0]  # Most common condition
}).round(2)
print(monthly_summary)

print("\n" + "=" * 70)
print("🎉 Analysis Complete! Explore the generated data and visualizations.")
print("=" * 70)