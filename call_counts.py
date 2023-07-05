import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('6mo_unique_callers.csv') 

# Pivot the data to get the total number of calls per customer
pivot_df = df.pivot_table(index='caller_id', values='num_calls', aggfunc='sum')

# Order the pivot table by number of calls in descending order
caller_counts = pivot_df.sort_values(by='num_calls', ascending=False)

print(caller_counts.head())

# Count the number of callers falling into each category
count_once = (caller_counts['num_calls'] == 1).sum()
count_twice = (caller_counts['num_calls'] == 2).sum()
count_three_times = (caller_counts['num_calls'] == 3).sum()
count_four_times = (caller_counts['num_calls'] == 4).sum()
count_five_times = (caller_counts['num_calls'] == 5).sum()
count_six_to_ten_times = ((caller_counts['num_calls'] >= 6) & (caller_counts['num_calls'] <= 10)).sum()
count_eleven_to_twenty_times = ((caller_counts['num_calls'] >= 11) & (caller_counts['num_calls'] <= 20)).sum()
count_more_than_twenty_times = (caller_counts['num_calls'] > 20).sum()

# Calculate the percentages
total_callers = caller_counts.index.nunique()
percentage_once = (count_once / total_callers) * 100
percentage_twice = (count_twice / total_callers) * 100
percentage_three_times = (count_three_times / total_callers) * 100
percentage_four_times = (count_four_times / total_callers) * 100
percentage_five_times = (count_five_times / total_callers) * 100
percentage_six_to_ten_times = (count_six_to_ten_times / total_callers) * 100
percentage_eleven_to_twenty_times = (count_eleven_to_twenty_times / total_callers) * 100
percentage_more_than_twenty_times = (count_more_than_twenty_times / total_callers) * 100

# Create a bar plot
categories = ["1", "2", "3", "4", "5", "6-10", "11-20", "21+"]
percentages = [percentage_once, percentage_twice, percentage_three_times, percentage_four_times, percentage_five_times,
               percentage_six_to_ten_times, percentage_eleven_to_twenty_times, percentage_more_than_twenty_times]

plt.bar(categories, percentages)
plt.xlabel('Number of Calls')
plt.ylabel('Percentage of Callers')
plt.title('Distribution of Callers by Number of Calls')
plt.xticks(categories)  # Set x-tick labels as categories

# Add labels to the bars
for i, percentage in enumerate(percentages):
    plt.text(categories[i], percentage, f"{percentage:.2f}%", ha='center', va='bottom')

# Save the label text as a TSV file
label_df = pd.DataFrame({'Number of Calls': categories, 'Percentage of Callers': percentages})
label_df.to_csv('labels_pct.csv',index=False)

# Save the count numbers as a TSV file
count_df = pd.DataFrame({'Number of Calls': categories, 'Count of Callers': [count_once, count_twice, count_three_times,
                                                                              count_four_times, count_five_times,
                                                                              count_six_to_ten_times,
                                                                              count_eleven_to_twenty_times,
                                                                              count_more_than_twenty_times]})
count_df.to_csv('labels_numbers.csv', index=False)

# Save the plot as a PNG('calls_pct_dist_v2.png')

# Show plot
plt.show()
