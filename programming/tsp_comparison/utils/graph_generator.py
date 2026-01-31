"""
Graph Generator for TSP Testing

Generates random city coordinates for benchmarking TSP algorithms.
"""

import random
import json
import math
from typing import List, Tuple, Dict


def generate_random_cities(
    n: int,
    x_range: Tuple[float, float] = (0, 100),
    y_range: Tuple[float, float] = (0, 100),
    seed: int = None
) -> List[Tuple[float, float]]:
    """
    Generate random city coordinates.

    Args:
        n: number of cities
        x_range: (min_x, max_x) range for x coordinates
        y_range: (min_y, max_y) range for y coordinates
        seed: random seed for reproducibility

    Returns:
        List of (x, y) coordinate tuples
    """
    if seed is not None:
        random.seed(seed)

    cities = []
    for _ in range(n):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        cities.append((round(x, 2), round(y, 2)))

    return cities


def generate_clustered_cities(
    n: int,
    n_clusters: int = 3,
    cluster_radius: float = 10,
    x_range: Tuple[float, float] = (0, 100),
    y_range: Tuple[float, float] = (0, 100),
    seed: int = None
) -> List[Tuple[float, float]]:
    """
    Generate cities in clusters (more realistic for logistics).

    Args:
        n: total number of cities
        n_clusters: number of cluster centers
        cluster_radius: radius around each cluster center
        x_range: (min_x, max_x) range
        y_range: (min_y, max_y) range
        seed: random seed

    Returns:
        List of (x, y) coordinate tuples
    """
    if seed is not None:
        random.seed(seed)

    # Generate cluster centers
    centers = []
    for _ in range(n_clusters):
        cx = random.uniform(x_range[0] + cluster_radius, x_range[1] - cluster_radius)
        cy = random.uniform(y_range[0] + cluster_radius, y_range[1] - cluster_radius)
        centers.append((cx, cy))

    # Distribute cities among clusters
    cities = []
    for i in range(n):
        center = centers[i % n_clusters]
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, cluster_radius)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        cities.append((round(x, 2), round(y, 2)))

    return cities


def generate_grid_cities(
    rows: int,
    cols: int,
    spacing: float = 10,
    noise: float = 0
) -> List[Tuple[float, float]]:
    """
    Generate cities on a grid pattern.

    Args:
        rows: number of rows
        cols: number of columns
        spacing: distance between grid points
        noise: random offset to add (0 = perfect grid)

    Returns:
        List of (x, y) coordinate tuples
    """
    cities = []
    for r in range(rows):
        for c in range(cols):
            x = c * spacing + random.uniform(-noise, noise)
            y = r * spacing + random.uniform(-noise, noise)
            cities.append((round(x, 2), round(y, 2)))

    return cities


def calculate_distance_matrix(cities: List[Tuple[float, float]]) -> List[List[float]]:
    """
    Calculate full distance matrix for a set of cities.

    Args:
        cities: list of (x, y) coordinates

    Returns:
        n x n distance matrix
    """
    n = len(cities)
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            dx = cities[j][0] - cities[i][0]
            dy = cities[j][1] - cities[i][1]
            dist = math.sqrt(dx**2 + dy**2)
            matrix[i][j] = round(dist, 4)
            matrix[j][i] = round(dist, 4)

    return matrix


def save_cities_json(
    cities: List[Tuple[float, float]],
    filename: str,
    dataset_name: str,
    description: str = ""
) -> None:
    """
    Save cities to JSON file in standard format.

    Args:
        cities: list of (x, y) coordinates
        filename: output JSON file path
        dataset_name: name for this dataset
        description: optional description
    """
    # Load existing data or create new
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Generate city names (A, B, C, ... AA, AB, ...)
    names = []
    for i in range(len(cities)):
        if i < 26:
            names.append(chr(65 + i))
        else:
            names.append(chr(65 + i // 26 - 1) + chr(65 + i % 26))

    # Add new dataset
    data[dataset_name] = {
        "description": description or f"{len(cities)} cities dataset",
        "cities": names,
        "coordinates": [list(c) for c in cities]
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(cities)} cities to {filename} as '{dataset_name}'")


def generate_benchmark_suite(output_file: str) -> Dict:
    """
    Generate a complete benchmark suite with various sizes and patterns.

    Args:
        output_file: path to output JSON file

    Returns:
        Dictionary with all generated datasets
    """
    datasets = {}

    # Random datasets of increasing size
    for n in [5, 10, 15, 20, 25, 30]:
        name = f"random_{n}"
        cities = generate_random_cities(n, seed=42 + n)
        datasets[name] = cities
        save_cities_json(cities, output_file, name, f"Random {n} cities")

    # Clustered datasets
    for n in [15, 30]:
        name = f"clustered_{n}"
        cities = generate_clustered_cities(n, n_clusters=3, seed=100 + n)
        datasets[name] = cities
        save_cities_json(cities, output_file, name, f"Clustered {n} cities (3 clusters)")

    # Grid dataset
    cities = generate_grid_cities(4, 4, spacing=20, noise=2)
    save_cities_json(cities, output_file, "grid_4x4", "4x4 grid with noise")
    datasets["grid_4x4"] = cities

    return datasets


if __name__ == "__main__":
    import os

    # Generate to data folder
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'generated_cities.json')

    print("Generating benchmark suite...")
    datasets = generate_benchmark_suite(output_path)

    print(f"\nGenerated {len(datasets)} datasets")
    for name, cities in datasets.items():
        print(f"  {name}: {len(cities)} cities")
