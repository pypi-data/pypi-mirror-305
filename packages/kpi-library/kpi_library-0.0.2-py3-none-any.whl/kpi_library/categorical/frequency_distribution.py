# kpi_library/categorical/frequency_distribution.py
import json
import pandas as pd

from typing import List, Dict
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class CategoricalFrequencyDistribution(MetricModel):
    """
    This metric gets the frequency distribution of the categorical data given as parameter.

    Note
    ----
    This metric lets to specify the number of items to show. The parameter `num_items` expresses the first most frequent
    categories that must be shown in the frequency distribution. This parameter must be a number and greater than 0.

    Example
    -------
    >>> c = CategoricalFrequencyDistribution()
    >>> srs = pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    [{'item': 'a', 'frequency': 3}, {'item': 'b', 'frequency': 2}, {'item': 'c', 'frequency': 1}]
    >>> c.run(srs, num_items=1)
    [{'item': 'a', 'frequency': 3}, {'item': 'OTHER', 'frequency': 3}]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': 'ID', 'rdf_datatype': 'List<Map<St\
ring,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"item": "a", "frequency": 3}, {"item": "b", "frequency": 2}, \
{"item": "c", "frequency": 1}]'}]
    >>> srs = pd.Series(['a', None, None, 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    [{'item': 'a', 'frequency': 3}, {'item': 'b', 'frequency': 1}]
    >>> c.run(srs, num_items=1)
    [{'item': 'a', 'frequency': 3}, {'item': 'OTHER', 'frequency': 3}]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': 'ID', 'rdf_datatype': 'List<Map<St\
ring,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"item": "a", "frequency": 3}, {"item": "b", "frequency": 1}]'\
}]
    >>> c.to_dqv(srs, num_items=-8)
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error',\
 'ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(srs, num_items='hello')
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error',\
 'ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddq\
v_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series([123.12313, 1231.23421, 1234124.2134]))
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddq\
v_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series(["2022-03-23", "2022-03-24", "2022-03-25", "2022-03-26", "2022-03-27", "2022-03-28"]))
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddq\
v_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    []
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'categorical.frequency_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'List<Map<Stri\
ng,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(CategoricalFrequencyDistribution, self).__init__(
            identifier='categorical.frequency_distribution',
            keyword='CategoricalFrequencyDistribution',
            title='Frequency distribution',
            definition='Frequency distribution of the categorical data.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_items', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='10', description='Number of items to show in the distribution.')]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        try:
            result = self.run(data, **kwargs)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': [],
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': "" if data.name is None else data.name,
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
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
        srs = self._check_categorical_data(data)
        num_items = kwargs.get('num_items', None)
        if num_items is not None:
            num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        # check if dataset is empty
        if srs.empty:
            return []
        # compute frequency of occurrence of each element
        distribution = srs.value_counts(dropna=False)
        if num_items is not None and distribution.shape[0] > num_items:
            # get the first `num_items` most frequent elements
            distribution = distribution.iloc[:num_items]
            return ([{'item': category, 'frequency': int(frequency)} for category, frequency in distribution.items()]
                    + [{'item': 'OTHER', 'frequency': int(data.shape[0] - distribution.sum())}])
        # return distribution of all data
        return [{'item': category, 'frequency': int(frequency)} for category, frequency in distribution.items()]
