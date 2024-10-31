# kpi_library/text/abbreviations_frequency_percent.py
import json
import contractions
import pandas as pd

from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextAbbreviationsFrequencyPercent(MetricModel):
    """
    This metric computes the number of abbreviations in the texts.

    Example
    -------
    >>> c = TextAbbreviationsFrequencyPercent()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    5.56
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.abbreviations_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float',\
 'ddqv_hasParameters': [], 'dqv_value': '5.56'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.abbreviations_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float\
', 'ddqv_hasParameters': [], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextAbbreviationsFrequencyPercent, self).__init__(
            identifier='text.abbreviations_frequency_percent',
            keyword='TextAbbreviationsFrequencyPercent',
            title='Percentage of abbreviations',
            definition='Percentage of abbreviations that appear in the texts.',
            expected_data_type=str(ResultTypes.FLOAT.value),
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

    def run(self, data: pd.Series, **kwargs) -> float:
        """
        This method returns the percentage of abbreviations that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of abbreviations that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        # get words
        words = srs.str.split(" ").explode().dropna()
        # get abbreviations
        num_abbreviations = 0
        for word in words:
            try:
                num_abbreviations += contractions.fix(word) != word
            except IndexError:
                # pass when this error happens
                pass
        return float(round((num_abbreviations/words.shape[0])*100, 2))
