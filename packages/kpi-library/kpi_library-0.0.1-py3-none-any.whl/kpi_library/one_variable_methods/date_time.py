# kpi_library/one_variable_methods/date_time.py
import pandas as pd

import json
from typing import List, Dict, Tuple, Union, Optional
from datetime import datetime

from ..uni_variable import OneVarMethods
from ..errors import DataTypeError
from ..result_types import ResultTypes


class DateMethods(OneVarMethods):
    """
    Date column quality profiling methods.

    Parameters
    ----------
    dataset: :obj:`pd.Series`
        Object containing the data to be processed.
    strftime: str, optional.
        The strftime to parse time, e.g. "%d/%m/%Y". See strftime documentation for more information on choices.

    Attributes
    ----------
    data: :obj:`pandas.Series`
        Object containing the data to be processed.
    __freq_dist: :obj:`pandas.Series`
        Object containing the number of times each unique element appears in the data.
    __empty: bool
        Whether the object `data_clean` is empty.
    __initial_n_nan: int
        Number of null values at the beginning of the analysis.
    __non_transformed_dates: int
        Number of non-transformed dates, since they do not follow the given or inferred date format.
    __min: :obj:`Timestamp`
        Minimum date in `data`.
    __max: :obj:`Timestamp`
        Maximum date in `data`.
    __q1: :obj:`Timestamp`
        First quartile of `data`.
    __q3: :obj:`Timestamp`
        Third quartile of `data`.
    """
    # constants
    DATE_TYPES: List[str] = ['datetime', 'date', 'time']
    # attributes
    date: pd.Series
    __freq_dist: pd.Series
    __empty: bool
    __initial_n_nan: int
    __non_transformed_dates: int
    __min: pd.Timestamp
    __max: pd.Timestamp
    __q1: pd.Timestamp
    __q3: pd.Timestamp

    def __init__(self, dataset: pd.Series, strftime: Optional[str] = None):
        super(DateMethods, self).__init__(class_name='date', dataset=dataset)
        # attributes
        self.__empty = False
        self.__initial_n_nan: int = dataset.isna().sum()
        self.__non_transformed_dates = 0
        # clean data
        self.__clean_data(srs=dataset, strftime=strftime)

    def to_dqv(self, method_name: str, parameters: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Examples
        --------
        >>> dm = DateMethods(pd.Series(["01/02/2000", "02/02/2000", "03/02/2000", "04/02/2000", "05/02/2000"]))
        >>> dm.to_dqv(method_name='mean', parameters=[])
        [{'dqv_isMeasurementOf': 'date.mean', 'dqv_computedOn': '', 'rdf_datatype': 'DateTime', 'ddqv_hasParameters': \
[], 'dqv_value': '2000-03-02 14:24:00'}]
        >>> dm.to_dqv(method_name='mode', parameters=[])
        [{'dqv_isMeasurementOf': 'date.mode', 'dqv_computedOn': '', 'rdf_datatype': 'DateTime', 'ddqv_hasParam\
eters': [], 'dqv_value': '2000-01-02 00:00:00'}]
        """
        try:
            value = self.get(method_name)(**self._turn_parameter_to_dictionary(parameters))
        except Exception:
            return [{
                'dqv_isMeasurementOf': f'{self._class_name}.{method_name}',
                'dqv_computedOn': self.name,
                'rdf_datatype': "Error",
                'ddqv_hasParameters': parameters,
                'dqv_value': None
            }]
        # value contains only one result
        return [{
            'dqv_isMeasurementOf': f'{self._class_name}.{method_name}',
            'dqv_computedOn': self.name,
            'rdf_datatype': self.data_type,
            'ddqv_hasParameters': parameters,
            'dqv_value': json.dumps(value) if method_name in ['histogram', 'frequency_distribution'] else value
        }]

    def __clean_data(self, srs: pd.Series, strftime: Optional[str] = None) -> None:
        """
        **Steps**:
        1. Transform data into date format. If `format` is not given, infer date format and transform the data. Those
        dates that could not be transformed, put them as NaN values.
        2. Count number of new NaN values.
        3. Return dataset dropping the NaN values.

        Parameters
        ----------
        srs: :obj:`pd.Series`
            Data to be profiled.
        strftime: str
            The strftime to parse time, e.g. "%d/%m/%Y". See strftime documentation for more information on choices.

        Raises
        ------
        DataTypeError:
            When the data are floats or integers.
        """
        if str(srs.dtype) in ["float64", "int64"]:
            raise DataTypeError("The given column should follow a date_methods format and is currently a numerical"
                                " column.", code=400)
        # drop null values + turn values into dates
        self.data: pd.Series = pd.to_datetime(self.data, errors='coerce', format=strftime)
        self.__non_transformed_dates = self.data.isna().sum() - self.__initial_n_nan
        self.data.dropna(inplace=True)
        self.__empty = self.data.empty

    def number_non_transformed_dates(self) -> int:
        """
        Computes the number of values that could not be transformed into the given or inferred date format.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-20-03 00:00:00", "2022-21-03 00:00:00", "2022-22-03 00:00:00", "2022-23"\
        "-03 00:00:00", "2022-24-03 00:00:00", "2022-25-03 00:00:00"], name='timestamp'), strftime=r'%Y-%d-%m %H:%M:%S')
        >>> dm.number_non_transformed_dates()
        0
        >>> dm = DateMethods(pd.Series(["2022-20-03", "2022-03-21", "2022-22-03", "2022-23-03", "2022-24-03", \
        "2022-25-03"], name='timestamp'), strftime=r'%Y-%d-%m')
        >>> dm.number_non_transformed_dates()
        1
        >>> dm = DateMethods(pd.Series(["01:00:00", None, "27-25-12", "01:00:15", "01:00:20", "01:00:25", \
        "01:00:30"], name='timestamp'))
        >>> dm.number_non_transformed_dates()
        1
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.number_non_transformed_dates()
        0
        >>> dm = DateMethods(pd.Series(["None", "None", "None"], name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.number_non_transformed_dates()
        3

        Returns
        -------
        _: int
            Number of elements that could not be transformed into the given or inferred format.
        """
        self.data_type = ResultTypes.INT.value
        return self.__non_transformed_dates

    def histogram(self, num_bins: Union[int, str] = 10) -> List[Dict[str, int]]:
        """
        Extracts from srs the necessary information to visualize the data in a histogram.

        Parameters
        ----------
        num_bins: int
            Number of bins to build the histogram, i.e, the number of columns in the histogram.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-20-03 00:00:00", "2022-21-03 00:00:00", "2022-22-03 00:00:00", "2022-23"\
        "-03 00:00:00", "2022-24-03 00:00:00", "2022-25-03 00:00:00"], name='timestamp'), strftime=r'%Y-%d-%m %H:%M:%S')
        >>> dm.histogram(num_bins=3)
        [{'limits': '[2022-03-20 00:00:00, 2022-03-21 16:00:00)', 'frequency': 2}, {'limits': '[2022-03-21 16:00:00, \
2022-03-23 08:00:00)', 'frequency': 2}, {'limits': '[2022-03-23 08:00:00, 2022-03-25 00:00:00]', 'frequency': 2}]
        >>> dm = DateMethods(pd.Series(["2022-20-03", "2022-21-03", "2022-22-03", "2022-23-03", "2022-24-03", \
        "2022-25-03"], name='timestamp'), strftime=r'%Y-%d-%m')
        >>> dm.histogram(num_bins=3)
        [{'limits': '[2022-03-20 00:00:00, 2022-03-21 16:00:00)', 'frequency': 2}, \
{'limits': '[2022-03-21 16:00:00, 2022-03-23 08:00:00)', 'frequency': 2}, \
{'limits': '[2022-03-23 08:00:00, 2022-03-25 00:00:00]', 'frequency': 2}]
        >>> dm = DateMethods(pd.Series(["01:00:00", "01:00:05", "01:00:10", "01:00:15", "01:00:20", "01:00:25", \
        "01:00:30"], name='timestamp'), strftime='%H:%M:%S')
        >>> dm.histogram(num_bins=3)
        [{'limits': '[1900-01-01 01:00:00, 1900-01-01 01:00:10)', 'frequency': 2}, {'limits': '[1900-01-01 01:00:10, \
1900-01-01 01:00:20)', 'frequency': 2}, {'limits': '[1900-01-01 01:00:20, 1900-01-01 01:00:30]', 'frequency': 3}]
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.histogram(num_bins=3)
        []

        Raises
        ------
        IncorrectParameters:
            When num_bins is not a number, or it is less than 2.

        Returns
        -------
        _: list of dict
            List of dictionaries containing the values of the histogram, where `limits` is the boundaries of the bin
            and `frequency` is the number of element that fit in it.
        """
        self.data_type = ResultTypes.HISTOGRAM.value
        # check data (if empty, return an empty list)
        if self.__empty:
            return []
        # check parameters
        num_bins = self._check_int_parameter(parameter=num_bins, parameter_name='num_bins', ge=2)
        # compute bins, frequency (histogram information)
        x_bins, y_freq = self.__histogram(num_bins=num_bins)
        # collect bin information into histogram object
        limits = zip(x_bins[:-2], x_bins[1:-1])
        hist = [{'limits': f'[{bin_i[0]}, {bin_i[1]})', 'frequency': int(freq)} for bin_i, freq in zip(limits, y_freq)]
        hist.append({'limits': f'[{x_bins[-2]}, {x_bins[-1]}]', 'frequency': int(y_freq[-1])})
        # return the result
        return hist

    def histogram_percent(self, num_bins: Union[int, str] = 10) -> List[Dict[str, float]]:
        """
        Extracts from srs the necessary information to visualize the data in a histogram.

        Parameters
        ----------
        num_bins: int
            Number of bins to build the histogram, i.e, the number of columns in the histogram.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-20-03 00:00:00", "2022-21-03 00:00:00", "2022-22-03 00:00:00", "2022-23"\
        "-03 00:00:00", "2022-24-03 00:00:00", "2022-25-03 00:00:00"], name='timestamp'), strftime=r'%Y-%d-%m %H:%M:%S')
        >>> dm.histogram_percent(num_bins=3)
        [{'limits': '[2022-03-20 00:00:00, 2022-03-21 16:00:00)', 'frequency': 0.33333}, \
{'limits': '[2022-03-21 16:00:00, 2022-03-23 08:00:00)', 'frequency': 0.33333}, \
{'limits': '[2022-03-23 08:00:00, 2022-03-25 00:00:00]', 'frequency': 0.33333}]
        >>> dm = DateMethods(pd.Series(["2022-20-03", "2022-21-03", "2022-22-03", "2022-23-03", "2022-24-03", \
        "2022-25-03"], name='timestamp'), strftime=r'%Y-%d-%m')
        >>> dm.histogram_percent(num_bins=3)
        [{'limits': '[2022-03-20 00:00:00, 2022-03-21 16:00:00)', 'frequency': 0.33333}, \
{'limits': '[2022-03-21 16:00:00, 2022-03-23 08:00:00)', 'frequency': 0.33333}, \
{'limits': '[2022-03-23 08:00:00, 2022-03-25 00:00:00]', 'frequency': 0.33333}]
        >>> dm = DateMethods(pd.Series(["01:00:00", "01:00:05", "01:00:10", "01:00:15", "01:00:20", "01:00:25", \
        "01:00:30"], name='timestamp'), strftime='%H:%M:%S')
        >>> dm.histogram_percent(num_bins=3)
        [{'limits': '[1900-01-01 01:00:00, 1900-01-01 01:00:10)', 'frequency': 0.28571}, {'limits': '[1900-01-01 01:00\
:10, 1900-01-01 01:00:20)', 'frequency': 0.28571}, {'limits': '[1900-01-01 01:00:20, 1900-01-01 01:00:30]', 'frequency\
': 0.42857}]
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.histogram_percent(num_bins=3)
        []
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.histogram_percent(num_bins=3)
        []

        Raises
        ------
        IncorrectParameters: exception which raises if n_bins < 2.

        Returns
        -------
        _: list of dict
            List of dictionaries containing the values of the histogram, where `limits` is the boundaries of the bin
            and `frequency` is the number of element that fit in it.
        """
        self.data_type = ResultTypes.HISTOGRAM.value
        # check data (if empty, return an empty list)
        if self.__empty:
            return []
        # check parameters
        num_bins = self._check_int_parameter(parameter=num_bins, parameter_name='num_bins', ge=2)
        # compute bins, frequency (histogram information)
        x_bins, y_freq = self.__histogram(num_bins=num_bins)
        # collect bin information into histogram object
        limits = zip(x_bins[:-2], x_bins[1:-1])
        hist = [{
            'limits': f'[{bin_i[0]}, {bin_i[1]})', 'frequency': float(round(freq/self.n_rows, 5))
        } for bin_i, freq in zip(limits, y_freq)]
        hist.append({'limits': f'[{x_bins[-2]}, {x_bins[-1]}]', 'frequency': round(y_freq[-1]/self.n_rows, 5)})
        # return the result
        return hist

    def __histogram(self, num_bins: int) -> Tuple[List[datetime], List[int]]:
        """
        Computes the histogram values of a date, time, or datetime variable.

        Parameters
        ----------
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
        self.__min = getattr(self, '__min', self.data.min())
        self.__max = getattr(self, '__max', self.data.max())
        offset = (self.__max - self.__min) / num_bins
        if offset == pd.Timedelta(0):
            one_day = pd.Timedelta(days=1)
            start_date = self.__min - one_day
            offset = pd.Timedelta(days=2) / 5
        else:
            start_date = self.__min
        # create bins
        bins = [start_date + i * offset for i in range(num_bins + 1)]
        # count the number of dates in each bin
        freq = [0] * num_bins
        prev_date = start_date
        for index, date in enumerate(bins[1:-1]):
            freq[index] = sum((prev_date <= self.data) & (self.data < date))
            prev_date = date
        freq[-1] = sum((prev_date <= self.data) & (self.data <= bins[-1]))
        # return the result
        return bins, freq

    def frequency_distribution(self) -> List[Dict[str, int]]:
        """
        Computes the frequency distribution of the values in the data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-23 00:00:00", "2022-03"\
        "-23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime='%Y-%m-%d %H:%M:%S')
        >>> dm.frequency_distribution()
        [{'item': '2022-03-20 00:00:00', 'frequency': 1}, {'item': '2022-03-21 00:00:00', 'frequency': 1}, \
{'item': '2022-03-23 00:00:00', 'frequency': 2}, {'item': '2022-03-24 00:00:00', 'frequency': 1}, \
{'item': '2022-03-25 00:00:00', 'frequency': 1}]
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-21", "2022-03-23", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime='%Y-%m-%d')
        >>> dm.frequency_distribution()
        [{'item': '2022-03-20 00:00:00', 'frequency': 1}, {'item': '2022-03-21 00:00:00', 'frequency': 1}, {'item': \
'2022-03-23 00:00:00', 'frequency': 2}, {'item': '2022-03-24 00:00:00', 'frequency': 1}, {'item': '2022-03-25 00:00:\
00', 'frequency': 1}]
        >>> dm = DateMethods(pd.Series(["01:00:00", "01:00:05", "01:00:10", "01:00:15", "01:00:15", "01:00:15"], \
        name='timestamp'), strftime='%H:%M:%S')
        >>> dm.frequency_distribution()
        [{'item': '1900-01-01 01:00:00', 'frequency': 1}, {'item': '1900-01-01 01:00:05', 'frequency': 1}, {'item': '\
1900-01-01 01:00:10', 'frequency': 1}, {'item': '1900-01-01 01:00:15', 'frequency': 3}]
        >>> dm = DateMethods(pd.Series([None, None, None]))
        >>> dm.frequency_distribution()
        []

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the frequency distribution of each element in the data.
        """
        self.data_type = ResultTypes.DISTRIBUTION_INT.value
        # check data
        if self.__empty:
            return []
        # compute count of elements
        self.__freq_dist = getattr(self, '__freq_dist', self.data.value_counts(sort=False))
        return [{'item': str(element), 'frequency': int(frequency)} for element, frequency in self.__freq_dist.items()]

    def frequency_distribution_percent(self) -> List[Dict[str, float]]:
        """
        Computes the frequency distribution of the values in the data, getting the percentage of ocurrence of each
         unique element.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-23 00:00:00", "2022-03"\
        "-23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime='%Y-%m-%d %H:%M:%S')
        >>> dm.frequency_distribution_percent()
        [{'item': '2022-03-20 00:00:00', 'frequency': 0.16667}, {'item': '2022-03-21 00:00:00', 'frequency': 0.16667}, \
{'item': '2022-03-23 00:00:00', 'frequency': 0.33333}, {'item': '2022-03-24 00:00:00', 'frequency': 0.16667}, \
{'item': '2022-03-25 00:00:00', 'frequency': 0.16667}]
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-21", "2022-03-23", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime='%Y-%m-%d')
        >>> dm.frequency_distribution_percent()
        [{'item': '2022-03-20 00:00:00', 'frequency': 0.16667}, {'item': '2022-03-21 00:00:00', 'frequency': 0.16667},\
 {'item': '2022-03-23 00:00:00', 'frequency': 0.33333}, {'item': '2022-03-24 00:00:00', 'frequency': 0.16667}, {'item':\
 '2022-03-25 00:00:00', 'frequency': 0.16667}]
        >>> dm = DateMethods(pd.Series(["01:00:00", "01:00:05", "01:00:10", "01:00:15", "01:00:15", "01:00:15"], \
        name='timestamp'), strftime='%H:%M:%S')
        >>> dm.frequency_distribution_percent()
        [{'item': '1900-01-01 01:00:00', 'frequency': 0.16667}, {'item': '1900-01-01 01:00:05', 'frequency': 0.16667},\
 {'item': '1900-01-01 01:00:10', 'frequency': 0.16667}, {'item': '1900-01-01 01:00:15', 'frequency': 0.5}]
        >>> dm = DateMethods(pd.Series([None, None, None]))
        >>> dm.frequency_distribution_percent()
        []

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the normalized frequency distribution of each element in the data.
        """
        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value
        # check data
        if self.__empty:
            return []
        # compute count of elements
        self.__freq_dist = getattr(self, '__freq_dist', self.data.value_counts(sort=False))
        return [{
            'item': str(element), 'frequency': float(round(frequency/self.n_rows, 5))
        } for element, frequency in self.__freq_dist.items()]

    def mean(self) -> str:
        """
        Gets the mean of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.mean()
        '2022-03-22 12:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", \
        "2022-03-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.mean()
        '2022-03-22 08:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.mean()
        '1900-01-01 01:00:20'
        >>> dm = DateMethods(pd.Series([None, None, None]))
        >>> dm.mean()
        'null'
        >>> dm = DateMethods(pd.Series(["None", "None", "None"]))
        >>> dm.mean()
        'null'

        Returns
        -------
        _: str
            Mean value obtained from the given data in string format or `'null'` if there are no data.
        """
        self.data_type = ResultTypes.DATE.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # compute mean
        return str(self.data.mean())

    def median(self) -> str:
        """
        Computes the median of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.median()
        '2022-03-22 12:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.median()
        '2022-03-22 12:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.median()
        '1900-01-01 01:00:20'
        >>> dm = DateMethods(pd.Series([None, None, None]), strftime=r'%H:%M:%S')
        >>> dm.median()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None']), strftime=r'%H:%M:%S')
        >>> dm.median()
        'null'

        Returns
        -------
        _: str
            Median value obtained from the given data in string format.
        """
        self.data_type = ResultTypes.DATE.value
        # check parameters and data
        if self.__empty:
            return json.dumps(None)
        # compute median
        return str(self.data.median())

    def mode(self) -> str:
        """
        Obtains the most frequent element in the data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.mode()
        '2022-03-20 00:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.mode()
        '2022-03-20 00:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.mode()
        '1900-01-01 01:00:05'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.mode()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.mode()
        'null'

        Returns
        -------
        _: str
            The most frequent element of the given data as string.
        """
        # check data
        self.data_type = ResultTypes.DATE.value
        if self.__empty:
            return json.dumps(None)
        # get most frequent element
        self.__freq_dist = getattr(self, '__freq_dist', self.data.value_counts(sort=False))
        return str(self.__freq_dist.index[self.__freq_dist.argmax()])

    def mode_frequency(self) -> str:
        """
        Gets the frequency of the most frequent element in the data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.mode_frequency()
        '1'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.mode_frequency()
        '2'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.mode_frequency()
        '2'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.mode_frequency()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.mode_frequency()
        'null'

        Returns
        -------
        _: str
            The frequency of the most frequent element in the data.
        """
        # check data
        self.data_type = ResultTypes.INT.value
        if self.__empty:
            return json.dumps(None)
        # get most frequent element
        self.__freq_dist = getattr(self, '__freq_dist', self.data.value_counts(sort=False))
        return str(self.__freq_dist.max())

    def mode_frequency_percent(self) -> str:
        """
        Gets the percentage of occurrence of the most frequent element in the data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.mode_frequency_percent()
        '0.16667'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.mode_frequency_percent()
        '0.33333'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.mode_frequency_percent()
        '0.33333'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.mode_frequency_percent()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.mode_frequency_percent()
        'null'

        Returns
        -------
        _: str
            Percentage of occurrence of the most frequent element in the data.
        """
        # check data
        self.data_type = ResultTypes.FLOAT.value
        if self.__empty:
            return json.dumps(None)
        # get most frequent element
        self.__freq_dist = getattr(self, '__freq_dist', self.data.value_counts(sort=False))
        return str(round(self.__freq_dist.max()/self.n_rows, 5))

    def min(self) -> str:
        """
        Gets the minimum value of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.min()
        '2022-03-20 00:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.min()
        '2022-03-20 00:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.min()
        '1900-01-01 01:00:05'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.min()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.min()
        'null'

        Returns
        -------
        _: str
            Minimum value of the given data as a string.
        """
        self.data_type = ResultTypes.DATE.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # compute minimum
        self.__min = getattr(self, '__min', self.data.min())
        return str(self.__min)

    def max(self) -> str:
        """
        Gets the maximum value of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.max()
        '2022-03-25 00:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.max()
        '2022-03-25 00:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.max()
        '1900-01-01 01:00:40'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.max()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.max()
        'null'

        Returns
        -------
        _: str
            Maximum value of the given data as string.
        """
        self.data_type = ResultTypes.DATE.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # compute maximum
        self.__max = getattr(self, '__max', self.data.max())
        return str(self.__max)

    def range(self) -> str:
        """
        Computes the range of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.range()
        '5 days 00:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.range()
        '5 days 00:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.range()
        '0 days 00:00:35'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.range()
        'null'
        >>> dm = DateMethods(pd.Series(['None', None, None], name='timestamp'))
        >>> dm.range()
        'null'

        Returns
        -------
        _: str
            Range value of the given data as string.
        """
        self.data_type = ResultTypes.TIMEDELTA.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # check if computed previously
        self.__min = getattr(self, '__min', self.data.min())
        self.__max = getattr(self, '__max', self.data.max())
        # compute range
        return str(self.__max - self.__min)

    def fifth_percentile(self) -> str:
        """
        This method returns the fifth percentile of `self.data`.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.fifth_percentile()
        '2022-03-20 06:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-21", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.fifth_percentile()
        '2022-03-20 06:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.fifth_percentile()
        '1900-01-01 01:00:05'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.fifth_percentile()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.fifth_percentile()
        'null'

        Returns
        -------
        _: str
            Fifth value of the given data as string.
        """
        self.data_type = ResultTypes.DATE.value
        # check parameters and data
        if self.__empty:
            return json.dumps(None)
        # compute
        return str(self.data.quantile(q=0.05))

    def first_quartile(self) -> str:
        """
        Obtains the first quartile of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03"\
        "-23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.first_quartile()
        '2022-03-21 06:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.first_quartile()
        '2022-03-20 12:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.first_quartile()
        '1900-01-01 01:00:08.750000128'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.first_quartile()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.first_quartile()
        'null'

        Returns
        -------
        _: str
            First quartile of the given data as a string.
        """
        self.data_type = ResultTypes.DATE.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # compute first percentile
        self.__q1 = getattr(self, '__q1', self.data.quantile(q=0.25))
        return str(self.__q1)

    def third_quartile(self) -> str:
        """
        Obtains the third quartile of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.third_quartile()
        '2022-03-23 18:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.third_quartile()
        '2022-03-23 18:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.third_quartile()
        '1900-01-01 01:00:27.500000'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.third_quartile()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.third_quartile()
        'null'

        Returns
        -------
        _: str
            Third quartile of the given data as a string.
        """
        self.data_type = ResultTypes.DATE.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # compute
        self.__q3 = getattr(self, '__q3', self.data.quantile(q=0.75))
        return str(self.__q3)

    def ninety_fifth_percentile(self) -> str:
        """
        Obtains the 95th-percentile of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.ninety_fifth_percentile()
        '2022-03-24 18:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-21", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.ninety_fifth_percentile()
        '2022-03-24 18:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.ninety_fifth_percentile()
        '1900-01-01 01:00:37.500000'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.ninety_fifth_percentile()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', None], name='timestamp'))
        >>> dm.ninety_fifth_percentile()
        'null'

        Returns
        -------
        _: str
            95th-percentile of the given data as string.
        """
        self.data_type = ResultTypes.DATE.value
        # check parameters and data
        if self.__empty:
            return json.dumps(None)
        # compute
        return str(self.data.quantile(q=0.95))

    def iqr(self) -> str:
        """
        Obtains the interquartile range of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.iqr()
        '2 days 12:00:00'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.iqr()
        '3 days 06:00:00'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.iqr()
        '0 days 00:00:18.749999872'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.iqr()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.iqr()
        'null'

        Returns
        -------
        _: :obj:`pandas.Timedelta` or None
            Interquartile range (iqr) of the given data.
        """
        self.data_type = ResultTypes.TIMEDELTA.value
        # check data
        if self.__empty:
            return json.dumps(None)
        # compute
        self.__q1 = getattr(self, '__q1', self.data.quantile(q=0.25))
        self.__q3 = getattr(self, '__q3', self.data.quantile(q=0.75))
        # compute range
        return str(self.__q3 - self.__q1)

    def std(self) -> str:
        """
        Computes the standard deviation of the given data.

        Examples
        --------
        >>> dm = DateMethods(pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-"\
        "23 00:00:00", "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp'), strftime=r'%Y-%m-%d %H:%M:%S')
        >>> dm.std()
        '1 days 20:53:59.599108634'
        >>> dm = DateMethods(pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03"\
        "-25"], name='timestamp'), strftime=r'%Y-%m-%d')
        >>> dm.std()
        '2 days 01:34:27.072593237'
        >>> dm = DateMethods(pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], \
        name='timestamp'), strftime=r'%H:%M:%S')
        >>> dm.std()
        '0 days 00:00:13.784048752'
        >>> dm = DateMethods(pd.Series([None, None, None], name='timestamp'))
        >>> dm.std()
        'null'
        >>> dm = DateMethods(pd.Series(['None', 'None', 'None'], name='timestamp'))
        >>> dm.std()
        'null'

        Returns
        -------
        _: :obj:`pandas.Timedelta` or None
            Standard deviation (std) of the given data.
        """
        self.data_type = ResultTypes.TIMEDELTA.value
        # check data and parameters
        if self.__empty:
            return json.dumps(None)
        # get std
        return str(self.data.std())
