"""
TSP QUBO Solver - Quantum-Inspired Optimization

Formulates TSP as a QUBO (Quadratic Unconstrained Binary Optimization) problem.
This approach is used by quantum annealers (D-Wave) and quantum-inspired algorithms.

Key insight: Convert TSP constraints into penalty terms in a quadratic function.
"""

import numpy as np
import time
import json
import math
from typing import Tuple, List, Optional


def calculate_distance_matrix(coordinates: List[tuple]) -> np.ndarray:
    """
    Create distance matrix from coordinates.

    Args:
        coordinates: list of (x, y) tuples

    Returns:
        np.ndarray: symmetric distance matrix
    """
    n = len(coordinates)
    dist_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                dx = coordinates[j][0] - coordinates[i][0]
                dy = coordinates[j][1] - coordinates[i][1]
                dist_matrix[i][j] = math.sqrt(dx**2 + dy**2)

    return dist_matrix


def create_qubo_matrix(distance_matrix: np.ndarray, penalty: float = 1000) -> np.ndarray:
    """
    Create QUBO matrix for TSP.

    The TSP QUBO uses binary variables x_{i,p} = 1 if city i is visited at position p.

    Objective: minimize sum of distances
    Constraints (encoded as penalties):
    1. Each city visited exactly once
    2. Each position has exactly one city

    Args:
        distance_matrix: n x n distance matrix
        penalty: penalty weight for constraint violations

    Returns:
        np.ndarray: QUBO matrix Q where energy E = x^T Q x
    """
    n = len(distance_matrix)
    num_vars = n * n  # x_{i,p} for i in cities, p in positions

    Q = np.zeros((num_vars, num_vars))

    def idx(city: int, pos: int) -> int:
        """Convert (city, position) to QUBO variable index."""
        return city * n + pos

    # Objective: Add distance costs
    # If city i at position p and city j at position p+1, add distance[i][j]
    for p in range(n):
        next_p = (p + 1) % n
        for i in range(n):
            for j in range(n):
                if i != j:
                    Q[idx(i, p)][idx(j, next_p)] += distance_matrix[i][j]

    # Constraint 1: Each city visited exactly once
    # sum_p(x_{i,p}) = 1 for all cities i
    # Penalty: A * (sum_p(x_{i,p}) - 1)^2
    for i in range(n):
        for p in range(n):
            Q[idx(i, p)][idx(i, p)] -= penalty  # Linear term
            for p2 in range(p + 1, n):
                Q[idx(i, p)][idx(i, p2)] += 2 * penalty  # Quadratic term

    # Constraint 2: Each position has exactly one city
    # sum_i(x_{i,p}) = 1 for all positions p
    for p in range(n):
        for i in range(n):
            Q[idx(i, p)][idx(i, p)] -= penalty  # Linear term
            for i2 in range(i + 1, n):
                Q[idx(i, p)][idx(i2, p)] += 2 * penalty  # Quadratic term

    # Add constant offset for constraint satisfaction (n cities + n positions)
    # This is for energy normalization but doesn't affect optimization

    return Q


def evaluate_qubo(Q: np.ndarray, x: np.ndarray) -> float:
    """Evaluate QUBO energy for solution x."""
    return float(x.T @ Q @ x)


def decode_solution(x: np.ndarray, n: int) -> Optional[List[int]]:
    """
    Decode QUBO solution to TSP route.

    Args:
        x: binary solution vector
        n: number of cities

    Returns:
        List[int]: route as list of city indices, or None if invalid
    """
    route = []
    for p in range(n):
        city_at_pos = -1
        for i in range(n):
            if x[i * n + p] > 0.5:
                if city_at_pos >= 0:
                    return None  # Multiple cities at same position
                city_at_pos = i
        if city_at_pos < 0:
            return None  # No city at this position
        route.append(city_at_pos)

    # Verify all cities visited
    if set(route) != set(range(n)):
        return None

    return route


def quantum_inspired_solver(
    Q: np.ndarray,
    n_cities: int,
    n_iterations: int = 10000,
    n_reads: int = 100
) -> Tuple[np.ndarray, float]:
    """
    Quantum-inspired solver using simulated quantum tunneling.

    This simulates the behavior of quantum annealers by:
    1. Starting from random superposition-like states
    2. Using probabilistic updates that can escape local minima
    3. Gradually reducing "quantum fluctuations"

    Args:
        Q: QUBO matrix
        n_cities: number of cities
        n_iterations: iterations per read
        n_reads: number of independent runs

    Returns:
        Tuple[np.ndarray, float]: best solution and its energy
    """
    num_vars = n_cities * n_cities
    best_x = None
    best_energy = float('inf')

    for read in range(n_reads):
        # Initialize with random valid solution (one-hot per row and column)
        x = np.zeros(num_vars)
        perm = np.random.permutation(n_cities)
        for p, city in enumerate(perm):
            x[city * n_cities + p] = 1

        current_energy = evaluate_qubo(Q, x)

        # Simulated quantum annealing
        for it in range(n_iterations):
            # "Transverse field" strength (quantum fluctuations)
            gamma = 1.0 - (it / n_iterations)
            temp = max(0.01, gamma * 10)

            # Try flipping pairs of variables (swap cities between positions)
            i1 = np.random.randint(n_cities)
            i2 = np.random.randint(n_cities)
            if i1 == i2:
                continue

            # Find current positions
            p1 = np.argmax(x[i1 * n_cities:(i1 + 1) * n_cities])
            p2 = np.argmax(x[i2 * n_cities:(i2 + 1) * n_cities])

            # Create candidate with swapped positions
            x_new = x.copy()
            x_new[i1 * n_cities + p1] = 0
            x_new[i1 * n_cities + p2] = 1
            x_new[i2 * n_cities + p2] = 0
            x_new[i2 * n_cities + p1] = 1

            new_energy = evaluate_qubo(Q, x_new)

            # Accept with Boltzmann probability (simulating quantum tunneling)
            delta = new_energy - current_energy
            if delta < 0 or np.random.random() < np.exp(-delta / temp):
                x = x_new
                current_energy = new_energy

        if current_energy < best_energy:
            best_energy = current_energy
            best_x = x.copy()

    return best_x, best_energy


def calculate_total_distance(route: List[int], coordinates: List[tuple]) -> float:
    """Calculate total distance of a route."""
    total = 0.0
    for i in range(len(route)):
        c1 = coordinates[route[i]]
        c2 = coordinates[route[(i + 1) % len(route)]]
        total += math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)
    return total


def tsp_qubo(coordinates: List[tuple], n_iterations: int = 5000, n_reads: int = 50) -> tuple:
    """
    Solve TSP using QUBO formulation with quantum-inspired solver.

    Args:
        coordinates: list of (x, y) for each city
        n_iterations: iterations per read
        n_reads: number of independent runs

    Returns:
        tuple: (best_route, best_distance, execution_time, qubo_energy)
    """
    n = len(coordinates)
    print(f"Solving TSP with {n} cities using QUBO...")
    print(f"QUBO variables: {n*n}")

    start_time = time.time()

    # Create distance matrix and QUBO
    dist_matrix = calculate_distance_matrix(coordinates)
    Q = create_qubo_matrix(dist_matrix)

    # Solve using quantum-inspired algorithm
    best_x, best_energy = quantum_inspired_solver(Q, n, n_iterations, n_reads)

    # Decode solution
    route = decode_solution(best_x, n)

    if route:
        distance = calculate_total_distance(route, coordinates)
    else:
        distance = float('inf')
        route = list(range(n))  # Fallback to sequential

    execution_time = time.time() - start_time

    return route, distance, execution_time, best_energy


def load_cities(filename: str, dataset: str) -> tuple:
    """Load cities from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    cities = data[dataset]['cities']
    coords = [tuple(c) for c in data[dataset]['coordinates']]
    return cities, coords


def print_results(cities: list, route: list, distance: float, time_sec: float, energy: float):
    """Pretty print the results."""
    print("\n" + "=" * 50)
    print("RESULTS (QUBO Quantum-Inspired)")
    print("=" * 50)
    print(f"Best route: {' -> '.join(cities[i] for i in route)} -> {cities[route[0]]}")
    print(f"Total distance: {distance:.2f}")
    print(f"Execution time: {time_sec:.4f} seconds")
    print(f"QUBO energy: {energy:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    import os

    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cities.json')

    # QUBO can handle moderate instances
    datasets = ["small_5", "small_6", "medium_8", "medium_10"]

    for dataset in datasets:
        print(f"\n{'#' * 60}")
        print(f"Dataset: {dataset}")
        print('#' * 60)

        cities, coords = load_cities(data_path, dataset)
        route, distance, exec_time, energy = tsp_qubo(coords)

        print_results(cities, route, distance, exec_time, energy)
