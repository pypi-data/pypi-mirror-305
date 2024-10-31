# kpi_library/text/spell_mistakes.py
import re
import json
import pandas as pd
from spellchecker import SpellChecker

from typing import List
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TextSpellMistakes(MetricModel):
    """
    This metric returns a list of spell mistakes that appear in the texts.

    Example
    -------
    >>> c = TextSpellMistakes()
    >>> srs = pd.Series(["are you", "I likej to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs, language="en")
    ['likej', 't']
    >>> srs = pd.Series(["are you", "I likej to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.spell_mistakes', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', \
'ddqv_hasParameters': [{'parameter_name': 'lang', 'value': '"en"'}], 'dqv_value': '["likej", "t"]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.spell_mistakes', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>\
', 'ddqv_hasParameters': [{'parameter_name': 'lang', 'value': '"en"'}], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextSpellMistakes, self).__init__(
            identifier='text.spell_mistakes',
            keyword='TextSpellMistakes',
            title='Spell mistakes',
            definition='List of spell mistakes that appear in the texts.',
            expected_data_type=str(ResultTypes.LIST_STR.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name="lang", data_type=str(ResultTypes.STRING.value),
                           description='Language in which the texts are written in.',
                           possible_values=['de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'], default_value="en")]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {'lang': kwargs.get("lang", "en")}
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

    def run(self, data: pd.Series, **kwargs) -> List[str]:
        """
        This method returns a list of spell mistakes that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of str
            List of spell mistakes that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        lang = kwargs.get("lang", "en")
        self._check_enum_parameter(
            parameter=lang, parameter_name='lang', values=['de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'])
        # get words
        words = srs.transform(lambda text: [item for item in re.split(r'\W+', text.lower()) if item != '']).explode()
        # compute number of misspellings in the data
        spell = SpellChecker(language=lang)
        return list(spell.unknown(words))
