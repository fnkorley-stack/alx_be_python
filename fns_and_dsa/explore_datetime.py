from datetime import datetime, timedelta


def display_current_datetime() -> datetime:
    """Return the current datetime and print it formatted as YYYY-MM-DD HH:MM:SS."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date


def calculate_future_date(current_date: datetime, days_to_add: int) -> datetime:
    """Calculate and return the future date after adding `days_to_add` days."""
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date


if __name__ == "__main__":
    current_date = display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Please enter a valid integer for days.")
