import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

plt.style.use('ggplot')

# Define your tasks data with week numbers and durations
tasks = [
    # Initial Planning and Design Phase
    {'task': 'User Flows and Feature Definitions', 'week': 1, 'duration': 4},
    {'task': 'UI/UX Design', 'week': 5, 'duration': 3},
    {'task': 'Architecture Planning', 'week': 9, 'duration': 2},
    {'task': 'API Endpoint Definition', 'week': 11, 'duration': 1},
    
    # Development Phase
    {'task': 'Backend Development', 'week': 12, 'duration': 10},
    {'task': 'Frontend Development', 'week': 22, 'duration': 10},
    {'task': 'Testing and QA', 'week': 32, 'duration': 5},
    
    # Deployment and DevOps
    {'task': 'CI/CD Setup', 'week': 37, 'duration': 1},
    {'task': 'Containerization', 'week': 38, 'duration': 1},
    {'task': 'Deployment', 'week': 39, 'duration': 1},
    
    # Additional Features
    {'task': 'Search Functionality', 'week': 16, 'duration': 3},
    {'task': 'Responsive Design', 'week': 21, 'duration': 3},
    
    # Non-functional Requirements
    {'task': 'Performance Testing', 'week': 27, 'duration': 2},
    {'task': 'Security Implementation', 'week': 29, 'duration': 2},
]

# Convert week numbers to actual start dates 
project_start_date = '2024-07-01'  # Adjust this based on your project's actual start date

for task in tasks:
    start_date = np.datetime64(project_start_date) + np.timedelta64((task['week'] - 1) * 7, 'D')
    task['start_date'] = start_date

# Create figure and axes
fig, ax = plt.subplots(figsize=(40, 8))

# Plot each task as a horizontal bar
for i, task in enumerate(tasks):
    ax.barh(task['task'], left=task['start_date'], width=task['duration']*7, height=0.5, align='center', alpha=0.8)

# Format x-axis with major and minor ticks
ax.set_xlabel('Timeline (Weeks)')
weeks = np.arange(1, 53)
week_dates = [np.datetime64(project_start_date) + np.timedelta64((week - 1) * 7, 'D') for week in weeks]

# Set major ticks every 4 weeks
major_locator = MultipleLocator(base=4*7)  # 4 weeks in days
ax.xaxis.set_major_locator(major_locator)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Set minor ticks every week
minor_locator = AutoMinorLocator(n=4)  # 4 minor ticks between each major tick
ax.xaxis.set_minor_locator(minor_locator)

# Add grid in the background
ax.grid(visible=True, which='both', linestyle='--', linewidth=0.5, color='gray')

# Set x-axis labels to "Week X"
months = np.arange(1, 14)  # Adjust range as needed
ax.set_xticks(week_dates[::4])  # Set ticks at every 4 weeks
ax.set_xticklabels([f'Month {month}' for month in range(1, len(week_dates[::4]) + 1)])

ax.set_xlim(np.datetime64(project_start_date), np.datetime64(project_start_date) + np.timedelta64(52 * 7, 'D'))

# Format y-axis
ax.set_yticks(np.arange(len(tasks)))
ax.set_yticklabels([task['task'] for task in tasks])
ax.set_ylabel('Tasks')


# Title and save plot
plt.title('Gantt Chart Example')
plt.tight_layout()
plt.savefig('/code/src/gantt_chart.png')  # Save the plot to a file