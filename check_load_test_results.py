import time
import os

def check_load_test_results(max_attempts=10, delay=5):
    for attempt in range(max_attempts):
        if os.path.exists('load_test_output.txt'):
            with open('load_test_output.txt', 'r') as f:
                content = f.read()
                if content:
                    print(content)
                    return
        print(f"Attempt {attempt + 1}: Results not available yet. Retrying in {delay} seconds...")
        time.sleep(delay)
    print("Load test results not available after maximum attempts.")

if __name__ == "__main__":
    check_load_test_results()
