# kpi_library/timeseries/component_resid.py
import json
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

from typing import List, Dict
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..errors import DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesComponentResid(MetricModel):
    """
    This metric uses the seasonal decomposition with moving averages to study the components of the time series and
    returns the resid component.

    Example
    -------
    >>> c = TimeseriesComponentResid()
    >>> ts = pd.read_csv("../../resources/example.csv", usecols=['Date', 'Num1'])
    >>> c.run(ts, feature_one='Date', feature_two='Num1', date_format='%m/%d/%Y')
    [{'x_axis': '2000-02-07 00:00:00', 'y_axis': -0.004177083333333276}, {'x_axis': '2000-02-08 00:00:00', 'y_axis': \
-0.004177083333333276}, {'x_axis': '2000-02-09 00:00:00', 'y_axis': -0.004177083333333272}, {'x_axis': '2000-02-10 00\
:00:00', 'y_axis': -0.004177083333333276}, {'x_axis': '2000-02-11 00:00:00', 'y_axis': -0.004177083333333276}, {'x_ax\
is': '2000-02-12 00:00:00', 'y_axis': -0.004177083333333276}, {'x_axis': '2000-02-13 00:00:00', 'y_axis': -0.00417708\
3333333276}, {'x_axis': '2000-02-14 00:00:00', 'y_axis': -0.004177083333333276}, {'x_axis': '2000-02-15 00:00:00', 'y\
_axis': -0.004177083333333272}, {'x_axis': '2000-02-16 00:00:00', 'y_axis': -0.004177083333333276}, {'x_axis': '2000-\
02-17 00:00:00', 'y_axis': -0.004177083333333276}, {'x_axis': '2000-02-18 00:00:00', 'y_axis': -0.004177083333333276}]
    >>> c.run(ts, feature_one='Date', feature_two='Num1', date_format='-1')
    []
    >>> c.to_dqv(ts, feature_one='Date', feature_two='Num1', date_format='%m/%d/%Y')
    [{'dqv_isMeasurementOf': 'timeseries.component_resid', 'dqv_computedOn': 'Date, Num1', 'rdf_datatype': 'List<M\
ap<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y"'}, {'parameter_name\
': 'model', 'value': '"additive"'}, {'parameter_name': 'period', 'value': '12'}], 'dqv_value': '\
[{"x_axis": "2000-02-07 00:00:00", "y_axis": -0.004177083333333276}, {"x_axis": "2000-02-08 00:00:00", "y_axis": \
-0.004177083333333276}, {"x_axis": "2000-02-09 00:00:00", "y_axis": -0.004177083333333272}, {"x_axis": "2000-02-10 00\
:00:00", "y_axis": -0.004177083333333276}, {"x_axis": "2000-02-11 00:00:00", "y_axis": -0.004177083333333276}, {"x_ax\
is": "2000-02-12 00:00:00", "y_axis": -0.004177083333333276}, {"x_axis": "2000-02-13 00:00:00", "y_axis": -0.00417708\
3333333276}, {"x_axis": "2000-02-14 00:00:00", "y_axis": -0.004177083333333276}, {"x_axis": "2000-02-15 00:00:00", "y\
_axis": -0.004177083333333272}, {"x_axis": "2000-02-16 00:00:00", "y_axis": -0.004177083333333276}, {"x_axis": "2000-\
02-17 00:00:00", "y_axis": -0.004177083333333276}, {"x_axis": "2000-02-18 00:00:00", "y_axis": -0.004177083333333276}\
]'}]
    >>> c.to_dqv(ts, feature_one='Date', feature_two='Num1', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.component_resid', 'dqv_computedOn': 'Date, Num1', 'rdf_datatype': 'List<M\
ap<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}, {'parameter_name\
': 'model', 'value': '"additive"'}, {'parameter_name': 'period', 'value': '12'}], 'dqv_value': '[]'}]
    >>> c.to_dqv(ts, feature_one='Date', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.component_resid', 'dqv_computedOn': 'Date, None', 'rdf_datatype': 'Error', \
'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name\
': 'model', 'value': '"additive"'}, {'parameter_name': 'period', 'value': '12'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='Num1', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.component_resid', 'dqv_computedOn': 'None, Num1', 'rdf_datatype': 'Error', \
'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name\
': 'model', 'value': '"additive"'}, {'parameter_name': 'period', 'value': '12'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.component_resid', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'Error',\
 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name\
': 'model', 'value': '"additive"'}, {'parameter_name': 'period', 'value': '12'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': ['2002/05/01','2002/05/02','2002/05/03','2002/05/04','2002/05/05'], 'num': \
    ['0','1','2','3','4']})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.component_resid', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name\
': 'model', 'value': '"additive"'}, {'parameter_name': 'period', 'value': '12'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesComponentResid, self).__init__(
            identifier='timeseries.component_resid',
            keyword='TimeseriesComponentResid',
            title='Resid component',
            definition='Resid component of the time series using the seasonal decomposition.',
            expected_data_type=str(ResultTypes.PLOT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.'),
            ParameterModel(
                name='model', data_type=str(ResultTypes.STRING.value), default_value="additive",
                possible_values=["additive", "multiplicative"], description='Type of seasonal decomposition.'),
            ParameterModel(
                name='period', data_type=str(ResultTypes.INT.value), default_value='12',
                possible_values=None, description="Period of the series. It must be used if ts is not a pandas object o"
                                                  "r if the index does not have a regular frequency.")
        ]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # get parameters
        params = {
            'date_format': kwargs.get('date_format', None),
            'model': kwargs.get('model', 'additive'),
            'period': kwargs.get('period', 12)
        }
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        # run method
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two, **params)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError, DataTypeIndexError, ValueError):
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

    def run(self, data: pd.DataFrame, **kwargs) -> List[Dict[str, float]]:
        """
        This method returns the resid component of the time series using the seasonal decomposition with moving
        averages.

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
                model: {additive, multiplicative}, optional. Default 'additive'
                    Type of seasonal decomposition.
                period: int, optional. Default 12
                    Period of the series. It must be used if ts is not a pandas object or if the index does not have a
                    frequency.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            Resid component.
        """
        # check correct parameter feature_one and feature_two
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # if no correct data
        if ts.empty:
            return []
        # check parameters
        model = kwargs.get('model', 'additive')
        self._check_enum_parameter(parameter_name='model', parameter=model, values=['additive', 'multiplicative'])
        period = self._check_int_parameter(parameter=kwargs.get('period', 12), parameter_name='period', ge=1)
        # decompose the time series and return trend component
        resid = seasonal_decompose(ts, model=model, period=period).resid.dropna(inplace=False)
        return [{'x_axis': str(index), 'y_axis': float(value)} for index, value in resid.items()]
