# kpi_library/text/count_sentences_percent.py
import json
import pandas as pd
from nltk.tokenize import sent_tokenize

from typing import Optional, List, Dict, Union
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextCountSentencesPercent(MetricModel):
    """
    This metric computes the percentage of occurrence of the different sentences lengths in the data. First, it splits
    the texts into sentences and counts how many of them are in each entry. Once the method knows how many sentences
    there are, it counts how many times each sentence length appears in the data and returns the percentage of
    occurrence of each of them.

    Example
    -------
    >>> c = TextCountSentencesPercent()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    [{'item': 1, 'frequency': 60.0}, {'item': 2, 'frequency': 20.0}]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.count_sentences_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<Map<Stri\
ng,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"item": 1, "frequency": 60.0}, {"item": 2, "frequency": 20.0}\
]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.count_sentences_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<Map<Stri\
ng,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextCountSentencesPercent, self).__init__(
            identifier='text.count_sentences_percent',
            keyword='TextCountSentencesPercent',
            title='Count sentences',
            definition='Distribution in percentage of the number of sentences per text.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_FLOAT.value),
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

    def run(self, data: pd.Series, **kwargs) -> Optional[List[Dict[str, Union[int, float]]]]:
        """
        This method counts the percentage of entries that are composed for a specific number of sentences, i.e.,
        computes the distribution in percentage of the sentence length.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of `dict`
            Distribution in percentage of the sentence length.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # compute the length in sentences of each entry and return distribution
        tokenized_sentences_count = srs.transform(lambda entry: len(sent_tokenize(entry))).value_counts(sort=False)
        return [{
            'item': int(length), 'frequency': float(round((count/data.shape[0])*100, 2))
        } for length, count in tokenized_sentences_count.items()]
