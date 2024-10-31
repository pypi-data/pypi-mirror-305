# kpi_library/text/distribution_less_frequent_elements_percent.py
import re
import json
import pandas as pd

from typing import Optional, List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TextDistributionLessFrequentElementPercent(MetricModel):
    """
    This metric studies the frequency distribution of the less frequent words in the texts.

    Example
    -------
    >>> c = TextDistributionLessFrequentElementPercent()
    >>> srs = pd.Series(["how are you", "how you crush."], name='text')
    >>> c.run(srs)
    [{'item': 'are', 'frequency': 16.67}, {'item': 'crush', 'frequency': 16.67}, {'item': 'how', 'frequency': 33.33}, \
{'item': 'you', 'frequency': 33.33}]
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs, num_items=3)
    [{'item': 'are', 'frequency': 5.26}, {'item': 'you', 'frequency': 5.26}, {'item': 'like', 'frequency': 5.26}]
    >>> c.to_dqv(srs, num_items=3)
    [{'dqv_isMeasurementOf': 'text.distribution_less_frequent_elements_percent', 'dqv_computedOn': 'text', 'rdf_datatyp\
e': 'List<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '3'}], 'dqv_value': '[{\
"item": "are", "frequency": 5.26}, {"item": "you", "frequency": 5.26}, {"item": "like", "frequency": 5.26}]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.distribution_less_frequent_elements_percent', 'dqv_computedOn': 'text', 'rdf_datatyp\
e': 'List<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '10'}], 'dqv_value': '[\
]'}]
    """
    def __init__(self):
        super(TextDistributionLessFrequentElementPercent, self).__init__(
            identifier='text.distribution_less_frequent_elements_percent',
            keyword='TextDistributionLessFrequentElementPercent',
            title='Distribution of the less frequent words',
            definition='Distribution in percentage of the less frequent words.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_FLOAT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_items', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='10', description="Number of elements to show.")]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {'num_items': kwargs.get('num_items', 10)}
        try:
            result = self.run(data, **params)
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

    def run(self, data: pd.Series, **kwargs) -> Optional[List[Dict[str, Union[str, int]]]]:
        """
        This method returns the frequency distribution in percentage of the less frequent words in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of `dict`
            List of dictionaries containing the less frequent words (`item`) and its frequency in percentage
            (`frequency`).
        """
        # check data
        srs = self._check_text_data(data)
        if srs.empty:
            return []
        # check parameter
        num_items = kwargs.get('num_items')
        num_items = None if num_items is None else self._check_int_parameter(
            parameter=num_items, parameter_name='num_items', ge=1)
        # split texts into words and compute the frequency of each of them
        words = srs.transform(lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != '']).explode()
        freq_dist = words.value_counts(sort=True, ascending=True, dropna=True)
        num_words = words.shape[0]
        return [{
            'item': word, 'frequency': float(round((freq/num_words)*100, 2))
        } for word, freq in (freq_dist if num_items is None else freq_dist.iloc[:num_items]).items()]
