from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    # Format the date and time as required
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date


def calculate_future_date(base_date, days_to_add):
    """Calculates a future date by adding days to a base date."""
    delta = timedelta(days=days_to_add)
    future_date = base_date + delta
    return future_date


def main():
    """Main function to run the date and time operations."""
    # Part 1: Display the current date and time
    current_datetime = display_current_datetime()

    # Part 2: Calculate a future date
    try:
        # Prompt the user for the number of days
        prompt_text = "Enter the number of days to add to the current date: "
        num_days_str = input(prompt_text)
        num_days = int(num_days_str)

        # Calculate and display the future date
        future_result_date = calculate_future_date(current_datetime, num_days)
        formatted_future_date = future_result_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
