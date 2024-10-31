# kpi_library/timeseries/tendencyLine.py
import json
import numpy as np
import pandas as pd

from typing import List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError, DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesTendencyLine(MetricModel):
    """
    This metric computes the tendency of the time series and visualizes it using a line.

    Example
    -------
    >>> c = TimeseriesTendencyLine()
    >>> ts = pd.DataFrame({'timestamp':['6/1/2018', '7/1/2018', '8/1/2018', '6/1/2019', '7/1/2019', '8/1/2019'], \
        'num': [0.626,0.256,0.385,1.053, 0.954, 0.985]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    [{'x_axis': '2018-06-01 00:00:00', 'y_axis': 0.38433333333333325}, {'x_axis': '2018-07-01 00:00:00', 'y_axis': 0.5\
145333333333333}, {'x_axis': '2018-08-01 00:00:00', 'y_axis': 0.6447333333333332}, {'x_axis': '2019-06-01 00:00:00', '\
y_axis': 0.7749333333333333}, {'x_axis': '2019-07-01 00:00:00', 'y_axis': 0.9051333333333331}, {'x_axis': '2019-08-01 \
00:00:00', 'y_axis': 1.0353333333333332}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    [{'dqv_isMeasurementOf': 'timeseries.tendency_line', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<Map<\
String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y"'}], 'dqv_value': \
'[{"x_axis": "2018-06-01 00:00:00", "y_axis": 0.38433333333333325}, {"x_axis": "2018-07-01 00:00:00", "y_axis": 0.5\
145333333333333}, {"x_axis": "2018-08-01 00:00:00", "y_axis": 0.6447333333333332}, {"x_axis": "2019-06-01 00:00:00", "\
y_axis": 0.7749333333333333}, {"x_axis": "2019-07-01 00:00:00", "y_axis": 0.9051333333333331}, {"x_axis": "2019-08-01 \
00:00:00", "y_axis": 1.0353333333333332}]'}]
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    []
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.tendency_line', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<Map<\
String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': '[]'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.tendency_line', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype': 'Error', \
'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.tendency_line', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.tendency_line', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesTendencyLine, self).__init__(
            identifier='timeseries.tendency_line',
            keyword='TimeseriesTendencyLine',
            title='Tendency line graph',
            definition='Points to visualize the tendency of the time series',
            expected_data_type=str(ResultTypes.PLOT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.')]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # get parameters
        param = {'date_format': kwargs.get('date_format', None)}
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        # run method
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two, date_format=param['date_format'])
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError, DataTypeIndexError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': f"{feature_one}, {feature_two}",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=param),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': f"{feature_one}, {feature_two}",
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=param),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.DataFrame, **kwargs) -> List[Dict[str, Union[str, int, float]]]:
        """
        This method computes the tendency of the time series and visualizes it using a line.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that may contain the name of the date column that must be processed (feature_one) and the time format
            (date_format).

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the points to visualize the tendency of the timeseries into a line graph.
        """
        # check correct parameter feature_one and feature_two
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # if no correct data
        if ts.empty:
            return []
        # compute the trend line which fits better the points in ts, using the square polynomial condition
        x: List[int] = list(range(ts.size))
        z = np.polyfit(x, ts.values, 1)
        y = np.poly1d(z)(x)
        # turn the tendency line into a list of dictionaries which contain each point of this line
        return [{'x_axis': str(index), 'y_axis': float(val)} for index, val in zip(ts.index, y)]
