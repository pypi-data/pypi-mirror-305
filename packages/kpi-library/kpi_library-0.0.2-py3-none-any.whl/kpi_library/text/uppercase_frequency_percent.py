# kpi_library/text/uppercase_frequency_percent.py
import re
import json
import pandas as pd

from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextUppercaseFrequencyPercent(MetricModel):
    """
    This metric computes the number of capitalized words in the texts.

    Example
    -------
    >>> c = TextUppercaseFrequencyPercent()
    >>> srs = pd.Series(["The United Nations (UN) are back.", "I like to eat pasta.", "I don't know how to do it", \
    "Please, help me."], name='text')
    >>> c.run(srs)
    14.29
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.uppercase_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float', \
'ddqv_hasParameters': [], 'dqv_value': '14.29'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.uppercase_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float\
', 'ddqv_hasParameters': [], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextUppercaseFrequencyPercent, self).__init__(
            identifier='text.uppercase_frequency_percent',
            keyword='TextUppercaseFrequencyPercent',
            title='Percentage of capitalized words',
            definition='Percentage of capitalized words that appear in the texts.',
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
        This method returns the percentage of capitalized words that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of capitalized words that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        # get percentage of capitalized words
        num_capt_list = srs.transform(lambda text: len(re.findall(r'\b[A-Z]+s?\b', text))).sum()
        num_total_words = srs.str.split(" ").str.len().sum()
        return float(round((num_capt_list/num_total_words)*100, 2))
