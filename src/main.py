import ast
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.routeFinder import RouteFinder

def main():
    # 1. Load Test Cases from file
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'test_cases.txt')
        with open(file_path, 'r') as f:
            test_cases = ast.literal_eval(f.read())
    except FileNotFoundError:
        print("Error: 'test_cases.txt' not found. Please ensure the file exists.")
        return
    except (ValueError, SyntaxError):
        print("Error: Could not parse 'test_cases.txt'. Please ensure it's a valid Python list of dictionaries.")
        return

    # 2. Initialize the Route Finder
    print("Initializing Route Finder (Driver Speed: 20 km/h)...")
    optimizer = RouteFinder(speed_kmh=20.0)

    # 3. Iterate over test cases and execute
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n--- Running Test Case {i} ---")
        
        del_exec_loc = test_case['del_exec_loc']
        restaurants = test_case['restaurants']
        consumers = test_case['consumers']

        print(f"Calculating best route for {len(restaurants)} order(s)...")
        best_time, best_path = optimizer.find_best_route(del_exec_loc, restaurants, consumers)

        # 4. Display Results for the current test case
        print(f"  Total Time (in hours): {best_time:.3f} hrs")
        
        all_locations = restaurants + consumers
        route_names = [all_locations[idx]["name"] for idx in best_path]
        print(f"  Route Execution Plan: {' -> '.join(route_names)}")

if __name__ == "__main__":
    main()