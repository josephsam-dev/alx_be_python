# Prompt for a single task and its details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using if/elif/else for backward compatibility
if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task. Make sure to complete it soon.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a medium priority task. Plan your time for it accordingly.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    # This handles any invalid priority input
    print("Invalid priority entered. Please choose from high, medium, or low.")
