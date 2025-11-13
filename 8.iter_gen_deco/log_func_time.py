import time

def log_execution_time(func):
    """Decorator to log how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.strftime("%H:%M:%S")
        print(start)
        result = func(*args, **kwargs)
        end = time.strftime("%H:%M:%S")
        print(end)
        return result
    return wrapper


# Apply decorator
@log_execution_time
def process_data():
    print("Processing data...")
    time.sleep(2)  # simulate a long-running task
    print("Done!")


# Example usage
process_data()
