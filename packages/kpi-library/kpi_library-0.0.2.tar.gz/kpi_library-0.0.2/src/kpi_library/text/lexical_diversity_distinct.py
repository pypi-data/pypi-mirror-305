# kpi_library/text/lexical_diversity_distinct.py
import re
import json
import pandas as pd

from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextLexicalDiversityDistinct(MetricModel):
    """
    This metric computes the number of distinct words in the texts.

    Example
    -------
    >>> c = TextLexicalDiversityDistinct()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    16
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.lexical_diversity_distinct', 'dqv_computedOn': 'text', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '16'}]
    >>> srs = pd.Series(["", "", ""], name='text')
    >>> c.run(srs)
    0
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.lexical_diversity_distinct', 'dqv_computedOn': 'text', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextLexicalDiversityDistinct, self).__init__(
            identifier='text.lexical_diversity_distinct',
            keyword='TextLexicalDiversityDistinct',
            title='Number of distinct words',
            definition='The total number of distinct words in the texts.',
            expected_data_type=str(ResultTypes.INT.value),
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

    def run(self, data: pd.Series, **kwargs) -> int:
        """
        This method gets the number of distinct words in the texts of `data`.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: int
            Number of distinct words.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        # get words
        words = srs.transform(
            lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != '']
        ).explode().dropna()
        return int(words.unique().shape[0])
