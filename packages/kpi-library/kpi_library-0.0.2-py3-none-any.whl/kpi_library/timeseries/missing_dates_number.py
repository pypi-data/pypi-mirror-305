# kpi_library/timeseries/missing_dates_number.py
import json
import pandas as pd

from datetime import timedelta
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TimeseriesMissingDatesNumber(MetricModel):
    """
    This metric computes the number of gaps in the measurements of the time series.

    Example
    -------
    >>> c = TimeseriesMissingDatesNumber()
    >>> ts = pd.DataFrame(\
    {'timestamp': ['6/1/2018', '6/2/2018', '6/3/2018', '6/4/2018', '6/5/2018'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    0
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    0
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.missing_dates_number', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': \
'Integer', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': '0'}]
    >>> ts = pd.DataFrame(\
    {'timestamp': ['2018-05-01', '2018-05-02', '2018-05-03', '2018-15-04', '2018-05-05'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    1
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.missing_dates_number', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Integer', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], \
'dqv_value': '1'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.missing_dates_number', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.missing_dates_number', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.missing_dates_number', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesMissingDatesNumber, self).__init__(
            identifier='timeseries.missing_dates_number',
            keyword='TimeseriesMissingDatesNumber',
            title='Missing measurements',
            definition='Number of gaps in the measurements.',
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

    def run(self, data: pd.DataFrame, **kwargs) -> int:
        """
        This method analyzes the time series index and returns the number of gaps in the measurements of the time
        series.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that may contain the name of the date column that must be processed (feature_one) and the time format
            (date_format).

        Returns
        -------
        _: int
            Number of gaps.
        """
        # check correct parameter feature_one and feature_two
        date_feature = kwargs.get('feature_one', None)
        self._check_bi_data(data=data, feature_one=date_feature, feature_two=kwargs.get('feature_two', None))
        # transform dates into time format
        date_format = kwargs.get('date_format', None)
        index = self._check_date_data(data=data[date_feature], date_format=date_format).dropna()
        # check again emptiness
        if index.empty:
            return 0
        # calculate the discrete difference between the adjacent values and get the median as inferred frequency
        diff: pd.Series = index.diff().dropna()
        med: timedelta = diff.median(skipna=True)
        # find gaps
        return int((diff > med * 1.5).sum())
