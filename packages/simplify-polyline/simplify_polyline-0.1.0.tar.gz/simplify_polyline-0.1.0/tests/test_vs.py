"""Test visvalingham-whyatt simplification.

:author: Shay Hill
:created: 2023-03-18
"""

import numpy as np

from simplify_polyline.simplifiers import simplify, vw_simplify


def loops_equal(a, b):
    """Return true if sequences contain the same values,
    in the same order, with different starting points."""
    list_a = [tuple(x) for x in a]
    list_b = [tuple(x) for x in b]
    if (list_a[0] == list_a[-1]) != (list_b[0] == list_b[-1]):
        return False
    if list_a[0] == list_a[-1]:
        list_a = list_a[:-1]
        list_b = list_b[:-1]
    if len(list_a) != len(list_b):
        return False
    for i in range(len(list_a)):
        if (
            list_a[i:] == list_b[: len(list_a) - i]
            and list_a[:i] == list_b[len(list_a) - i :]
        ):
            return True
    breakpoint()
    return False


class TestVW:
    """Test visvalingham-whyatt simplification."""

    def test_near_linear(self):
        """Linear and near-linear points are removed."""
        points = [(0, 0), (1, 0), (2, 0), (3, 0.01), (4, 0)]
        np.testing.assert_almost_equal(vw_simplify(points, 1), [(0, 0), (4, 0)])

    def test_spike(self):
        """Linear and near-linear points are removed."""
        points = [(0, 0), (1, 0), (1, 1), (2, 2), (0.99, 1), (0, 1)]
        np.testing.assert_almost_equal(
            vw_simplify(points, 0.1), [(0, 0), (1, 0), (1, 1), (0, 1)]
        )

    def test_area(self):
        """Area calculation is correct."""
        points = [(0, 0), (1, 0), (1, 1)]
        true_area = 1 / 2
        slightly_less_than_true_area = true_area - 0.01
        slightly_more_than_true_area = true_area + 0.01
        np.testing.assert_equal(
            vw_simplify(points, slightly_more_than_true_area), [(0, 0), (1, 1)]
        )
        np.testing.assert_equal(
            vw_simplify(points, slightly_less_than_true_area), [(0, 0), (1, 0), (1, 1)]
        )

    def test_closes(self):
        """Simplification closes the path."""
        points = [(0, 0), (1, 0), (1, 1), (0, 0)]
        np.testing.assert_equal(
            vw_simplify(points, 0), [(0, 0), (1, 0), (1, 1), (0, 0)]
        )


class TestDP:
    """Test Douglas-Peucker simplification."""

    def test_near_linear(self):
        """Linear and near-linear points are removed."""
        points = [(0, 0), (1, 0), (2, 0), (3, 0.01), (4, 0)]
        np.testing.assert_almost_equal(simplify(points, 1), [(0, 0), (4, 0)])

    def test_polyline_spike(self):
        """Spikes are retained in polylines."""
        points = [(0, 0), (1, 0), (1, 1), (2, 2), (0.99, 1), (0, 1)]
        np.testing.assert_almost_equal(simplify(points, 0.1), points)

    def test_polygon_spike(self):
        """Spikes are retained in polygons."""
        points = [(0, 0), (1, 0), (1, 1), (2, 2), (0.99, 1), (0, 1), (0, 0)]
        result = list(simplify(points, 0.1))
        expect = list(points)
        assert loops_equal(result, expect)
        # np.testing.assert_almost_equal(simplify(points, 0.1), points)


class TestCorbasia:
    """Test results against data supplied by r/Corbasia."""

    def test_is_closed(self):
        """Path is closed."""
        points = [
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (3, 6),
            (4, 6),
            (5, 6),
            (6, 6),
        ]
        np.testing.assert_almost_equal(
            simplify(points, min_dist=1, is_closed=True), [(2, 1), (2, 6), (6, 6)]
        )

    def test_is_closed_implicitly(self):
        """Path is closed."""
        points = [
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (3, 6),
            (4, 6),
            (5, 6),
            (6, 6),
            (2, 1),
        ]
        assert loops_equal(
            simplify(points, min_dist=1), [(2, 1), (2, 6), (6, 6), (2, 1)]
        )

    def test_is_not_closed(self):
        """Path is not closed."""
        points = [
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (3, 6),
            (4, 6),
            (5, 6),
            (6, 6),
        ]
        np.testing.assert_almost_equal(
            simplify(points, min_dist=1), [(2, 1), (2, 6), (6, 6)]
        )
