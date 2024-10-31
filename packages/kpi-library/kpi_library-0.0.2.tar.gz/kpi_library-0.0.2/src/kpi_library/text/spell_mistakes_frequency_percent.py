# kpi_library/text/spell_mistakes_frequency_percent.py
import re
import json
import pandas as pd
from spellchecker import SpellChecker

from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class TextSpellMistakesFrequencyPercent(MetricModel):
    """
    This metric computes the percentage of spell mistakes in the texts.

    Example
    -------
    >>> c = TextSpellMistakesFrequencyPercent()
    >>> srs = pd.Series(["are you", "I likej to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    11.11
    >>> c.to_dqv(srs, lang='en')
    [{'dqv_isMeasurementOf': 'text.spell_mistakes_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Flo\
at', 'ddqv_hasParameters': [{'parameter_name': 'lang', 'value': '"en"'}], 'dqv_value': '11.11'}]
    >>> c.to_dqv(srs, lang='-1')
    [{'dqv_isMeasurementOf': 'text.spell_mistakes_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Err\
or', 'ddqv_hasParameters': [{'parameter_name': 'lang', 'value': '"-1"'}], 'dqv_value': 'null'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.spell_mistakes_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float\
', 'ddqv_hasParameters': [{'parameter_name': 'lang', 'value': '"en"'}], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextSpellMistakesFrequencyPercent, self).__init__(
            identifier='text.spell_mistakes_frequency_percent',
            keyword='TextSpellMistakesFrequencyPercent',
            title='Percentage of spell mistakes',
            definition='Percentage of spell mistakes that appear in the texts.',
            expected_data_type=str(ResultTypes.FLOAT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name="lang", data_type=str(ResultTypes.STRING.value),
                           description='Language in which the texts are written in.',
                           possible_values=['de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'], default_value="en")]

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        params = {"lang": kwargs.get("lang", "en")}
        try:
            result = self.run(data, **params)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "" if data.name is None else data.name,
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

    def run(self, data: pd.Series, **kwargs) -> float:
        """
        This method returns the percentage of spell mistakes that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of spell mistakes that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        lang = kwargs.get("lang", "en")
        self._check_enum_parameter(
            parameter=lang, parameter_name='lang', values=['de', 'en', 'es', 'fr', 'pt', 'ru', 'ar'])
        # get words
        words = srs.transform(lambda text: [item for item in re.split(r'\W+', text.lower()) if item != '']).explode()
        # compute number of misspellings in the data
        spell = SpellChecker(language=lang)
        return float(round((len(spell.unknown(words))/words.shape[0])*100, 2))
