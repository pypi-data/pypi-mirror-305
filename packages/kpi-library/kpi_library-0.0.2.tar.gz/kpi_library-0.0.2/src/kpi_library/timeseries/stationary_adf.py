# kpi_library/timeseries/stationary_adf.py
import json
import pandas as pd
from statsmodels.tsa.stattools import adfuller

from typing import Optional, Tuple, Any
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError, DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesStationaryAdf(MetricModel):
    """
    This metric checks whether the time series is stationary or not, using the Augmented Dickey-Fuller unit root test.

    Example
    -------
    >>> c = TimeseriesStationaryAdf()
    >>> ts = pd.DataFrame({'timestamp': ['6/1/2018 01:00', '6/1/2018 02:00', '6/1/2018 03:00', '6/1/2018 04:00', \
    '6/1/2018 05:00'], 'data': [0.626,0.256,0.385,1.053, 0.954]})
    >>> c.run(ts, feature_one='timestamp', feature_two='data', date_format='%m/%d/%Y %H:%M')
    False
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='data', date_format='%m/%d/%Y %H:%M')
    [{'dqv_isMeasurementOf': 'timeseries.stationary_adf', 'dqv_computedOn': 'timestamp, data', 'rdf_datatype': 'Boolean\
', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y %H:%M"'}, {'parameter_name': 'alpha', \
'value': '0.05'}], 'dqv_value': 'false'}]
    >>> c.run(ts, feature_one='timestamp', feature_two='data', date_format='-1')
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='data', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.stationary_adf', 'dqv_computedOn': 'timestamp, data', 'rdf_datatype': 'Boolean\
', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}, {'parameter_name': 'alpha', 'value': '0.\
05'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.stationary_adf', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'alpha\
', 'value': '0.05'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='Date', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.stationary_adf', 'dqv_computedOn': 'None, Date', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'alpha\
', 'value': '0.05'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.stationary_adf', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'alpha\
', 'value': '0.05'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': ['6/1/2018 01:00', '6/1/2018 02:00', '6/1/2018 03:00', '6/1/2018 04:00', \
    '6/1/2018 05:00'], 'data': ['0.626', '0.256', '0.385', '1.053', '0.954']})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='data', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.stationary_adf', 'dqv_computedOn': 'timestamp, data', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'alpha\
', 'value': '0.05'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesStationaryAdf, self).__init__(
            identifier='timeseries.stationary_adf',
            keyword='TimeseriesStationaryAdf',
            title='Stationary',
            definition='Testing if the time series is stationary by using the Augmented Dickey-Fuller unit root test.',
            expected_data_type=str(ResultTypes.BOOL.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.'),
            ParameterModel(
                name='alpha', data_type=str(ResultTypes.FLOAT.value), possible_values=None, default_value='0.05',
                description="Threshold to establish whether the time-series is stationary or not.")
        ]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # get parameters
        param = {'date_format': kwargs.get('date_format', None), 'alpha': kwargs.get('alpha', 0.05)}
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

    def run(self, data: pd.DataFrame, **kwargs) -> Optional[bool]:
        """
        This method checks if the time series is stationary by using the Augmented Dickey-Fuller unit root test.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that contain the following information:
                feature_one: str
                    Name of the time column, i.e., the index of the time series.
                feature_two: str
                    Name of the numeric column, i.e., data of the time series.
                date_format: str, optional
                    String specifying the time column format.
                alpha: float, optional. Default, 0.05
                    Threshold to establish whether the time series is stationary or not.

        Returns
        -------
        _: :obj:`bool`, optional
            Whether the time series is stationary or not.
        """
        # check correct parameter feature_one and feature_two, and get time series
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # if no correct data
        if ts.empty:
            return None
        # check parameter
        alpha = self._check_float_parameter(parameter=kwargs.get('alpha', 0.05), parameter_name='alpha', ge=0, le=1)
        # get ADF test statistics
        df_test: Tuple[Any] = adfuller(ts)
        adf_ = df_test[0]
        p_value = df_test[1]
        critical_value = df_test[4]['5%']
        # check if the time-series is stationary
        if(p_value < alpha) and (adf_ < critical_value):
            return True
        else:
            return False
