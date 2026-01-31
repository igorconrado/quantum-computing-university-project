"""
TSP Route Visualizer

Visualize city locations and routes using matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from typing import List, Tuple, Optional
import json
import os


def plot_cities(
    coordinates: List[Tuple[float, float]],
    names: Optional[List[str]] = None,
    ax: Optional[plt.Axes] = None,
    show_labels: bool = True,
    color: str = 'blue',
    size: int = 100
) -> plt.Axes:
    """
    Plot city locations.

    Args:
        coordinates: list of (x, y) tuples
        names: optional city names for labels
        ax: matplotlib axes (creates new if None)
        show_labels: whether to show city name labels
        color: marker color
        size: marker size

    Returns:
        matplotlib Axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))

    x = [c[0] for c in coordinates]
    y = [c[1] for c in coordinates]

    ax.scatter(x, y, c=color, s=size, zorder=5, edgecolors='black', linewidth=1)

    if show_labels and names:
        for i, name in enumerate(names):
            ax.annotate(name, (x[i], y[i]), xytext=(5, 5),
                       textcoords='offset points', fontsize=9, fontweight='bold')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True, alpha=0.3)

    return ax


def plot_route(
    coordinates: List[Tuple[float, float]],
    route: List[int],
    ax: Optional[plt.Axes] = None,
    names: Optional[List[str]] = None,
    title: str = "TSP Route",
    color: str = 'green',
    linewidth: float = 2,
    show_arrows: bool = True
) -> plt.Axes:
    """
    Plot a TSP route.

    Args:
        coordinates: list of (x, y) tuples
        route: list of city indices in visit order
        ax: matplotlib axes
        names: optional city names
        title: plot title
        color: route line color
        linewidth: route line width
        show_arrows: whether to show direction arrows

    Returns:
        matplotlib Axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))

    # Plot cities first
    plot_cities(coordinates, names, ax, show_labels=True)

    # Draw route
    for i in range(len(route)):
        start_idx = route[i]
        end_idx = route[(i + 1) % len(route)]

        x1, y1 = coordinates[start_idx]
        x2, y2 = coordinates[end_idx]

        if show_arrows:
            ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                       arrowprops=dict(arrowstyle='->', color=color, lw=linewidth))
        else:
            ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth, zorder=1)

    # Highlight start city
    start = coordinates[route[0]]
    ax.scatter([start[0]], [start[1]], c='red', s=200, marker='*', zorder=10,
              edgecolors='black', linewidth=1, label='Start')

    ax.set_title(title)
    ax.legend()

    return ax


def compare_routes(
    coordinates: List[Tuple[float, float]],
    routes: dict,
    names: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (15, 5)
) -> plt.Figure:
    """
    Compare multiple routes side by side.

    Args:
        coordinates: list of (x, y) tuples
        routes: dict of {algorithm_name: (route, distance)}
        names: optional city names
        figsize: figure size

    Returns:
        matplotlib Figure object
    """
    n_routes = len(routes)
    fig, axes = plt.subplots(1, n_routes, figsize=figsize)

    if n_routes == 1:
        axes = [axes]

    colors = ['green', 'blue', 'orange', 'purple', 'red']

    for i, (algo_name, (route, distance)) in enumerate(routes.items()):
        ax = axes[i]
        plot_route(coordinates, route, ax, names,
                  title=f"{algo_name}\nDistance: {distance:.2f}",
                  color=colors[i % len(colors)])

    plt.tight_layout()
    return fig


def plot_convergence(
    iterations: List[int],
    distances: List[float],
    algorithm: str = "Algorithm",
    ax: Optional[plt.Axes] = None
) -> plt.Axes:
    """
    Plot algorithm convergence over iterations.

    Args:
        iterations: list of iteration numbers
        distances: corresponding distances
        algorithm: algorithm name for title
        ax: matplotlib axes

    Returns:
        matplotlib Axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(iterations, distances, 'b-', linewidth=1.5)
    ax.fill_between(iterations, distances, alpha=0.3)

    ax.set_xlabel('Iteration')
    ax.set_ylabel('Best Distance')
    ax.set_title(f'{algorithm} - Convergence')
    ax.grid(True, alpha=0.3)

    # Mark final value
    final_dist = distances[-1]
    ax.axhline(y=final_dist, color='r', linestyle='--', alpha=0.7,
              label=f'Final: {final_dist:.2f}')
    ax.legend()

    return ax


def plot_complexity_comparison(
    sizes: List[int],
    times: dict,
    ax: Optional[plt.Axes] = None
) -> plt.Axes:
    """
    Plot time complexity comparison between algorithms.

    Args:
        sizes: list of problem sizes (number of cities)
        times: dict of {algorithm_name: [times]}
        ax: matplotlib axes

    Returns:
        matplotlib Axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    markers = ['o-', 's-', '^-', 'D-', 'v-']
    colors = ['blue', 'green', 'orange', 'red', 'purple']

    for i, (algo, algo_times) in enumerate(times.items()):
        ax.plot(sizes, algo_times, markers[i % len(markers)],
               color=colors[i % len(colors)], label=algo, linewidth=2, markersize=8)

    ax.set_xlabel('Number of Cities')
    ax.set_ylabel('Execution Time (s)')
    ax.set_title('Algorithm Time Complexity Comparison')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)
    ax.legend()

    return ax


def save_figure(fig: plt.Figure, filename: str, dpi: int = 150) -> None:
    """Save figure to file."""
    fig.savefig(filename, dpi=dpi, bbox_inches='tight')
    print(f"Saved figure to {filename}")


if __name__ == "__main__":
    # Demo visualization
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cities.json')

    with open(data_path, 'r') as f:
        data = json.load(f)

    # Load small dataset
    dataset = data['small_5']
    coords = [tuple(c) for c in dataset['coordinates']]
    names = dataset['cities']

    # Example route (just sequential for demo)
    route = list(range(len(coords)))

    # Calculate distance
    total_dist = 0
    for i in range(len(route)):
        c1 = coords[route[i]]
        c2 = coords[route[(i + 1) % len(route)]]
        total_dist += ((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)**0.5

    # Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_route(coords, route, ax, names,
              title=f"Example Route (Distance: {total_dist:.2f})")

    plt.tight_layout()
    plt.show()
