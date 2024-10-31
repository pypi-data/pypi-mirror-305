# kpi_library/date/mode_frequency.py
import json
import pandas as pd
from typing import Optional

from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class DateModeFrequency(MetricModel):
    """
    This metric computes the frequency of the most frequent element of a time column.

    Example
    -------
    >>> dm = DateModeFrequency()
    >>> data = pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-22 00:00:00", "2022-03-23 00:00:00", \
    "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp')
    >>> dm.run(data, date_format=r'%Y-%m-%d %H:%M:%S')
    1
    >>> data = pd.Series(["2022-03-20", "2022-03-20", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03-25"])
    >>> dm.run(data, date_format=r'%Y-%m-%d')
    2
    >>> dm.to_dqv(data, date_format=r'%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'date.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParamet\
ers': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': '2'}]
    >>> dm.to_dqv(data, date_format="-1")
    [{'dqv_isMeasurementOf': 'date.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParamet\
ers': [{'parameter_name': 'date_format', 'value': '"-1"'}], 'dqv_value': 'null'}]
    >>> data = pd.Series(["01:00:05", "01:00:05", "01:00:20", "01:00:20", "01:00:30", "01:00:40"], name='timestamp')
    >>> dm.run(data, date_format='%H:%M:%S')
    2
    >>> dm.run(pd.Series([None, None, None]))
    >>> dm.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'date.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParamet\
ers': [{'parameter_name': 'date_format', 'value': 'null'}], 'dqv_value': 'null'}]
    >>> dm.to_dqv(pd.Series(["None", "None", "None"]))
    [{'dqv_isMeasurementOf': 'date.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParamet\
ers': [{'parameter_name': 'date_format', 'value': 'null'}], 'dqv_value': 'null'}]
    >>> dm.to_dqv(pd.Series([1, 1, 1]))
    [{'dqv_isMeasurementOf': 'date.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParameter\
s': [{'parameter_name': 'date_format', 'value': 'null'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(DateModeFrequency, self).__init__(
            identifier='date.mode_frequency',
            keyword='DateModeFrequency',
            title='Frequency of the most frequent element',
            definition='Frequency of the most frequent element of the time data.',
            expected_data_type=str(ResultTypes.INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), default_value=None,
                           possible_values=None, description='The format to parse the dates.')]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {'date_format': kwargs.get('date_format', None)}
        try:
            result = self.run(data, **kwargs)
        except (EmptyDatasetError, DataTypeError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': '',
                'rdf_datatype': 'Error',
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(params),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': '' if data.name is None else data.name,
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(params),
            'dqv_value': 'null' if result is None else str(result)
        }]

    def run(self, data: pd.Series, **kwargs) -> Optional[int]:
        """
        This method returns the frequency of the most frequent element of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Dictionary containing the time format (`date_time`).

        Returns
        -------
        _: int, optional.
            Frequency of the most frequent element of the data.
        """
        srs = self._check_date_data(data, kwargs.get('date_format', None)).dropna()
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        distribution = srs.value_counts(sort=False, dropna=False)
        return int(distribution.max())
