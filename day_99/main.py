import pandas as pd
import matplotlib.pyplot as plt

# Load the data (assuming it's in a CSV file)
data = pd.read_csv('space_missions.csv')

# Extract the year from the 'launch_date' column
data['year'] = pd.to_datetime(data['launch_date']).dt.year

# Group by year and country to count launches
launch_counts = data.groupby(['year', 'country']).size().reset_index(name='launch_count')

# Find the country with the most launches each year
max_launches_per_year = launch_counts.loc[launch_counts.groupby('year')['launch_count'].idxmax()]

# Plot the results
plt.figure(figsize=(10,6))
for year in max_launches_per_year['year'].unique():
    year_data = max_launches_per_year[max_launches_per_year['year'] == year]
    plt.plot(year_data['year'], year_data['launch_count'], marker='o', label=f"{year} - {year_data['country'].values[0]}")

plt.title('Countries with Most Launches Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.legend()
plt.show()

# Assuming 'cost' is a column with mission costs
data['cost'] = data['cost'].apply(pd.to_numeric, errors='coerce')  # Convert cost to numeric (if it's not)
cost_by_year = data.groupby('year')['cost'].mean().dropna()

# Plot the cost over time
plt.figure(figsize=(10,6))
cost_by_year.plot(kind='line')
plt.title('Average Mission Cost Over Time')
plt.xlabel('Year')
plt.ylabel('Average Mission Cost (in million USD)')
plt.show()

# Extract month from the 'launch_date' column
data['month'] = pd.to_datetime(data['launch_date']).dt.month

# Count launches by month
launches_by_month = data.groupby('month').size()

# Plot the results
plt.figure(figsize=(10,6))
launches_by_month.plot(kind='bar')
plt.title('Number of Launches per Month')
plt.xlabel('Month')
plt.ylabel('Number of Launches')
plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.show()

# Assuming 'status' column has values like 'Success' or 'Failure'
data['status'] = data['status'].str.strip().apply(lambda x: 'Success' if x == 'Success' else 'Failure')

# Calculate the success rate by year
success_rate = data.groupby('year')['status'].value_counts(normalize=True).unstack().fillna(0)
success_rate['success_rate'] = success_rate['Success']

# Plot the success rate over time
plt.figure(figsize=(10,6))
success_rate['success_rate'].plot(kind='line', color='green')
plt.title('Space Mission Success Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Success Rate')
plt.show()

