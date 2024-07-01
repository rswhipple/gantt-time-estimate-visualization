import matplotlib.pyplot as plt
import numpy as np

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

# Convert week numbers to actual start dates based on your project start date and duration
project_start_date = '2024-07-01'  # Adjust this based on your project's actual start date

for task in tasks:
    start_date = np.datetime64(project_start_date) + np.timedelta64((task['week'] - 1) * 7, 'D')
    task['start_date'] = start_date

# Convert start dates to formatted strings if needed
# Example: task['start_date'] = task['start_date'].astype('datetime64[D]').astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each task as a horizontal bar
for i, task in enumerate(tasks):
    ax.barh(task['task'], left=task['start_date'], width=task['duration']*7, height=0.5, align='center', alpha=0.8, label='Task Duration')

# Format x-axis
ax.set_xlabel('Timeline (Weeks)')
ax.set_xlim(np.datetime64(project_start_date), np.datetime64(project_start_date) + np.timedelta64(52 * 7, 'D'))  # Assuming 52 weeks in a year
ax.xaxis.set_major_locator(plt.MaxNLocator(10))  # Adjust as needed

# Format y-axis
ax.set_yticks(np.arange(len(tasks)))
ax.set_yticklabels([task['task'] for task in tasks])
ax.set_ylabel('Tasks')

# Title and display
plt.title('Gantt Chart Example')
plt.tight_layout()
plt.show()
