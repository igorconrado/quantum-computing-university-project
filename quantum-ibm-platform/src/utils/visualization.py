"""
Visualization Utilities

Plotting and display functions for quantum experiments.
"""

from typing import List, Optional, Tuple
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit


def plot_expectation_values(
    labels: List[str],
    values: List[float],
    errors: Optional[List[float]] = None,
    title: str = "Expectation Values",
    figsize: Tuple[int, int] = (10, 6),
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot expectation values with optional error bars.

    Args:
        labels: Observable labels
        values: Expectation values
        errors: Optional standard deviations
        title: Plot title
        figsize: Figure size
        save_path: Optional path to save figure

    Returns:
        Tuple of (figure, axes)
    """
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(labels))

    if errors is not None:
        ax.errorbar(x, values, yerr=errors, fmt="o-", capsize=5, capthick=2, markersize=8)
    else:
        ax.plot(x, values, "o-", markersize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_xlabel("Observable")
    ax.set_ylabel("Expectation Value")
    ax.set_title(title)
    ax.axhline(y=0, color="gray", linestyle="--", alpha=0.5)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    return fig, ax


def plot_counts(
    counts: dict,
    title: str = "Measurement Results",
    figsize: Tuple[int, int] = (10, 6),
    sort: bool = True,
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot measurement counts as bar chart.

    Args:
        counts: Dictionary of {bitstring: count}
        title: Plot title
        figsize: Figure size
        sort: Sort by count descending
        save_path: Optional path to save figure

    Returns:
        Tuple of (figure, axes)
    """
    fig, ax = plt.subplots(figsize=figsize)

    if sort:
        items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    else:
        items = list(counts.items())

    labels = [item[0] for item in items]
    values = [item[1] for item in items]

    ax.bar(labels, values, color="steelblue", edgecolor="black")
    ax.set_xlabel("Measurement Outcome")
    ax.set_ylabel("Count")
    ax.set_title(title)

    if len(labels) > 10:
        plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    return fig, ax


def draw_circuit(
    circuit: QuantumCircuit,
    output_type: str = "mpl",
    figsize: Optional[Tuple[int, int]] = None,
    save_path: Optional[str] = None
):
    """
    Draw a quantum circuit.

    Args:
        circuit: QuantumCircuit to draw
        output_type: "mpl", "text", or "latex"
        figsize: Optional figure size for mpl output
        save_path: Optional path to save figure

    Returns:
        Circuit drawing (type depends on output_type)
    """
    kwargs = {}
    if figsize and output_type == "mpl":
        kwargs["figsize"] = figsize

    drawing = circuit.draw(output=output_type, **kwargs)

    if save_path and output_type == "mpl":
        drawing.savefig(save_path, dpi=150, bbox_inches="tight")

    return drawing


def compare_ideal_vs_real(
    ideal_values: List[float],
    real_values: List[float],
    labels: List[str],
    title: str = "Ideal vs Real Comparison",
    figsize: Tuple[int, int] = (10, 6)
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Compare ideal (simulated) vs real (hardware) results.

    Args:
        ideal_values: Values from ideal simulation
        real_values: Values from real hardware
        labels: Observable labels
        title: Plot title
        figsize: Figure size

    Returns:
        Tuple of (figure, axes)
    """
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(labels))
    width = 0.35

    ax.bar(x - width / 2, ideal_values, width, label="Ideal", color="steelblue")
    ax.bar(x + width / 2, real_values, width, label="Real", color="coral")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_xlabel("Observable")
    ax.set_ylabel("Expectation Value")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    return fig, ax


def plot_convergence(
    iterations: List[int],
    values: List[float],
    title: str = "Convergence",
    xlabel: str = "Iteration",
    ylabel: str = "Value",
    figsize: Tuple[int, int] = (10, 6)
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot convergence over iterations.

    Args:
        iterations: Iteration numbers
        values: Values at each iteration
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        figsize: Figure size

    Returns:
        Tuple of (figure, axes)
    """
    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(iterations, values, "b-", linewidth=1.5)
    ax.fill_between(iterations, values, alpha=0.3)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

    # Mark final value
    final = values[-1]
    ax.axhline(y=final, color="r", linestyle="--", alpha=0.7, label=f"Final: {final:.4f}")
    ax.legend()

    plt.tight_layout()
    return fig, ax
