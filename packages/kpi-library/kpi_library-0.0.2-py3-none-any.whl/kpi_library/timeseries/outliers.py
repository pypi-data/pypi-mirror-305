# kpi_library/timeseries/outliers.py
import json
import pandas as pd

from typing import Optional
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..errors import DataTypeIndexError
from ..result_types import ResultTypes


class TimeseriesOutliers(MetricModel):
    """
    This metric computes the number of outliers, using the interquartile range method, in the time series.

    Example
    -------
    >>> c = TimeseriesOutliers()
    >>> ts = pd.DataFrame(\
    {'timestamp': ['6/1/2018', '6/2/2018', '6/3/2018', '6/4/2018', '6/5/2018'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    0
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.outliers', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'Integer', '\
ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame(\
    {'timestamp': ['2018-05-01', '2018-05-02', '2018-05-03', '2018-05-04', '2018-05-05'], 'num': [0,1,2,1000,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    1
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.outliers', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'Integer', '\
ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': '1'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.outliers', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.outliers', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.outliers', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesOutliers, self).__init__(
            identifier='timeseries.outliers',
            keyword='TimeseriesOutliers',
            title='Outliers',
            definition='Number of outliers in the timeseries.',
            expected_data_type=str(ResultTypes.INT.value),
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

    def run(self, data: pd.DataFrame, **kwargs) -> Optional[int]:
        """
        This metric uses the interquartile range (IQR) method to find possible outliers. The interquartile range is a
        measure of statistical dispersion, which shows the spread of the data. It is defined as the difference between
        the 75th and 25th percentiles of the data. The samples are classified as outliers because they fall outside
        the range.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that may contain the name of the date column that must be processed (feature_one) and the time format
            (date_format).

        Returns
        -------
        _: int, optional.
            Number of outliers in the time series.
        """
        # check correct parameter feature_one and feature_two
        ts = self._check_timeseries(data=data,
                                    feature_one=kwargs.get('feature_one', None),
                                    feature_two=kwargs.get('feature_two', None),
                                    date_format=kwargs.get('date_format', None))
        # if no correct data
        if ts.empty:
            return None
        # get the quartiles
        stat: pd.Series = ts.quantile([.25, .75])
        # iqr equal to Q3 - Q1, upper fence = Q3 + (1.5*IQR), lower fence = Q1 - (1.5*IQR)
        iqr: float = stat.loc[.75] - stat.loc[.25]
        upper: float = stat.loc[.75] + 1.5 * iqr
        lower: float = stat.loc[.25] - 1.5 * iqr
        # Use the fences to highlight any outliers (all values that fall outside the fences)
        return int(((ts > upper) | (ts < lower)).sum())
