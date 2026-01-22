"""
TSP Brute Force Solution - O(n!)

This is intentionally inefficient to demonstrate the classical limitation.
Watch the execution time explode as you add more cities!

TODO: Implement the algorithm.
"""

from itertools import permutations
import time
import json
import math


def calculate_distance(city1: tuple, city2: tuple) -> float:
    """
    Calculate Euclidean distance between two cities.

    Args:
        city1: (x, y) coordinates
        city2: (x, y) coordinates

    Returns:
        float: distance between cities
    """
    # TODO: Implement Euclidean distance formula
    # sqrt((x2-x1)^2 + (y2-y1)^2)
    pass


def calculate_total_distance(route: list, coordinates: list) -> float:
    """
    Calculate total distance of a route.

    Args:
        route: list of city indices in order
        coordinates: list of (x, y) for each city

    Returns:
        float: total distance of the route
    """
    # TODO: Sum distances between consecutive cities
    # Don't forget to return to starting city!
    pass


def tsp_brute_force(coordinates: list) -> tuple:
    """
    Solve TSP using brute force (try all permutations).

    Args:
        coordinates: list of (x, y) for each city

    Returns:
        tuple: (best_route, best_distance, execution_time, permutations_checked)
    """
    n = len(coordinates)
    print(f"Solving TSP with {n} cities...")
    print(f"Total permutations to check: {math.factorial(n-1):,}")

    start_time = time.time()

    # TODO: Implement brute force algorithm
    # 1. Fix first city (optimization: reduces n! to (n-1)!)
    # 2. Try all permutations of remaining cities
    # 3. Calculate total distance for each
    # 4. Keep track of minimum

    best_route = None
    best_distance = float('inf')
    permutations_checked = 0

    # Your code here...

    execution_time = time.time() - start_time

    return best_route, best_distance, execution_time, permutations_checked


def load_cities(filename: str, dataset: str) -> tuple:
    """
    Load cities from JSON file.

    Args:
        filename: path to cities.json
        dataset: which dataset to load (e.g., "small_5")

    Returns:
        tuple: (city_names, coordinates)
    """
    with open(filename, 'r') as f:
        data = json.load(f)

    cities = data[dataset]['cities']
    coords = [tuple(c) for c in data[dataset]['coordinates']]
    return cities, coords


def print_results(cities: list, route: list, distance: float, time_sec: float, perms: int):
    """Pretty print the results."""
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Best route: {' -> '.join(cities[i] for i in route)} -> {cities[route[0]]}")
    print(f"Total distance: {distance:.2f}")
    print(f"Execution time: {time_sec:.4f} seconds")
    print(f"Permutations checked: {perms:,}")
    print("=" * 50)


if __name__ == "__main__":
    import os

    # Find cities.json
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cities.json')

    # Test with different sizes
    datasets = ["small_5", "small_6", "medium_8"]

    for dataset in datasets:
        print(f"\n{'#' * 60}")
        print(f"Dataset: {dataset}")
        print('#' * 60)

        cities, coords = load_cities(data_path, dataset)
        route, distance, exec_time, perms = tsp_brute_force(coords)

        if route:
            print_results(cities, route, distance, exec_time, perms)
        else:
            print("TODO: Implement the algorithm!")

        print()

    # Try medium_10 if you dare! (warning: will take a long time)
    # cities, coords = load_cities(data_path, "medium_10")
    # route, distance, exec_time, perms = tsp_brute_force(coords)
