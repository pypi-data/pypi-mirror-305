# kpi_library/text/distribution_most_frequent_elements.py
import re
import json
import pandas as pd
import nltk
from nltk.corpus import stopwords

from typing import Optional, List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes

nltk.download("stopwords")


class TextDistributionMostFrequentElement(MetricModel):
    """
    This metric studies the frequency distribution of the most frequent words in the texts.

    Example
    -------
    >>> c = TextDistributionMostFrequentElement()
    >>> srs = pd.Series(["how are you", "how you crush."], name='text')
    >>> c.run(srs)
    [{'item': 'how', 'frequency': 2}, {'item': 'you', 'frequency': 2}, {'item': 'are', 'frequency': 1}, {'item': \
'crush', 'frequency': 1}]
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs, num_items=3, stopwords_removal=False, language='english')
    [{'item': 'how', 'frequency': 2}, {'item': 'i', 'frequency': 2}, {'item': 'to', 'frequency': 2}]
    >>> c.run(srs, num_items=3, stopwords_removal=True, language='english')
    [{'item': 'like', 'frequency': 1}, {'item': 'eat', 'frequency': 1}, {'item': 'pasta', 'frequency': 1}]
    >>> c.to_dqv(srs, num_items=3, stopwords_removal=True, language='english')
    [{'dqv_isMeasurementOf': 'text.distribution_most_frequent_elements', 'dqv_computedOn': 'text', 'rdf_datatype': 'Lis\
t<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '3'}, {'parameter_name': 'stopw\
ords_removal', 'value': 'true'}, {'parameter_name': 'language', 'value': '"english"'}], 'dqv_value': '[{"item": "like\
", "frequency": 1}, {"item": "eat", "frequency": 1}, {"item": "pasta", "frequency": 1}]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.distribution_most_frequent_elements', 'dqv_computedOn': 'text', 'rdf_datatype': 'Lis\
t<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '10'}, {'parameter_name': 'stop\
words_removal', 'value': 'false'}, {'parameter_name': 'language', 'value': '"english"'}], 'dqv_value': '[]'}]
    """
    LANGUAGE_STOPWORDS: List[str] = stopwords.fileids()

    def __init__(self):
        super(TextDistributionMostFrequentElement, self).__init__(
            identifier='text.distribution_most_frequent_elements',
            keyword='TextDistributionMostFrequentElement',
            title='Distribution of the most frequent words',
            definition='Distribution of the most frequent words.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_items', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='10', description="Number of elements to show."),
            ParameterModel(
                name='stopwords_removal', data_type=str(ResultTypes.BOOL.value), default_value='true',
                description="Whether the stopwords must be removed or not.", possible_values=['false', 'true']),
            ParameterModel(
                name='language', data_type=str(ResultTypes.STRING.value), default_value="english",
                possible_values=self.LANGUAGE_STOPWORDS, description="Language in which the texts are written.")
        ]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {
            'num_items': kwargs.get('num_items', 10),
            'stopwords_removal': kwargs.get('stopwords_removal', False),
            'language': kwargs.get('language', 'english')
        }
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
        This method returns the frequency distribution of the most frequent words in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of `dict`
            List of dictionaries containing the most frequent words (`item`) and its frequency (`frequency`).
        """
        # check data
        srs = self._check_text_data(data)
        if srs.empty:
            return []
        # check parameters
        num_items = kwargs.get('num_items')
        num_items = None if num_items is None else self._check_int_parameter(
            parameter=num_items, parameter_name='num_items', ge=1)
        stopwords_removal = self._check_boolean_parameter(
            parameter=kwargs.get('stopwords_removal', False), parameter_name='stopwords_removal')
        language = kwargs.get('language', "english")
        self._check_enum_parameter(parameter=language, parameter_name='language', values=self.LANGUAGE_STOPWORDS)
        # split texts into words
        words = srs.transform(lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != ''])
        # remove stopwords if it is necessary
        if stopwords_removal:
            _stopwords = set(stopwords.words(language))
            words = words.apply(lambda entry: [word for word in entry if word not in _stopwords])
        # compute frequency of each word
        freq_dist = words.explode().value_counts(sort=True, ascending=False, dropna=True)
        return [{
            'item': word, 'frequency': int(freq)
        } for word, freq in (freq_dist if num_items is None else freq_dist.iloc[:num_items]).items()]
