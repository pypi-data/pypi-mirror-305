# kpi_library/date/frequency_distribution.py
import json
import pandas as pd

from typing import List, Dict
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class DateFrequencyDistribution(MetricModel):
    """
    This metric gets the frequency distribution of the time data given as parameter.

    Note
    ----
    This metric lets to specify the format of the time data. If non is specified, the metric tries to infer the time
    format and all values that cannot be turned into this format are converted to null values.

    Example
    -------
    >>> dm = DateFrequencyDistribution()
    >>> data = pd.Series(["2022-03-20 00:00:00", "2022-03-21 00:00:00", "2022-03-23 00:00:00", "2022-03-23 00:00:00", \
    "2022-03-24 00:00:00", "2022-03-25 00:00:00"], name='timestamp')
    >>> dm.run(data, date_format='%Y-%m-%d %H:%M:%S')
    [{'item': '2022-03-20 00:00:00', 'frequency': 1}, {'item': '2022-03-21 00:00:00', 'frequency': 1}, {'item': '2022\
-03-23 00:00:00', 'frequency': 2}, {'item': '2022-03-24 00:00:00', 'frequency': 1}, {'item': '2022-03-25 00:00:00', '\
frequency': 1}]
    >>> dm.run(data, date_format='-1')
    []
    >>> data = pd.Series(["2022-03-20", "2022-03-21", "2022-03-23", "2022-03-23", "2022-03-24", "2022-03-25"])
    >>> dm.run(data, date_format='%Y-%m-%d')
    [{'item': '2022-03-20 00:00:00', 'frequency': 1}, {'item': '2022-03-21 00:00:00', 'frequency': 1}, {'item': '2022\
-03-23 00:00:00', 'frequency': 2}, {'item': '2022-03-24 00:00:00', 'frequency': 1}, {'item': '2022-03-25 00:00:00', '\
frequency': 1}]
    >>> dm.to_dqv(data, date_format='%Y-%m-%d')
    [{'dqv_isMeasurementOf': 'date.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'List<Map<String,Stri\
ng>>', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%m-%d"'}], 'dqv_value': '[{"item": "2022-\
03-20 00:00:00", "frequency": 1}, {"item": "2022-03-21 00:00:00", "frequency": 1}, {"item": "2022-03-23 00:00:00", "fre\
quency": 2}, {"item": "2022-03-24 00:00:00", "frequency": 1}, {"item": "2022-03-25 00:00:00", "frequency": 1}]'}]
    >>> data = pd.Series(["01:00:00", "01:00:05", "01:00:10", "01:00:15", "01:00:15", "01:00:15"], name='timestamp')
    >>> dm.run(data, date_format='%H:%M:%S')
    [{'item': '1900-01-01 01:00:00', 'frequency': 1}, {'item': '1900-01-01 01:00:05', 'frequency': 1}, {'item': '\
1900-01-01 01:00:10', 'frequency': 1}, {'item': '1900-01-01 01:00:15', 'frequency': 3}]
    >>> dm.to_dqv(pd.Series([1,2,3,4,5,6]))
    [{'dqv_isMeasurementOf': 'date.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasPa\
rameters': [{'parameter_name': 'date_format', 'value': 'null'}], 'dqv_value': 'null'}]
    >>> dm.run(pd.Series([None, None, None]))
    []
    """
    def __init__(self):
        super(DateFrequencyDistribution, self).__init__(
            identifier='date.frequency_distribution',
            keyword='DateFrequencyDistribution',
            title='Frequency distribution',
            definition='Frequency distribution of the time data.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_items', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='10', description='Number of items to show in the distribution.')]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {'date_format': kwargs.get('date_format', None)}
        try:
            result = self.run(data, **kwargs)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': "" if data.name is None else data.name,
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.Series, **kwargs) -> List[Dict[str, int]]:
        """
        This method returns the frequency distribution of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object containing the number of items that must be show in the frequency distribution (`num_items`).

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            Frequency distribution.
        """
        # check data
        srs = self._check_date_data(data, kwargs.get('date_format', None)).dropna(inplace=False)
        # check if dataset is empty
        if srs.empty:
            return []
        # compute frequency of occurrence of each element and return it
        distribution = srs.value_counts(dropna=False, sort=False)
        return [{'item': str(element), 'frequency': int(frequency)} for element, frequency in distribution.items()]
