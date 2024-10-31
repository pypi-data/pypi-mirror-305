# kpi_library/text/lexical_diversity_uniqueness.py
import re
import json
import pandas as pd

from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextLexicalDiversityUniqueness(MetricModel):
    """
    This metric computes the ratio between the number of distinct words with the total number of words in the texts.

    Example
    -------
    >>> c = TextLexicalDiversityUniqueness()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    84.21
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.lexical_diversity_uniqueness', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float', \
'ddqv_hasParameters': [], 'dqv_value': '84.21'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> srs = pd.Series(["", "", ""], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.lexical_diversity_uniqueness', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float', \
'ddqv_hasParameters': [], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextLexicalDiversityUniqueness, self).__init__(
            identifier='text.lexical_diversity_uniqueness',
            keyword='TextLexicalDiversityUniqueness',
            title='Uniqueness',
            definition='Rate between the number of distinct words and the number of total words.',
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
        This method computes the rate between the number of distinct words and the number of total words.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            This method computes the rate between the number of distinct words and the number of total words.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        # get words
        words = srs.transform(
            lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != '']
        ).explode().dropna()
        return 0 if words.shape[0] == 0 else float(round((words.unique().shape[0]/words.shape[0])*100, 2))
