# kpi_library/text/collocations_distribution.py
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


class TextCollocationDistribution(MetricModel):
    """
    This metric studies the frequency distribution of the most frequent collocations in the texts.

    Example
    -------
    >>> c = TextCollocationDistribution()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs, num_items=3, language='english', collocation='bigram')
    [{'item': 'like eat', 'frequency': 1}, {'item': 'eat pasta', 'frequency': 1}, {'item': 'please help', 'frequency':\
 1}]
    >>> c.run(srs, num_items=1, language='english', collocation='trigram')
    [{'item': 'like eat pasta', 'frequency': 1}]
    >>> c.to_dqv(srs, num_items=2, language='english', collocation='both')
    [{'dqv_isMeasurementOf': 'text.collocations_distribution', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<\
Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parameter_name': 'langu\
age', 'value': '"english"'}, {'parameter_name': 'collocation', 'value': '"both"'}], 'dqv_value': '[{"item": "like eat \
pasta", "frequency": 1}, {"item": "like eat", "frequency": 1}]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.collocations_distribution', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<\
Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '10'}, {'parameter_name': 'langu\
age', 'value': '"english"'}, {'parameter_name': 'collocation', 'value': '"bigram"'}], 'dqv_value': '[]'}]
    """
    LANGUAGE_STOPWORDS: List[str] = stopwords.fileids()

    def __init__(self):
        super(TextCollocationDistribution, self).__init__(
            identifier='text.collocations_distribution',
            keyword='TextCollocationDistribution',
            title='Distribution of collocations',
            definition='Distribution of collocations.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_items', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='10', description="Number of elements to show."),
            ParameterModel(
                name='language', data_type=str(ResultTypes.STRING.value), default_value="english",
                possible_values=self.LANGUAGE_STOPWORDS, description="Language in which the texts are written."),
            ParameterModel(name='collocation', data_type=str(ResultTypes.STRING.value), default_value='bigram',
                           description="Type of collocation to obtain. `both` means the method should search for bigram"
                                       " and trigram collocations", possible_values=['bigram', 'trigram', 'both'])
        ]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {
            'num_items': kwargs.get('num_items', 10),
            'language': kwargs.get('language', 'english'),
            'collocation': kwargs.get('collocation', 'bigram'),
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
        This method returns the frequency distribution of the most frequent collocations in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of `dict`
            List of dictionaries containing the most frequent collocations (`item`) and its frequency (`frequency`).
        """
        # check data
        srs = self._check_text_data(data)
        if srs.empty:
            return []
        # check parameters
        num_items = kwargs.get('num_items')
        num_items = None if num_items is None else self._check_int_parameter(
            parameter=num_items, parameter_name='num_items', ge=1)
        language = kwargs.get('language', "english")
        collocation = kwargs.get('collocation', "bigram")
        self._check_enum_parameter(parameter=language, parameter_name='language', values=self.LANGUAGE_STOPWORDS)
        self._check_enum_parameter(parameter=collocation, parameter_name='collocation',
                                   values=['bigram', 'trigram', 'both'])
        # tokenize data
        words = srs.transform(lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != ''])
        # remove stopwords
        _stopwords = set(stopwords.words(language))
        words = words.apply(lambda entry: [word for word in entry if word not in _stopwords])
        # get collocations
        collocations = words.transform(getattr(self, f'_get_{collocation}')).explode()
        # compute frequency and return
        freq_dist = collocations.value_counts(sort=True, ascending=False)
        return [{
            'item': word, 'frequency': int(freq)
        } for word, freq in (freq_dist if num_items is None else freq_dist.iloc[:num_items]).items()]

    @staticmethod
    def _get_bigram(entry: List[str]) -> List[str]:
        """
        Return a list with the bigrams in entry.

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List with words to transform.

        Returns
        -------
        _: :obj:`list` of :obj:`tuple`
            A list of tuples with the bigrams.
        """
        return [f'{word1} {word2}' for word1, word2 in zip(entry[:-1], entry[1:])]

    @staticmethod
    def _get_trigram(entry: List[str]) -> List[str]:
        """
        Return a list with trigrams of entry.

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List with words to transform.

        Returns
        -------
        _: :obj:`list` of :obj:`tuple`
            A list of tuples with the trigrams.
        """
        return [f'{word1} {word2} {word3}' for word1, word2, word3 in zip(entry[:-2], entry[1:-1], entry[2:])]

    @staticmethod
    def _get_both(entry: List[str]) -> List[str]:
        """
        Return a list with bigrams and trigrams of entry.

        Parameters
        ----------
        entry: :obj:`list` of :obj:`str`
            List with words to transform.

        Returns
        -------
        _: :obj:`list` of :obj:`tuple`
            A list of tuples with the bigrams and trigrams.
        """
        # compute trigrams and bigrams
        grams = [f"{word1} {word2} {word3}" for word1, word2, word3 in zip(entry[:-2], entry[1:-1], entry[2:])]
        grams += [f"{word1} {word2}" for word1, word2 in zip(entry[:-1], entry[1:])]
        # return obtained collocations
        return grams

