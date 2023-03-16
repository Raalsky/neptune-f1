import sys

import numpy as np
import pytest

from neptune_f1.metric_over_lap_period import MetricOverLapPeriod

IS_MACOS = sys.platform == "darwin"


@pytest.mark.skipif(IS_MACOS, reason="Dont like MACOS")
def test_name():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=10)

    assert metric.name == "Sample Metric"


@pytest.mark.skipif(IS_MACOS, reason="Dont like MACOS")
def test_repr():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=10)

    assert str(metric) == "sample-metric"


@pytest.mark.skipif(IS_MACOS, reason="Dont like MACOS")
def test_array_with_all_values():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=3)

    metric.log(at_distance=0, value=10)
    metric.log(at_distance=1, value=20)
    metric.log(at_distance=2, value=30)

    np.testing.assert_array_equal(metric.result(), np.array([10, 20, 30]))


def test_array_with_single_missing_value():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=3)

    metric.log(at_distance=0, value=10)
    metric.log(at_distance=2, value=30)

    np.testing.assert_array_equal(metric.result(), np.array([10, 20, 30]))


def test_array_without_any_value():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=3)

    with pytest.raises(AssertionError):
        metric.result()


def test_values_interpolation():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=5)

    metric.log(at_distance=0, value=50)
    metric.log(at_distance=4, value=10)

    np.testing.assert_array_equal(metric.result(), np.array([50, 40, 30, 20, 10]))


def test_resolution():
    metric = MetricOverLapPeriod(name="Sample Metric", lap_length=2, resolution=10)

    metric.log(at_distance=0.5, value=50)
    metric.log(at_distance=1.3, value=10)

    np.testing.assert_array_equal(
        metric.result(), np.array([50, 50, 50, 50, 50, 50, 45, 40, 35, 30, 25, 20, 15, 10, 10, 10, 10, 10, 10, 10])
    )
