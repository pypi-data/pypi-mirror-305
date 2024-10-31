# kpi_library/date/histogram_percent.py
import json
import pandas as pd
from typing import List, Dict, Union

from .date_histogram import date_histogram
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class DateHistogramPercent(MetricModel):
    """
    This metric extracts from the given data the necessary information to visualize them in a histogram.

    Note
    ----
    The histogram requires the number of bins to be visualized. If not specified, ten bins will be displayed.
    Additionally, it is possible to specify the format of the dates, but, if it is not given, the metric infers it.

    Examples
    --------
    >>> data = pd.Series(["2022-20-03 00:00:00", "2022-21-03 00:00:00", "2022-22-03 00:00:00", "2022-23-03 00:00:00", \
    "2022-24-03 00:00:00", "2022-25-03 00:00:00"], name='timestamp')
    >>> dm = DateHistogramPercent()
    >>> dm.run(data, date_format=r'%Y-%d-%m %H:%M:%S', num_bins=3)
    [{'limits': '[2022-03-20 00:00:00, 2022-03-21 16:00:00)', 'frequency': 33.33}, {'limits': '[2022-03-21 16:00:00, \
2022-03-23 08:00:00)', 'frequency': 33.33}, {'limits': '[2022-03-23 08:00:00, 2022-03-25 00:00:00]', 'frequency': 33.33\
}]
    >>> dm.run(data, date_format='-1', num_bins=3)
    []
    >>> data = pd.Series(["2022-20-03", "2022-21-03", "2022-22-03", "2022-23-03", "2022-24-03", "2022-25-03"])
    >>> dm.run(data, date_format='%Y-%d-%m', num_bins=3)
    [{'limits': '[2022-03-20 00:00:00, 2022-03-21 16:00:00)', 'frequency': 33.33}, \
{'limits': '[2022-03-21 16:00:00, 2022-03-23 08:00:00)', 'frequency': 33.33}, \
{'limits': '[2022-03-23 08:00:00, 2022-03-25 00:00:00]', 'frequency': 33.33}]
    >>> dm.to_dqv(data, date_format='%Y-%d-%m', num_bins=3)
    [{'dqv_isMeasurementOf': 'date.histogram_percent', 'dqv_computedOn': '', 'rdf_datatype': 'List<Map<String,String>>'\
, 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%d-%m"'}, {'parameter_name': 'num_bins', 'valu\
e': '3'}], 'dqv_value': '[{"limits": "[2022-03-20 00:00:00, 2022-03-21 16:00:00)", "frequency": 33.33}, {"limits": "[20\
22-03-21 16:00:00, 2022-03-23 08:00:00)", "frequency": 33.33}, {"limits": "[2022-03-23 08:00:00, 2022-03-25 00:00:00]",\
 "frequency": 33.33}]'}]
    >>> data = pd.Series(["01:00:00", "01:00:05", "01:00:10", "01:00:15", "01:00:20", "01:00:25", "01:00:30"])
    >>> dm.run(data, date_format='%H:%M:%S', num_bins=3)
    [{'limits': '[1900-01-01 01:00:00, 1900-01-01 01:00:10)', 'frequency': 28.57}, {'limits': '[1900-01-01 01:00:10, 19\
00-01-01 01:00:20)', 'frequency': 28.57}, {'limits': '[1900-01-01 01:00:20, 1900-01-01 01:00:30]', 'frequency': 42.86}]
    >>> dm.run(pd.Series([None, None, None]), num_bins=3)
    []
    >>> dm.to_dqv(pd.Series([None, None, None]), num_bins=3)
    [{'dqv_isMeasurementOf': 'date.histogram_percent', 'dqv_computedOn': '', 'rdf_datatype': 'List<Map<String,String>>'\
, 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': 'null'}, {'parameter_name': 'num_bins', 'value': '3\
'}], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(DateHistogramPercent, self).__init__(
            identifier='date.histogram_percent',
            keyword='DateHistogramPercent',
            title='Histogram',
            definition='Necessary information to display a histogram of the given data.',
            expected_data_type=str(ResultTypes.HISTOGRAM.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.'),
            ParameterModel(name='num_bins', data_type=str(ResultTypes.INT.value), description='Number of bins.',
                           possible_values=None, default_value='10')]

    def to_dqv(self, data: pd.Series, **kwargs):
        """"""
        params = {'date_format': kwargs.get('date_format', None), 'num_bins': kwargs.get('num_bins', '10')}
        try:
            # get result
            result = self.run(data, **params)
        except (IncorrectParameterError, DataTypeError, EmptyDatasetError):
            # error
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
                'dqv_value': None
            }]
        # no error
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': '' if data.name is None else data.name,
            'rdf_datatype': ResultTypes.HISTOGRAM.value,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.Series, **kwargs) -> List[Dict[str, Union[str, float]]]:
        """
        This method computes the necessary information to visualize the given data in a histogram. The value of the
        y-axis will show the percentage of values that fit in a bin.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Data to be processed.
        kwargs: :obj:`dict`
            Dictionary containing the number of bins that must be displayed (`num_bins`) and the format the dates follow
            (`date_format`). The default value of the number of bins to display is 10 in the case the number is not
            specified.

        Raises
        ------
        IncorrectParameterError
            If num_bins is less than 2, or it is not a number.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries, where `limits` is the boundaries of the bin and `frequency` is the percentages of
            elements that fit in it.
        """
        # check data
        num_rows = data.shape[0]
        srs = self._check_date_data(data, date_format=kwargs.get('date_format', None)).dropna(inplace=False)
        # check parameter (num_bins)
        num_bins = self._check_int_parameter(parameter=kwargs.get('num_bins', 10), parameter_name='num_bins', ge=2)
        # check if data is empty
        if srs.empty:
            return []
        # compute bins, frequency (histogram information)
        x_bins, y_freq = date_histogram(srs, num_bins=num_bins)
        # collect bin information into histogram object
        limits = zip(x_bins[:-2], x_bins[1:-1])
        hist = [{
            'limits': f'[{bin_i[0]}, {bin_i[1]})',
            'frequency': float(round((freq/num_rows)*100, 2))
        } for bin_i, freq in zip(limits, y_freq)]
        hist.append({
            'limits': f'[{x_bins[-2]}, {x_bins[-1]}]', 'frequency': float(round((y_freq[-1]/num_rows)*100, 2))
        })
        # return the result
        return hist
