"""
TSP Simulated Annealing Solution

A metaheuristic that can escape local minima by accepting
worse solutions with decreasing probability.

This is what classical computers use in practice.
"""

import random
import math
import time
import json


def calculate_distance(city1: tuple, city2: tuple) -> float:
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)


def calculate_total_distance(route: list, coordinates: list) -> float:
    """Calculate total distance of a route."""
    total = 0
    for i in range(len(route)):
        total += calculate_distance(
            coordinates[route[i]],
            coordinates[route[(i + 1) % len(route)]]
        )
    return total


def generate_neighbor(route: list) -> list:
    """
    Generate a neighboring solution by swapping two cities.

    Args:
        route: current route

    Returns:
        list: new route with two cities swapped
    """
    new_route = route.copy()
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


def acceptance_probability(current_distance: float, new_distance: float, temperature: float) -> float:
    """
    Calculate probability of accepting a worse solution.

    Args:
        current_distance: distance of current solution
        new_distance: distance of candidate solution
        temperature: current temperature

    Returns:
        float: probability of accepting new solution
    """
    if new_distance < current_distance:
        return 1.0
    return math.exp(-(new_distance - current_distance) / temperature)


def simulated_annealing(
    coordinates: list,
    initial_temp: float = 10000,
    cooling_rate: float = 0.9995,
    min_temp: float = 1
) -> tuple:
    """
    Solve TSP using Simulated Annealing.

    Args:
        coordinates: list of (x, y) for each city
        initial_temp: starting temperature
        cooling_rate: how fast to cool (0.99 = slow, 0.9999 = very slow)
        min_temp: stop when temperature reaches this

    Returns:
        tuple: (best_route, best_distance, execution_time, iterations)
    """
    n = len(coordinates)
    print(f"Solving TSP with {n} cities using Simulated Annealing...")

    start_time = time.time()

    # Start with random route
    current_route = list(range(n))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, coordinates)

    best_route = current_route.copy()
    best_distance = current_distance
    iterations = 0

    temperature = initial_temp

    while temperature > min_temp:
        # Generate neighbor solution
        new_route = generate_neighbor(current_route)
        new_distance = calculate_total_distance(new_route, coordinates)

        # Accept or reject based on probability
        if random.random() < acceptance_probability(current_distance, new_distance, temperature):
            current_route = new_route
            current_distance = new_distance

            # Update best if improved
            if current_distance < best_distance:
                best_distance = current_distance
                best_route = current_route.copy()

        # Cool down
        temperature *= cooling_rate
        iterations += 1

        # Progress indicator
        if iterations % 50000 == 0:
            print(f"  Iteration {iterations:,}, temp={temperature:.2f}, best={best_distance:.2f}")

    execution_time = time.time() - start_time

    return best_route, best_distance, execution_time, iterations


def load_cities(filename: str, dataset: str) -> tuple:
    """Load cities from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    cities = data[dataset]['cities']
    coords = [tuple(c) for c in data[dataset]['coordinates']]
    return cities, coords


def print_results(cities: list, route: list, distance: float, time_sec: float, iters: int):
    """Pretty print the results."""
    print("\n" + "=" * 50)
    print("RESULTS (Simulated Annealing)")
    print("=" * 50)
    print(f"Best route: {' -> '.join(cities[i] for i in route)} -> {cities[route[0]]}")
    print(f"Total distance: {distance:.2f}")
    print(f"Execution time: {time_sec:.4f} seconds")
    print(f"Iterations: {iters:,}")
    print("=" * 50)


if __name__ == "__main__":
    import os

    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cities.json')

    # SA can handle larger instances!
    datasets = ["small_5", "small_6", "medium_8", "medium_10", "large_15"]

    for dataset in datasets:
        print(f"\n{'#' * 60}")
        print(f"Dataset: {dataset}")
        print('#' * 60)

        cities, coords = load_cities(data_path, dataset)
        route, distance, exec_time, iters = simulated_annealing(coords)

        print_results(cities, route, distance, exec_time, iters)
