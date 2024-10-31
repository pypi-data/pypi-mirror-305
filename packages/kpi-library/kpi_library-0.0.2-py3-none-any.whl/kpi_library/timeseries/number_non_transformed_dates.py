# kpi_library/timeseries/number_non_transformed_dates.py
import json
import pandas as pd

from typing import Optional
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TimeseriesNumberNonTransformedDates(MetricModel):
    """
    This metric computes the number of values in the index of the time series that could not be transformed into the
    given or inferred date format.

    Example
    -------
    >>> c = TimeseriesNumberNonTransformedDates()
    >>> ts = pd.DataFrame(\
    {'timestamp': ['6/1/2018', '6/2/2018', '6/3/2018', '6/4/2018', '6/5/2018'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    0
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    5
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.number_non_transformed_dates', 'dqv_computedOn': 'timestamp, num', 'rdf_datat\
ype': 'Integer', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': '5'}]
    >>> ts = pd.DataFrame(\
    {'timestamp': ['2018-05-01', '2018-05-02', '2018-05-03', '2018-15-04', '2018-05-05'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    1
    >>> c.run(ts, feature_one='timestamp', feature_two='num')
    1
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.number_non_transformed_dates', 'dqv_computedOn': 'timestamp, None', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.number_non_transformed_dates', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.number_non_transformed_dates', 'dqv_computedOn': 'timestamp, num', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesNumberNonTransformedDates, self).__init__(
            identifier='timeseries.number_non_transformed_dates',
            keyword='TimeseriesNumberNonTransformedDates',
            title='Number of non-transformed dates',
            definition='Number of non-transformed dates.',
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
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError):
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

    def run(self, data: pd.DataFrame, **kwargs) -> Optional[float]:
        """
        This method returns the number of entries that could not be transformed into dates.

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
            Number of non-transformed dates.
        """
        # check correct parameter feature_one
        date_feature = kwargs.get('feature_one', None)
        self._check_bi_data(data=data, feature_one=date_feature, feature_two=kwargs.get('feature_two', None))
        # transform dates into time format
        date_format = kwargs.get('date_format', None)
        srs = self._check_date_data(data=data[date_feature], date_format=date_format)
        # compute number of null values
        return int(srs.isna().sum())
