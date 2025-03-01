import pandas as pd

# Load the datasets
shootings_df = pd.read_csv("fatal_shootings.csv")  # Washington Post fatal shootings dataset
census_df = pd.read_csv("census_data.csv")  # US Census data

# Ensure that the location column is standardized (e.g., lowercased or stripped)
shootings_df['location'] = shootings_df['location'].str.lower()
census_df['county_name'] = census_df['county_name'].str.lower()

# Merge the datasets based on the location (county)
merged_df = pd.merge(shootings_df, census_df, how='inner', left_on='location', right_on='county_name')

# Group by race and gender
race_gender_distribution = merged_df.groupby(['race', 'gender']).size().reset_index(name='count')

# Plot the distribution
import seaborn as sns
sns.countplot(x='race', hue='gender', data=merged_df)

# Group by state or county
shootings_by_location = merged_df.groupby('state')['id'].count().reset_index(name='shootings_count')

# Plot the results
sns.barplot(x='state', y='shootings_count', data=shootings_by_location)

# Correlation analysis
correlation = merged_df[['poverty_rate', 'median_household_income', 'high_school_graduation_rate', 'shootings_count']].corr()

# Visualize the correlations
import matplotlib.pyplot as plt
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.show()

# Convert date to datetime
merged_df['date'] = pd.to_datetime(merged_df['date'])

# Group by year and count shootings
yearly_shootings = merged_df.groupby(merged_df['date'].dt.year)['id'].count()

# Plot the trend over time
plt.plot(yearly_shootings)
plt.title('Fatal Shootings by Police (Yearly Trend)')
plt.xlabel('Year')
plt.ylabel('Number of Shootings')
plt.show()

