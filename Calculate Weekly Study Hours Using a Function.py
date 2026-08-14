def display_study_hours():
    # Read the inputs, calculate the total and print it
    hours_per_day = int(input())
    study_days = int(input())
    
    total_hours = hours_per_day * study_days
    print(f"Total Study Hours: {total_hours}")

# Call the function
display_study_hours()

