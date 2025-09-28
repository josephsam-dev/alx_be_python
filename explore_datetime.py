from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time and returns it as a string."""
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    # FIX: Return the formatted string as required by the checker.
    return formatted_datetime


def calculate_future_date(days_to_add):
    """Calculates a future date by adding days to the current date."""
    # FIX: Get a fresh current_date here instead of passing it in.
    current_date = datetime.now()
    delta = timedelta(days=days_to_add)
    future_date = current_date + delta
    return future_date


def main():
    """Main function to run the date and time operations."""
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        # Prompt the user for the number of days
        prompt_text = "Enter the number of days to add to the current date: "
        num_days_str = input(prompt_text)
        num_days = int(num_days_str)

        # Calculate and display the future date
        # FIX: Pass only the number of days to the updated function.
        future_result_date = calculate_future_date(num_days)
        formatted_future_date = future_result_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
