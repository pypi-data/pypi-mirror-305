# kpi_library/timeseries/boxPlots.py
import json
import pandas as pd

from typing import List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError, DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesBoxPlots(MetricModel):
    """
    This metric returns the statistics to build box plots depending on the split factor of the time in the timeseries.

    Example
    -------
    >>> c = TimeseriesBoxPlots()
    >>> ts = pd.DataFrame({'timestamp':['6/1/2018', '7/1/2018', '8/1/2018', '6/1/2019', '7/1/2019', '8/1/2019'], \
    'num': [0.626,0.256,0.385,1.053, 0.954, -9.265]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    [{'x_axis': '2018', 'y_axis': {'min': 0.256, 'max': 0.626, 'first_quartile': 0.3205, 'median': 0.385, 'third_quart\
ile': 0.5055000000000001, 'outliers': []}}, {'x_axis': '2019', 'y_axis': {'min': -9.265, 'max': 1.053, 'first_quartile\
': -4.155500000000001, 'median': 0.954, 'third_quartile': 1.0034999999999998, 'outliers': []}}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y', split_factor='year')
    [{'dqv_isMeasurementOf': 'timeseries.box_plots', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<Map<Str\
ing,Serializable>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y"'}, {'parameter_nam\
e': 'split_factor', 'value': '"year"'}], 'dqv_value': '[{"x_axis": "2018", "y_axis": {"min": 0.256, "max": 0.626, "fi\
rst_quartile": 0.3205, "median": 0.385, "third_quartile": 0.5055000000000001, "outliers": []}}, {"x_axis": "2019", "y\
_axis": {"min": -9.265, "max": 1.053, "first_quartile": -4.155500000000001, "median": 0.954, "third_quartile": 1.0034\
999999999998, "outliers": []}}]'}]
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    []
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.box_plots', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'List<Map<Str\
ing,Serializable>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}, {'parameter_name': 's\
plit_factor', 'value': '"year"'}], 'dqv_value': '[]'}]
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y', split_factor='error')
    [{'dqv_isMeasurementOf': 'timeseries.box_plots', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'Error', 'ddq\
v_hasParameters': [{'parameter_name': 'date_format', 'value': '"%m/%d/%Y"'}, {'parameter_name': 'split_factor', 'valu\
e': '"error"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.box_plots', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'split_factor', 'va\
lue': '"year"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.box_plots', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'split\
_factor', 'value': '"year"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.box_plots', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}, {'parameter_name': 'split\
_factor', 'value': '"year"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesBoxPlots, self).__init__(
            identifier='timeseries.box_plots',
            keyword='TimeseriesBoxPlots',
            title='Box plots',
            definition='Statistics to build different box plots depending on the split factor of the time in the time '
                       'series',
            expected_data_type=str(ResultTypes.CAT_BOX_PLOT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.'),
            ParameterModel(name='split_factor', data_type=str(ResultTypes.STRING.value), default_value='year',
                           possible_values=['year', 'month', 'day'], description='Split factor which groups the time-s\
                           eries to build different box plots.')
        ]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # get parameters
        params = {'date_format': kwargs.get('date_format', None), 'split_factor': kwargs.get('split_factor', 'year')}
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
        This metric returns the statistics to build different box plots depending on the split factor of the time in the
        time series.

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
                split_factor: {'year', 'month', 'day'}, optional. Default 'year'.
                    Split factor which groups the time series (ts) to build different box plots.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the statistics to visualize each of the box plots.
        """
        # check correct parameter feature_one and feature_two
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # check parameter
        split_factor = kwargs.get('split_factor', 'year')
        self._check_enum_parameter(
            parameter_name='split_factor', parameter=split_factor, values=['year', 'month', 'day'])
        # if no correct data
        if ts.empty:
            return []
        # check the correct parameter (split_factor)
        if split_factor == 'year':
            splits = ts.index.year
        elif split_factor == 'month':
            splits = ts.index.month
        else:
            splits = ts.index.day
        # group the time series according to `splits`
        ts_groups = ts.groupby(by=splits)
        # get the necessary data to build a box plot of each group of the time-series
        res: List[Dict[str, Union[str, int, float]]] = []
        for split_date, elements in ts_groups:
            # statistics of the rows that are in the split factor elem
            stats = elements.describe()
            iqr = stats['75%'] - stats['25%']
            upper = stats['75%'] + 1.5 * iqr
            lower = stats['25%'] - 1.5 * iqr
            # possible outliers
            outliers = elements.loc[(elements.gt(upper)) | (elements.lt(lower))].to_list()

            res.append({'x_axis': str(split_date),
                        'y_axis': {
                            'min': stats.loc['min'],
                            'max': stats.loc['max'],
                            'first_quartile': stats.loc['25%'],
                            'median': stats.loc['50%'],
                            'third_quartile': stats.loc['75%'],
                            'outliers': outliers}})
        # return
        return res
