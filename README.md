# DeliveryOptimiser

Delivery route optimiser for a food delivery scenario

## Directory Structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    ├── main.py              # Primary entry point
    ├── test_cases.txt       # Input test cases
    ├── distanceCalc/
    │   ├── __init__.py
    │   └── distance_calculator.py
    └── routeFinder/
        ├── __init__.py
        ├── route_finder.py
        └── route_optimiser.py
```

## Code Flow

1. **Initialization:** The application (`src/main.py`) reads the test cases from `src/test_cases.txt`, where each test case includes the delivery executive's coordinates of current location, list of restaurants and list of consumers. In the list of restaurants, each item of the list contains name of the restaurant, it's location coordinates and preparation time. In list of consumers, each item of the list contains name of the consumer, it's location coordinates.
2. **Route Generation:** The `RouteFinder` generates all valid order permutations using a backtracking algorithm. The validity is ensured by checking the consumer node is not visited before visiting it's corresponding restaurant node. A sequence is only valid if a meal is picked up from a restaurant before being delivered to its respective consumer.
3. **Distance Calculation:** For each valid sequence, travel times are calculated utilizing the `DistanceCalculator`, which applies the Haversine formula to find the great-circle distance between geospatial coordinates.
4. **Wait Time Handling:** The route time simulation properly accounts for restaurant preparation times. If the delivery executive arrives at a restaurant before the meal is ready, the wait time is added to the total calculation.
5. **Optimization:** The route resulting in the minimum total time from start to final drop-off is selected and output to the terminal.

## Execution

Clone the repository and navigate to the project folder.

To automatically set up the environment, install Python (if necessary), and run the application, execute the provided setup script:

```bash
chmod +x setup_and_run.sh
./setup_and_run.sh
```
