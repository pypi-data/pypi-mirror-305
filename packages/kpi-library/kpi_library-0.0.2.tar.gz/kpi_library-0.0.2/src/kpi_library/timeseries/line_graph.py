# kpi_library/timeseries/lineGraph.py
import json
import pandas as pd

from typing import List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError, DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesLineGraph(MetricModel):
    """
    This metric computes the number of outliers, using the interquartile range method, in the time series.

    Example
    -------
    >>> c = TimeseriesLineGraph()
    >>> ts = pd.DataFrame({'timestamp': ['6/1/2018 01:00', '6/1/2018 02:00', '6/1/2018 03:00', '6/1/2018 04:00', '6/1/'\
    '2018 05:00'], 'num': [0.626,0.256,0.385,1.053, 0.954]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y %H:%M')
    [{'x_axis': '2018-06-01 01:00:00', 'y_axis': 0.626}, {'x_axis': '2018-06-01 02:00:00', 'y_axis': 0.256}, {'x_axis'\
: '2018-06-01 03:00:00', 'y_axis': 0.385}, {'x_axis': '2018-06-01 04:00:00', 'y_axis': 1.053}, {'x_axis': '2018-06-01 \
05:00:00', 'y_axis': 0.954}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y %H:%M')
    [{'dqv_isMeasurementOf': 'timeseries.line_graph', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<Map<Str\
ing,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y %H:%M"'}], 'dqv_value': \
'[{"x_axis": "2018-06-01 01:00:00", "y_axis": 0.626}, {"x_axis": "2018-06-01 02:00:00", "y_axis": 0.256}, {"x_axis"\
: "2018-06-01 03:00:00", "y_axis": 0.385}, {"x_axis": "2018-06-01 04:00:00", "y_axis": 1.053}, {"x_axis": "2018-06-01 \
05:00:00", "y_axis": 0.954}]'}]
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    []
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.line_graph', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<Map<St\
ring,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': '[]'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.line_graph', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.line_graph', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.line_graph', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesLineGraph, self).__init__(
            identifier='timeseries.line_graph',
            keyword='TimeseriesLineGraph',
            title='Line graph',
            definition='Points to visualize the time series in a line graph',
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
        This metric returns the necessary information to visualize the time series into a line graph, i.e., it returns a
        list of the graph points.

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
            List of dictionaries containing the points to visualize the timeseries into a line graph.
        """
        # check correct parameter feature_one and feature_two
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # if no correct data
        if ts.empty:
            return []
        # return the list of points of the line plot
        return [{'x_axis': str(date), 'y_axis': float(elem)} for date, elem in ts.items()]
