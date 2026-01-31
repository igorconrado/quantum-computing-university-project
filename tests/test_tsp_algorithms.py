"""Unit tests for TSP algorithms."""

import pytest
import sys
from pathlib import Path

# Add programming directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "programming"))

from tsp_comparison.classical.brute_force import brute_force, calculate_distance
from tsp_comparison.classical.nearest_neighbor import nearest_neighbor
from tsp_comparison.classical.simulated_annealing import simulated_annealing


class TestCalculateDistance:
    """Tests for distance calculation utility."""

    def test_same_point(self):
        """Distance from point to itself should be zero."""
        point = (0, 0)
        assert calculate_distance(point, point) == 0.0

    def test_horizontal_distance(self):
        """Test horizontal distance calculation."""
        p1 = (0, 0)
        p2 = (3, 0)
        assert calculate_distance(p1, p2) == 3.0

    def test_vertical_distance(self):
        """Test vertical distance calculation."""
        p1 = (0, 0)
        p2 = (0, 4)
        assert calculate_distance(p1, p2) == 4.0

    def test_diagonal_distance(self):
        """Test diagonal distance (3-4-5 triangle)."""
        p1 = (0, 0)
        p2 = (3, 4)
        assert calculate_distance(p1, p2) == 5.0

    def test_symmetry(self):
        """Distance should be symmetric."""
        p1 = (1, 2)
        p2 = (4, 6)
        assert calculate_distance(p1, p2) == calculate_distance(p2, p1)


class TestBruteForce:
    """Tests for brute force TSP solver."""

    @pytest.fixture
    def simple_cities(self):
        """Simple 4-city square configuration."""
        return [(0, 0), (0, 1), (1, 1), (1, 0)]

    @pytest.fixture
    def triangle_cities(self):
        """Equilateral triangle configuration."""
        return [(0, 0), (1, 0), (0.5, 0.866)]

    def test_minimum_cities(self, simple_cities):
        """Brute force should work with minimum input."""
        route, distance, _ = brute_force(simple_cities)
        assert len(route) == 4
        assert distance > 0

    def test_returns_valid_route(self, simple_cities):
        """Route should contain all cities exactly once."""
        route, _, _ = brute_force(simple_cities)
        assert set(route) == {0, 1, 2, 3}
        assert len(route) == len(set(route))

    def test_optimal_square_distance(self, simple_cities):
        """Optimal route for unit square should be 4."""
        _, distance, _ = brute_force(simple_cities)
        assert abs(distance - 4.0) < 0.001

    def test_execution_time_returned(self, simple_cities):
        """Should return positive execution time."""
        _, _, exec_time = brute_force(simple_cities)
        assert exec_time >= 0


class TestNearestNeighbor:
    """Tests for nearest neighbor heuristic."""

    @pytest.fixture
    def line_cities(self):
        """Cities in a line configuration."""
        return [(0, 0), (1, 0), (2, 0), (3, 0)]

    @pytest.fixture
    def square_cities(self):
        """Unit square cities."""
        return [(0, 0), (0, 1), (1, 1), (1, 0)]

    def test_returns_valid_route(self, line_cities):
        """Route should contain all cities."""
        route, _, _ = nearest_neighbor(line_cities)
        assert set(route) == {0, 1, 2, 3}

    def test_respects_start_city(self, line_cities):
        """Should start from specified city."""
        route, _, _ = nearest_neighbor(line_cities, start=2)
        assert route[0] == 2

    def test_line_optimal(self, line_cities):
        """For line configuration, NN should find optimal."""
        _, distance, _ = nearest_neighbor(line_cities, start=0)
        # Optimal is 0->1->2->3->0 = 3 + 3 = 6
        assert abs(distance - 6.0) < 0.001

    def test_execution_time_returned(self, line_cities):
        """Should return positive execution time."""
        _, _, exec_time = nearest_neighbor(line_cities)
        assert exec_time >= 0


class TestSimulatedAnnealing:
    """Tests for simulated annealing solver."""

    @pytest.fixture
    def small_cities(self):
        """Small set of cities for fast testing."""
        return [(0, 0), (1, 0), (1, 1), (0, 1)]

    def test_returns_valid_route(self, small_cities):
        """Route should contain all cities."""
        route, _, _ = simulated_annealing(small_cities)
        assert set(route) == {0, 1, 2, 3}

    def test_returns_positive_distance(self, small_cities):
        """Distance should be positive."""
        _, distance, _ = simulated_annealing(small_cities)
        assert distance > 0

    def test_respects_parameters(self, small_cities):
        """Should work with custom parameters."""
        route, distance, _ = simulated_annealing(
            small_cities,
            initial_temp=100,
            cooling_rate=0.99,
            min_temp=0.1
        )
        assert len(route) == 4
        assert distance > 0

    def test_reasonable_solution_quality(self, small_cities):
        """SA solution should not be much worse than optimal."""
        _, sa_distance, _ = simulated_annealing(small_cities)
        _, optimal_distance, _ = brute_force(small_cities)
        # SA should be within 50% of optimal for small instances
        assert sa_distance <= optimal_distance * 1.5


class TestAlgorithmConsistency:
    """Cross-algorithm consistency tests."""

    @pytest.fixture
    def test_cities(self):
        """Standard test configuration."""
        return [(0, 0), (2, 0), (2, 2), (0, 2)]

    def test_all_algorithms_same_city_count(self, test_cities):
        """All algorithms should return routes with same length."""
        bf_route, _, _ = brute_force(test_cities)
        nn_route, _, _ = nearest_neighbor(test_cities)
        sa_route, _, _ = simulated_annealing(test_cities)

        assert len(bf_route) == len(nn_route) == len(sa_route) == 4

    def test_heuristics_not_worse_than_double_optimal(self, test_cities):
        """Heuristics should be within 2x of optimal."""
        _, optimal, _ = brute_force(test_cities)
        _, nn_dist, _ = nearest_neighbor(test_cities)
        _, sa_dist, _ = simulated_annealing(test_cities)

        assert nn_dist <= optimal * 2
        assert sa_dist <= optimal * 2
