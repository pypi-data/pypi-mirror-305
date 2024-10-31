# kpi_library/text/count_words.py
import re
import json
import pandas as pd

from typing import Optional, List, Dict
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextCountWords(MetricModel):
    """
    This metric computes the distribution of the length in words of text data.

    Example
    -------
    >>> c = TextCountWords()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    [{'item': 3, 'frequency': 2}, {'item': 5, 'frequency': 1}, {'item': 8, 'frequency': 1}]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.countWords', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<Map<String,String>>\
', 'ddqv_hasParameters': [], 'dqv_value': '[{"item": 3, "frequency": 2}, {"item": 5, "frequency": 1}, {"item": 8, "freq\
uency": 1}]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.count_words', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<Map<String,String>>\
', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextCountWords, self).__init__(
            identifier='text.count_words',
            keyword='TextCountWords',
            title='Count words',
            definition='Distribution of the number of words per text.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_INT.value),
            dimension='profile',
            category='inherent'
        )

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        try:
            result = self.run(data, **kwargs)
        except (EmptyDatasetError, DataTypeError):
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

    def run(self, data: pd.Series, **kwargs) -> Optional[List[Dict[str, int]]]:
        """
        This method counts the number of words per entry and returns the frequency of each word-length.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of `dict`
            List of dictionaries containing the length in words (`item`) and the number of entries that has this
            length (`frequency`).
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # compute the length in words of each entry and return distribution
        words = srs.transform(lambda entry: len([word for word in re.split(r'\W+', entry.lower()) if word != '']))
        lengths = words.value_counts(sort=False)
        return [{'item': int(length), 'frequency': int(count)} for length, count in lengths.items()]
