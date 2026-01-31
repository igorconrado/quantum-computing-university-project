"""
TSP Nearest Neighbor Heuristic - O(n²)

A greedy algorithm that always visits the closest unvisited city.
Fast but often produces suboptimal solutions.
"""

import math
import time
import json
from typing import List, Tuple


def calculate_distance(city1: tuple, city2: tuple) -> float:
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)


def nearest_neighbor(coordinates: List[tuple], start: int = 0) -> Tuple[list, float, float]:
    """
    Solve TSP using Nearest Neighbor heuristic.

    Always moves to the closest unvisited city.

    Args:
        coordinates: list of (x, y) for each city
        start: starting city index

    Returns:
        tuple: (route, total_distance, execution_time)
    """
    n = len(coordinates)
    print(f"Solving TSP with {n} cities using Nearest Neighbor...")

    start_time = time.time()

    visited = [False] * n
    route = [start]
    visited[start] = True
    total_distance = 0.0

    current = start
    for _ in range(n - 1):
        nearest = None
        nearest_dist = float('inf')

        # Find closest unvisited city
        for j in range(n):
            if not visited[j]:
                dist = calculate_distance(coordinates[current], coordinates[j])
                if dist < nearest_dist:
                    nearest_dist = dist
                    nearest = j

        # Move to nearest city
        route.append(nearest)
        visited[nearest] = True
        total_distance += nearest_dist
        current = nearest

    # Return to start
    total_distance += calculate_distance(coordinates[current], coordinates[start])

    execution_time = time.time() - start_time

    return route, total_distance, execution_time


def nearest_neighbor_all_starts(coordinates: List[tuple]) -> Tuple[list, float, float]:
    """
    Run Nearest Neighbor from all possible starting cities.

    Returns the best result found.

    Args:
        coordinates: list of (x, y) for each city

    Returns:
        tuple: (best_route, best_distance, execution_time)
    """
    n = len(coordinates)
    print(f"Solving TSP with {n} cities using Nearest Neighbor (all starts)...")

    start_time = time.time()

    best_route = None
    best_distance = float('inf')

    for start in range(n):
        route, distance, _ = nearest_neighbor(coordinates, start)
        if distance < best_distance:
            best_distance = distance
            best_route = route

    execution_time = time.time() - start_time

    return best_route, best_distance, execution_time


def load_cities(filename: str, dataset: str) -> tuple:
    """Load cities from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    cities = data[dataset]['cities']
    coords = [tuple(c) for c in data[dataset]['coordinates']]
    return cities, coords


def print_results(cities: list, route: list, distance: float, time_sec: float):
    """Pretty print the results."""
    print("\n" + "=" * 50)
    print("RESULTS (Nearest Neighbor)")
    print("=" * 50)
    print(f"Best route: {' -> '.join(cities[i] for i in route)} -> {cities[route[0]]}")
    print(f"Total distance: {distance:.2f}")
    print(f"Execution time: {time_sec:.6f} seconds")
    print("=" * 50)


if __name__ == "__main__":
    import os

    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cities.json')

    # NN is very fast, can handle any size
    datasets = ["small_5", "small_6", "medium_8", "medium_10", "large_15"]

    for dataset in datasets:
        print(f"\n{'#' * 60}")
        print(f"Dataset: {dataset}")
        print('#' * 60)

        cities, coords = load_cities(data_path, dataset)

        # Single start
        route, distance, exec_time = nearest_neighbor(coords)
        print_results(cities, route, distance, exec_time)

        # All starts (better quality)
        route_all, distance_all, exec_time_all = nearest_neighbor_all_starts(coords)
        print(f"\nAll-starts improvement: {distance:.2f} -> {distance_all:.2f}")
