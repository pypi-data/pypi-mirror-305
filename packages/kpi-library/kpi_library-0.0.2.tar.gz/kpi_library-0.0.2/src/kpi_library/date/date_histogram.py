# kpi_library/date/date_histogram.py
from typing import Tuple, List
from datetime import datetime
import pandas as pd


def date_histogram(data: pd.Series, num_bins: int) -> Tuple[List[datetime], List[int]]:
    """
    Computes the histogram values of a date, time, or datetime variable.

    Parameters
    ----------
    data: :obj:`pandas.Series`
        Pandas object containing date values.
    num_bins: int
        Number of bins to build the histogram, i.e, the number of columns in the histogram.

    Return
    ------
    bins: list of :obj:`datetime`
        List containing the lower bound of each bin, i.e., the smallest date, time, or datetime that falls in that
        bin.
    freq: list of int
        List containing the number of elements per bin.
    """
    # Define the time intervals for binning regarding the number of bins and the range between the maximum and
    # minimum (self.__min = start_date, self.__max = end_date)
    min_date = data.min()
    max_date = data.max()
    offset = (max_date - min_date) / num_bins
    if offset == pd.Timedelta(0):
        start_date = min_date - pd.Timedelta(days=1)
        offset = pd.Timedelta(days=2) / 5
    else:
        start_date = min_date
    # create bins
    bins = [start_date + i * offset for i in range(num_bins + 1)]
    # count the number of dates in each bin
    freq = [0] * num_bins
    prev_date = start_date
    for index, date in enumerate(bins[1:-1]):
        freq[index] = sum((prev_date <= data) & (data < date))
        prev_date = date
    freq[-1] = sum((prev_date <= data) & (data <= bins[-1]))
    # return the result
    return bins, freq
