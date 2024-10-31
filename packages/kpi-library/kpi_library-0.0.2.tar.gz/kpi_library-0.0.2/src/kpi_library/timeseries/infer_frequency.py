# kpi_library/timeseries/infer_frequency.py
import json
import pandas as pd

from datetime import timedelta
from typing import Optional, Dict
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TimeseriesInferFrequency(MetricModel):
    """
    This metric infers the frequency with which the time series measurements are obtained.

    Example
    -------
    >>> c = TimeseriesInferFrequency()
    >>> ts = pd.DataFrame(\
    {'timestamp': ['6/1/2018', '6/2/2018', '6/3/2018', '6/4/2018', '6/5/2018'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%m/%d/%Y')
    {'years': 0, 'months': 0, 'days': 1, 'hours': 0, 'minutes': 0, 'seconds': 0}
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='-1')
    [{'dqv_isMeasurementOf': 'timeseries.infer_frequency', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype': 'Map<Str\
ing,Integer>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame(\
    {'timestamp': ['2018-05-01', '2018-05-02', '2018-05-03', '2018-15-04', '2018-05-05'], 'num': [0,1,2,3,4]})
    >>> c.run(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    {'years': 0, 'months': 0, 'days': 1, 'hours': 0, 'minutes': 0, 'seconds': 0}
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.infer_frequency', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Map<String,Integer>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], \
'dqv_value': '{"years": 0, "months": 0, "days": 1, "hours": 0, "minutes": 0, "seconds": 0}'}]
    >>> c.to_dqv(ts, feature_one='timestamp', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.infer_frequency', 'dqv_computedOn': 'timestamp, None', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(ts, feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.infer_frequency', 'dqv_computedOn': 'None, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    >>> ts = pd.DataFrame({'timestamp': [1,2,3,4,5], 'num': [0,1,2,3,4]})
    >>> c.to_dqv(ts, feature_one='timestamp', feature_two='num', date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'timeseries.infer_frequency', 'dqv_computedOn': 'timestamp, num', 'rdf_datatype\
': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(TimeseriesInferFrequency, self).__init__(
            identifier='timeseries.infer_frequency',
            keyword='TimeseriesInferFrequency',
            title='Frequency of measurement',
            definition='Inferred frequency with which the time series measurements are obtained.',
            expected_data_type=str(ResultTypes.INFER_FREQUENCY.value),
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

    def run(self, data: pd.DataFrame, **kwargs) -> Optional[Dict[str, int]]:
        """
        This method analyzes the time series index and infers a possible frequency.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that may contain the name of the date column that must be processed (feature_one) and the time format
            (date_format).

        Returns
        -------
        _: :obj:`dict`, optional
            Dictionary containing the frequency with which the measurements of the time series are obtained.
        """
        # check correct parameter feature_one and feature_two
        date_feature = kwargs.get('feature_one', None)
        self._check_bi_data(data=data, feature_one=date_feature, feature_two=kwargs.get('feature_two', None))
        # transform dates into time format
        date_format = kwargs.get('date_format', None)
        index = self._check_date_data(data=data[date_feature], date_format=date_format).dropna()
        # check again emptiness
        if index.empty:
            return None
        # calculate the discrete difference between the adjacent values and get the median as inferred frequency
        med: timedelta = index.diff().median(skipna=True)
        # return the result in a dictionary object
        res: Dict[str, int] = {'years': 0, 'months': 0, 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}
        if med in [timedelta(days=28), timedelta(days=29), timedelta(days=30), timedelta(days=31)]:
            res['months'] = 1
        elif med in [timedelta(days=365), timedelta(days=366)]:
            res['years'] = 1
        else:
            secs: int = med.seconds
            res['days'] = med.days
            # compute hours
            res['hours'] = int(secs / 3600)
            secs = secs % 3600
            # compute minutes
            res['minutes'] = int(secs / 60)
            secs = secs % 60
            # save seconds
            res['seconds'] = secs
        # return
        return res
