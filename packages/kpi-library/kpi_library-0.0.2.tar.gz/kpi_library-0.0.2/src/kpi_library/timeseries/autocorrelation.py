# kpi_library/timeseries/autocorrelation.py
import json
import pandas as pd
import statsmodels.api as sm

from typing import List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError, DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesAutocorrelation(MetricModel):
    """
    This metric computes the number of outliers, using the interquartile range method, in the time series.

    Example
    -------
    >>> c = TimeseriesAutocorrelation()
    >>> ts = pd.DataFrame({'timestamp': ['6/1/2018 01:00', '6/1/2018 02:00', '6/1/2018 03:00', '6/1/2018 04:00', \
        '6/1/2018 05:00'], 'num': [0.626,0.256,0.564,0.183,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y %H:%M')
    [{'x_axis': 0, 'y_axis': 1.0}, {'x_axis': 1, 'y_axis': -0.12001210710355731}, {'x_axis': 2, 'y_axis': -0.04907342\
613001419}, {'x_axis': 3, 'y_axis': -0.1937350208207345}, {'x_axis': 4, 'y_axis': -0.13717944594569403}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y %H:%M')
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<\
Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y %H:%M"'}, {'parame\
ter_name': 'fft', 'value': 'false'}], 'dqv_value': '[{"x_axis": 0, "y_axis": 1.0}, {"x_axis": 1, "y_axis": -0.1200121\
0710355731}, {"x_axis": 2, "y_axis": -0.04907342613001419}, {"x_axis": 3, "y_axis": -0.1937350208207345}, {"x_axis": \
4, "y_axis": -0.13717944594569403}]'}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y %H:%M', fft=True)
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<\
Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y %H:%M"'}, {'parame\
ter_name': 'fft', 'value': 'true'}], 'dqv_value': '[{"x_axis": 0, "y_axis": 1.0}, {"x_axis": 1, "y_axis": -0.12001210\
710355734}, {"x_axis": 2, "y_axis": -0.04907342613001416}, {"x_axis": 3, "y_axis": -0.19373502082073446}, {"x_axis": \
4, "y_axis": -0.13717944594569406}]'}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y %H:%M', fft="error")
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'Error\
', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y %H:%M"'}, {'parameter_name': 'fft', '\
value': '"error"'}], 'dqv_value': 'null'}]
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1', fft=False)
    []
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1', fft=False)
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<\
Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}, {'parameter_name': '\
fft', 'value': 'false'}], 'dqv_value': '[]'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype': 'Error\
', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'fft', 'value':\
 'false'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'fft',\
 'value': 'false'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.autocorrelation', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'fft',\
 'value': 'false'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesAutocorrelation, self).__init__(
            identifier='timeseries.autocorrelation',
            keyword='TimeseriesAutocorrelation',
            title='Autocorrelation Plot',
            definition='Points to visualize the autocorrelation plot of the time series.',
            expected_data_type=str(ResultTypes.PLOT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.'),
            ParameterModel(
                name='fft', data_type=str(ResultTypes.BOOL.value), possible_values=["false", "true"],
                default_value="false", description='Whether the autocorrelation function is computed by FFT or a simple'
                                                   ' and direct estimator of the autocovariance.')]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # get parameters
        params = {'date_format': kwargs.get('date_format', None), 'fft': kwargs.get('fft', False)}
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        # run method
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two, **params)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError, DataTypeIndexError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': f"{feature_one}, {feature_two}",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': f"{feature_one}, {feature_two}",
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.DataFrame, **kwargs) -> List[Dict[str, Union[str, int, float]]]:
        """
        This metric returns the necessary information to visualize the time series into an autocorrelation plot, i.e.,
        it returns a list of the graph points.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that contains the following information:
                feature_one: str
                    Name of the date column, the index.
                feature_two: str
                    Name of the numeric column, the data of the time series.
                date_format: str
                    The time format.
                fft: bool, optional. Default False.
                    Whether the autocorrelation function is computed by FFT or a simple and direct estimator of the
                    autocovariance.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the points to visualize the timeseries into a autocorrelation plot.
        """
        # check correct parameter feature_one and feature_two
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # check paramater
        fft = self._check_boolean_parameter(parameter=kwargs.get("fft", False), parameter_name='fft')
        # if no correct data
        if ts.empty:
            return []
        # return the list of points of the autocorrelation plot
        return [{
            'x_axis': index, 'y_axis': element
        } for index, element in enumerate(sm.tsa.acf(ts.dropna(inplace=False), fft=fft))]
