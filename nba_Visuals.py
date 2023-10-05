import pandas as pd
import matplotlib.pyplot as plt

# A graph like this can be generated easily in Excel/sheets, but for the purpose of this project I utilized Python
# Assuming your data is in a CSV file named "NBA_data - COMPILED.csv"
data = pd.read_csv("/Users/jonco11ins/Documents/NBA_data/NBA_data - COMPILED.csv")

df = pd.DataFrame(data)

# Setting the positions and width for the bars
pos = list(range(len(df['3PA'])))
width = 0.4

# Plotting the bars
fig, ax = plt.subplots(figsize=(15, 7))

# Create a bar with FGA data
plt.bar(pos, df['3PA'], width, alpha=0.8, color='#EE3224', label=df['SEASON'][0])

# Create a bar with 3P% data
plt.bar([p + width for p in pos], df['3P%'], width, alpha=0.8, color='#F78F1E', label=df['SEASON'][1])

# Set the y axis label
ax.set_ylabel('Value')

# Set the chart's title
ax.set_title('3-pointers Attempted and Percentage Made by Season')

# Set the position of the x ticks
ax.set_xticks([p + 0.5 * width for p in pos])

# Set the labels for the x ticks and rotate them
ax.set_xticklabels(df['SEASON'], rotation=45, ha="right")  # Added rotation and alignment

# Setting the x-axis and y-axis limits
plt.xlim(min(pos) - width, max(pos) + width * 2)
plt.ylim([0, 45])  # Set y-axis max value to 60

# Adding the legend and showing the plot
plt.legend(['Average of 3-pointers attempted', 'Average 3-pointers made'], loc='upper left')
plt.grid()
plt.tight_layout()  # To ensure labels and titles fit well
plt.show()


