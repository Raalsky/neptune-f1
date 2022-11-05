__all__ = ["MetricOverLapPeriod"]

import typing

import numpy as np


def build_nans_list(length: int) -> np.array:
    a = np.empty((length,))
    a[:] = np.nan
    return a


def scale_distance_to_internal_resolution(at_distance: float, resolution: int) -> int:
    return int(resolution * at_distance)


def nan_helper(y):
    """Helper to handle indices and logical indices of NaNs.

    Input:
        - y, 1d numpy array with possible NaNs
    Output:
        - nans, logical indices of NaNs
        - index, a function, with signature indices= index(logical_indices),
          to convert logical indices of NaNs to 'equivalent' indices
    Example:
        >>> # linear interpolation of NaNs
        >>> nans, x= nan_helper(y)
        >>> y[nans]= np.interp(x(nans), x(~nans), y[~nans])
    """

    return np.isnan(y), lambda z: z.nonzero()[0]


class MetricOverLapPeriod:
    def __init__(self, name: str, lap_length: int, resolution: int = 1):
        self._name: str = name
        self._lap_length: int = lap_length
        self._resolution: int = resolution

        self._data = build_nans_list(length=self._lap_length * self._resolution)

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return self._name.lower().replace(" ", "-")

    def log(self, at_distance: float, value: typing.Any):
        assert 0 <= at_distance < self._lap_length, "Should be distance from 0 to lap total distance"

        at_distance_with_proper_resolution = scale_distance_to_internal_resolution(
            at_distance=at_distance, resolution=self._resolution
        )
        self._data[at_distance_with_proper_resolution] = value

    def _fill_missing_values_with_interpolated_values(self):
        if len(self._data):
            nans, index = nan_helper(self._data)
            self._data[nans] = np.interp(index(nans), index(~nans), self._data[~nans])

    def result(self) -> np.array:
        assert (~np.isnan(self._data)).any(), "Metric has no values"

        if np.isnan(self._data).any():
            self._fill_missing_values_with_interpolated_values()

        return self._data
