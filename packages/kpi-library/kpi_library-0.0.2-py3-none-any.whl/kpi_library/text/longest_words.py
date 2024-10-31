# kpi_library/text/longest_words.py
import re
import json
import pandas as pd

from typing import List
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TextLongestWords(MetricModel):
    """
    This metric gets those words that are longer than a specified length.

    Example
    -------
    >>> c = TextLongestWords()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs, length=4)
    ['like', 'pasta', 'know', 'please', 'help']
    >>> c.to_dqv(srs, length=4)
    [{'dqv_isMeasurementOf': 'text.longest_words', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', 'ddqv_has\
Parameters': [{'parameter_name': 'length', 'value': '4'}], 'dqv_value': '["like", "pasta", "know", "please", "help"]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.longest_words', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', 'ddqv_has\
Parameters': [{'parameter_name': 'length', 'value': '7'}], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextLongestWords, self).__init__(
            identifier='text.longest_words',
            keyword='TextLongestWords',
            title='Longest words',
            definition='Words that are longer than the specified length.',
            expected_data_type=str(ResultTypes.LIST_STR.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='length', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='7', description="Minimum length of the words to pick.")]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {'length': kwargs.get('length', 7)}
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

    def run(self, data: pd.Series, **kwargs) -> List[str]:
        """
        This method returns those words that are longer than the specified length.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list`
            List of words that are longer than a specified length.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # check parameter
        length = self._check_int_parameter(parameter=kwargs.get("length", 7), parameter_name="length", ge=1)
        # compute the length in words of each entry and return distribution
        words = srs.transform(
            lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != '']
        ).explode().unique()
        return [word for word in words if len(word) >= length]
