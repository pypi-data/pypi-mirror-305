# kpi_library/one_variable_methods/numeric.py
from typing import Dict, List, Union

import numpy as np
import pandas as pd
from scipy import stats

from ..result_types import ResultTypes
from ..uni_variable import OneVarMethods
from ..errors import DataTypeError


class NumericMethods(OneVarMethods):
    """
    Numeric column quality profiling methods.

    This module looks for profiling numeric data, getting statistics, the significant digits, and possible outliers, and
    visualizing them with a box plot or a histogram.

    Attributes
    ----------
    data: pandas.Series
        Object containing the numeric data to be processed without missing values.
    data_numpy: numpy.ndarray
        Numpy object containing the numeric data to be processed, without null values.
    empty: bool
        Whether the dataset is empty or not, after dropping all missing values.
    min_var: int or float
    max_var: int or float
    quartile1: float
    quartile3: float
    mean_var: float
    std_var: float
    """
    # parameters
    data: pd.Series
    data_numpy: np.ndarray
    empty: bool
    min_var: Union[int, float]
    max_var: Union[int, float]
    quartile1: float
    quartile3: float
    mean_var: float
    std_var: float

    # constructor
    def __init__(self, dataset: pd.Series):
        """
        Create a NumericMethods object which contains the data to be processed in a pandas Series object.

        Parameters
        ----------
        dataset: :obj:`pandas.Series`
            Object containing the data to be processed.
        """
        # saving dataset (data), nº of rows (n_rows), and name (name)
        super(NumericMethods, self).__init__(class_name='numeric', dataset=dataset)
        # drop null values and get both pandas.Series and numpy.ndarray
        self.__check_data(dataset=dataset)
        self.data_numpy: np.ndarray = self.data.to_numpy()

    def __turn_correct_format(self, result: Union[int, float, np.ndarray]) -> Union[int, float]:
        """"""
        if isinstance(result, np.int64):
            self.data_type = ResultTypes.INT.value
            return int(result)
        self.data_type = ResultTypes.FLOAT.value
        return float(result)

    def __check_data(self, dataset: pd.Series) -> None:
        """
        Check the correct format and type of the dataset.

        Parameters
        ----------
        dataset: :obj:`pandas.Series`
            Pandas object containing the numeric data to be processed.

        Raises
        ------
        DataTypeError
            If the data type of `dataset` is not numeric.

        Returns
        -------
        dataset: :obj:`pandas.Series`
            Pandas object containing the numeric data to be processed.
        """
        # drop null values and check if dataset is empty
        self.data.dropna(inplace=True)
        self.empty = self.data.empty
        if not self.empty and str(dataset.dtype) not in ['int64', 'float64']:
            raise DataTypeError(f'The column format is incorrect, the values should be numeric but they are not. The '
                                f'type of the data is {dataset.dtype}.', code=400)

    def fifth_percentile(self) -> Union[None, float]:
        """
        This method returns the fifth percentile of `self.data`.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1,2,3,4,5,6,7], name='ID'))
        >>> nm.fifth_percentile()
        1.3
        >>> nm = NumericMethods(pd.Series([1,None,3,4,5,6,7]))
        >>> nm.fifth_percentile()
        1.5
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.fifth_percentile()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of one element containing the fifth-percentile of the data (`self.data`).
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        return float(np.percentile(self.data_numpy, q=5))

    def first_quartile(self) -> Union[float, None]:
        """
        Computes the firts quartile (25th-percentile) of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1,2,3,4,5,6,7], name='ID'))
        >>> nm.first_quartile()
        2.5
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.first_quartile()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of one element containing the first quartile (twenty-fifth percentile) of the data (`self.data`).
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.quartile1 = getattr(self, 'quartile1', float(np.percentile(self.data_numpy, q=25)))
        return self.quartile1

    def median(self) -> Union[int, float, None]:
        """
        Computes the median of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1,2,3,4,5,6,7], name='ID'))
        >>> nm.median()
        4.0
        >>> nm = NumericMethods(pd.Series([1,None,3,4,5,6,7], name='ID'))
        >>> nm.median()
        4.5
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.median()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of one element containing the first quartile (twenty-fifth percentile) of the data (`self.data`).
        """
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        return self.__turn_correct_format(np.median(self.data_numpy))

    def third_quartile(self) -> Union[float, None]:
        """
        Computes the third quantile of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.third_quartile()
        5.5
        >>> nm = NumericMethods(pd.Series([1, None, 3, 4, 5, 6, 7]))
        >>> nm.third_quartile()
        5.75
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.third_quartile()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the third quantile, i.e., the
            75th-percentile of the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.quartile3 = getattr(self, 'quartile3', float(np.percentile(self.data_numpy, q=75)))
        return self.quartile3

    def ninety_fifth_percentile(self) -> Union[float, None]:
        """
        Computes the 95th-percentile of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.ninety_fifth_percentile()
        6.699999999999999
        >>> nm = NumericMethods(pd.Series([1, None, 3, 4, 5, 6, 7]))
        >>> nm.ninety_fifth_percentile()
        6.75
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.ninety_fifth_percentile()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the 95th-percentile of the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        return float(np.percentile(self.data_numpy, q=95))

    def mean(self) -> Union[float, None]:
        """
        Gets the mean of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.mean()
        4.0
        >>> nm = NumericMethods(pd.Series([1, None, 3, 4, 5, 6, 7], name=''))
        >>> nm.mean()
        4.333333333333333
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.mean()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            Mean value obtained from the given data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.mean_var = getattr(self, 'mean_var', float(np.mean(self.data_numpy)))
        return self.mean_var

    def min(self) -> Union[int, float, None]:
        """
        Gets the minimum value of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.min()
        1
        >>> nm = NumericMethods(pd.Series([1, 2, None, 4, 5, 6, 7]))
        >>> nm.min()
        1.0
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.min()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the minimum value of the data.
        """
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.min_var = getattr(self, 'min_var', self.__turn_correct_format(np.min(self.data_numpy)))
        return self.min_var

    def max(self) -> Union[int, float, None]:
        """
        Gets the maximum value of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.max()
        7
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, None]))
        >>> nm.max()
        6.0
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.max()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the maximum value of the data.
        """
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.max_var = getattr(self, 'max_var', self.__turn_correct_format(np.max(self.data_numpy)))
        return self.max_var

    def mode(self, return_element: str = 'element') -> Union[int, float, None]:
        """
        Computes the mode of the given data.

        Parameters
        ----------
        return_element: {'element', 'frequency', 'normalized'}. Default 'element'.
            Whether the method should return the most frequent element of the data, its frequency or its normalized
            frequency, i.e. the percentage of data that are this element.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.mode()
        1.0
        >>> nm.mode(return_element='frequency')
        1
        >>> nm.mode(return_element='normalized')
        0.14286
        >>> nm = NumericMethods(pd.Series([1, None, 1, 4, 5, 6, 7, None, None]))
        >>> nm.mode(return_element='frequency')
        2
        >>> nm.mode(return_element='normalized')
        0.33333
        >>> nm.mode(return_element='kdjfask')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `return_element` is not correct, it \
should be any of the following values: ['element', 'frequency', 'normalized'], but it is kdjfask.
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.mode()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the mode.
        """
        # check if dataset is empty
        if self.empty:
            self.data_type = ResultTypes.FLOAT.value
            return None
        # check parameters
        self._check_enum_parameter(
            parameter=return_element, parameter_name='return_element', values=['element', 'frequency', 'normalized'])
        # obtain most frequent element of data
        mode = stats.mode(self.data_numpy, keepdims=False, nan_policy='omit')
        if return_element == 'element':
            self.data_type = ResultTypes.FLOAT.value
            return float(mode.mode)
        elif return_element == 'frequency':
            self.data_type = ResultTypes.INT.value
            return int(mode.count)

        self.data_type = ResultTypes.FLOAT.value
        return round(mode.count/self.data_numpy.size, 5)

    def std(self) -> Union[float, None]:
        """
        Computes the standard deviation of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.std()
        2.0
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, None, 7]))
        >>> nm.std()
        1.9720265943665387
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.std()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the standard deviation.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.std_var = getattr(self, 'std_var', float(np.std(self.data_numpy)))
        return self.std_var

    def range(self) -> Union[int, float, None]:
        """
        Computes the range of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.range()
        6
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, None, 7]))
        >>> nm.range()
        6.0
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.range()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the range.
        """
        # check if dataset is empty
        if self.empty:
            self.data_type = ResultTypes.FLOAT.value
            return None
        # compute statistic
        self.min_var = getattr(self, 'min_var', self.__turn_correct_format(np.min(self.data_numpy)))
        self.max_var = getattr(self, 'max_var', self.__turn_correct_format(np.max(self.data_numpy)))
        return self.max_var - self.min_var

    def iqr(self) -> Union[float, None]:
        """
        Computes the interquartile rante (iqr) of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.iqr()
        3.0
        >>> nm = NumericMethods(pd.Series([1, 2, None, 4, 5, 6, 7]))
        >>> nm.iqr()
        3.25
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.iqr()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the iqr of the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.quartile1 = getattr(self, 'quartile1', float(np.percentile(self.data_numpy, q=25)))
        self.quartile3 = getattr(self, 'quartile3', float(np.percentile(self.data_numpy, q=75)))
        return self.quartile3 - self.quartile1

    def coefficient_variation(self) -> Union[float, None]:
        """
        Computes the coefficient of variation of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.coefficient_variation()
        0.5
        >>> nm = NumericMethods(pd.Series([1, 2, 3, None, 5, 6, 7]))
        >>> nm.coefficient_variation()
        0.5400617248673217
        >>> nm = NumericMethods(pd.Series([0, 0, 0, 0]))
        >>> nm.coefficient_variation()
        nan
        >>> nm = NumericMethods(pd.Series([5, -5]))
        >>> nm.coefficient_variation()
        inf
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.coefficient_variation()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the coefficient of variation in the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        self.std_var = getattr(self, 'std_var', float(np.std(self.data_numpy)))
        self.mean_var = getattr(self, 'mean_var', float(np.mean(self.data_numpy)))
        # edge cases (different behaviour)
        if self.mean_var == 0:
            if self.std_var == 0:
                # If both the mean and the standard deviation are zero, nan is returned
                return float("nan")
            # If the mean is zero and the standard deviation is nonzero, inf is returned.
            return float('inf')
        # normal cases
        return self.std_var / self.mean_var

    def mad(self) -> Union[float, None]:
        """
        Computes the Median Absolute Deviation (MAD) of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.mad()
        2.0
        >>> nm = NumericMethods(pd.Series([1, 2, 3, None, 5, 6, 7], name='ID'))
        >>> nm.mad()
        2.0
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.mad()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the Median Absolute Deviation
            (MAD) of the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        return float(stats.median_abs_deviation(self.data, nan_policy='omit'))

    def kurtosis(self) -> Union[float, None]:
        """
        Computes the kurtosis of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.kurtosis()
        -1.2000000000000002
        >>> nm = NumericMethods(pd.Series([1, 2, 3, None, 5, 6, 7]))
        >>> nm.kurtosis()
        -1.875
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.kurtosis()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the kurtosis of the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        return float(self.data.kurtosis(skipna=True))

    def skewness(self) -> Union[float, None]:
        """
        Computes the skewness of the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.skewness()
        0.0
        >>> nm = NumericMethods(pd.Series([1, 2, None, 4, 5, 6, None], name='ID'))
        >>> nm.skewness()
        -0.23551393640880616
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.skewness()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the skewness of the data.
        """
        self.data_type = ResultTypes.FLOAT.value
        # check if dataset is empty
        if self.empty:
            return None
        # compute statistic
        return float(self.data.skew(skipna=True))

    def sum(self) -> Union[int, float, None]:
        """
        Computes the sum of the elements in the given data.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, 2, 3, 4, 5, 6, 7], name='ID'))
        >>> nm.sum()
        28
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.sum()

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the sum of all elements in the given
            data.
        """
        # check if dataset is empty
        if self.empty:
            self.data_type = ResultTypes.INT.value
            return None
        # compute statistic
        return self.__turn_correct_format(np.sum(self.data_numpy))

    def count_zeros(self, normalized: Union[bool, str] = False) -> Union[int, float, None]:
        """
        Computes the number of zeros in the given data.

        Parameters
        ----------
        normalized: bool or str, optional. Default, False.
            Whether the output should be normalized or not.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, -2, 3, 4, 0, 6, -5], name='ID'))
        >>> nm.count_zeros()
        1
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.count_zeros()
        0

        Returns
        -------
        _: int or float
            Number of zeros in the data.
        """
        # check if dataset is empty
        if self.empty:
            self.data_type = ResultTypes.INT.value
            return 0
        # check parameter normalized
        normalized = self._check_boolean_parameter(parameter=normalized, parameter_name='normalized')
        # compute number of zeros in self.data
        if normalized:
            self.data_type = ResultTypes.FLOAT.value
            return float(round(np.sum(self.data_numpy == 0) / self.n_rows, 5))
        self.data_type = ResultTypes.INT.value
        return int(np.sum(self.data_numpy == 0))

    def count_negatives(self, normalized: Union[bool, str] = False) -> Union[int, float, None]:
        """
        Computes the number of negative values of the given data.

        Parameters
        ----------
        normalized: bool or str, optional. Default, False.
            Whether the output should be normalized or not.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1, -2, 3, 4, 0, 6, -5], name='ID'))
        >>> nm.count_negatives()
        2
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.count_negatives()
        0

        Returns
        -------
        _: int or float
            Number of negative values in the data.
        """
        # check if dataset is empty
        if self.empty:
            self.data_type = ResultTypes.INT.value
            return 0
        # check normalized parameter
        normalized = self._check_boolean_parameter(parameter_name='normalized', parameter=normalized)
        # compute number of negative values in self.data
        if normalized:
            self.data_type = ResultTypes.FLOAT.value
            return float(round(np.sum(self.data_numpy < 0)/self.n_rows, 5))
        self.data_type = ResultTypes.INT.value
        return int(np.sum(self.data_numpy < 0))

    def box_plot(self) -> Union[None, Dict[str, Union[int, float]]]:
        """
        Extracts from df the necessary information of the numerical columns to visualize the data in a box plot. Those
        elements are the first, second and third quartile, the maximum and minimum element, and those values that are
        larger or smaller than the interquartile range.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1,2,3,4,5,6,7], name='ID'))
        >>> nm.box_plot()
        {'min': 1.0, 'max': 7.0, 'first_quartile': 2.5, 'median': 4.0, 'third_quartile': 5.5, 'outliers': []}
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.box_plot()

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the data and the result after processing the given data by the
            box plot method.
        """
        self.data_type = ResultTypes.BOX_PLOT.value
        # check if dataset is empty
        if self.empty:
            return None
        # obtain statistics
        statistics = np.percentile(a=self.data_numpy, q=[0, 25, 50, 75, 100])
        outliers = self.__find_outliers(percentiles=statistics[[1, 3]])

        result = {
            'min': statistics[0],
            'max': statistics[4],
            'first_quartile': statistics[1],
            'median': statistics[2],
            'third_quartile': statistics[3],
            'outliers': outliers
        }

        # return the element of the box plot
        return result

    def histogram(self, num_bins: Union[str, int] = 10) -> List[Dict[str, Union[str, int, float]]]:
        """
        Extracts from the data (`self.data`) the necessary information to visualize the data in a histogram.

        Parameters
        ----------
        num_bins: int or str
            Number of bins to build the histogram, i.e, the number of columns in the histogram

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1,2,3,4,5,6,7], name='ID'))
        >>> nm.histogram(num_bins=3)
        [{'limits': '[1.0, 3.0)', 'frequency': 2}, {'limits': '[3.0, 5.0)', 'frequency': 2}, \
{'limits': '[5.0, 7.0]', 'frequency': 3}]
        >>> nm.histogram(num_bins='skfj')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `num_bins` must be an integer, but it's \
not. Its value is skfj.
        >>> nm.histogram(num_bins=-2)
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `num_bins` must be larger or equal to 2,\
 but it is actual value is -2.
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.histogram()
        []

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the values of the histogram in a string
            format, where `limits` is the boundaries of the bin and `frequency` is the number of element that fit in it.

        Raises
        ------
        IncorrectParameterError
            If num_bins is less than 2, or it is not a number.
        """
        self.data_type = ResultTypes.HISTOGRAM.value
        # check if dataset is empty
        if self.empty:
            return []
        # Check parameter `num_bins`
        num_bins = self._check_int_parameter(parameter=num_bins, parameter_name='num_bins', ge=2)

        # get histogram values
        y_freq, x_bins = np.histogram(self.data.dropna(inplace=False), bins=num_bins)
        bins = zip(x_bins[:-2], x_bins[1:-1])
        result = [
            {'limits': f'[{round(b[0], 4)}, {round(b[1], 4)})', 'frequency': int(freq)}
            for b, freq in zip(bins, y_freq[:-1])
        ] + [{'limits': f'[{round(x_bins[-2], 4)}, {round(x_bins[-1], 4)}]', 'frequency': int(y_freq[-1])}]
        # return
        return result

    def outliers(self, normalized: Union[bool, str] = False) -> Union[float, int]:
        """
        Checks the data, obtains possible outliers and returns the number of outliers found as an integer or float, if
        the output is normalized.

        Parameters
        ----------
        normalized: bool or str, optional. Default, False.
            Whether the output should be normalized or not.

        Examples
        --------
        >>> nm = NumericMethods(pd.Series([1.0253,2.6,3.420,4.26,5,6.075,7.200]))
        >>> nm.outliers()
        0
        >>> nm.outliers(normalized='True')
        0.0
        >>> nm = NumericMethods(pd.Series([-2.0253,2.6,3.420,4.26,5,6.075,10], name='ID'))
        >>> nm.outliers(normalized='false')
        2
        >>> nm.outliers(normalized='True')
        0.28571
        >>> nm = NumericMethods(pd.Series([-2.0253,2.6,3.420,4.26,5,None,10], name='ID'))
        >>> nm.outliers(normalized=True)
        0.33333
        >>> nm.outliers(normalized='sdf')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `normalized` is incorrect, it must be a \
boolean, but its value is sdf.
        >>> nm = NumericMethods(pd.Series([None,None, None, None]))
        >>> nm.outliers()
        0

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the processed data and the number of outliers found, as an
            integer or float, if the output is normalized.
        """
        # check if dataset is empty
        if self.empty:
            self.data_type = ResultTypes.INT.value
            return 0
        # check and transform the normalized parameter
        normalized = self._check_boolean_parameter(parameter=normalized, parameter_name='normalized')
        # compute the outliers founded and return the number
        num_elements: int = self.data_numpy.size
        outliers: int = len(self.__find_outliers(np.percentile(self.data_numpy, q=[25, 75])))

        if normalized:
            self.data_type = ResultTypes.FLOAT.value
            return round(outliers/num_elements, 5)

        self.data_type = ResultTypes.INT.value
        return outliers

    def __find_outliers(self, percentiles: np.ndarray) -> List[Union[int, float]]:
        """
        This method uses the interquartile range (IQR) method to find possible outliers. The interquartile range is a
        measure of statistical dispersion, which shows the spread of the data. It is defined as the difference between
        the 75th and 25th percentiles of the data. The samples are classified as outliers because they fall outside the
        range.

        Parameters
        ----------
        percentiles: :obj:`numpy.ndarray`
            First quartile and third quartile from `srs`.

        Return
        ------
        _: :obj:`list` of int or float
            List containing the outliers found.
        """
        # get limits
        iqr_stat = percentiles[1] - percentiles[0]
        upper = percentiles[1] + 1.5 * iqr_stat
        lower = percentiles[0] - 1.5 * iqr_stat
        # compute outliers
        return self.data_numpy[(self.data_numpy > upper) | (self.data_numpy < lower)].tolist()
