# kpi_library/text/acronyms_frequency_percent.py
import re
import json
import pandas as pd

from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextAcronymsFrequencyPercent(MetricModel):
    """
    This metric computes the number of acronyms in the texts.

    Example
    -------
    >>> c = TextAcronymsFrequencyPercent()
    >>> srs = pd.Series(["United Nations (UN) are back.", "I like to eat pasta.", None, "I don't know how to do it", \
    "Please, help me."], name='text')
    >>> c.run(srs)
    5.0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.acronyms_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float', \
'ddqv_hasParameters': [], 'dqv_value': '5.0'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.acronyms_frequency_percent', 'dqv_computedOn': 'text', 'rdf_datatype': 'Float\
', 'ddqv_hasParameters': [], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextAcronymsFrequencyPercent, self).__init__(
            identifier='text.acronyms_frequency_percent',
            keyword='TextAcronymsFrequencyPercent',
            title='Percentage of acronyms',
            definition='Percentage of acronyms that appear in the texts.',
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
        This method returns the percentage of acronyms that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of acronyms that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        # get acronyms
        count = srs.transform(lambda entry: len(re.findall(r'\b[A-Z.]{2,}s?\b', entry))).astype('float')
        total_num_acronyms = count.sum()
        # get number of words
        total_num_words = srs.str.split(" ").explode().dropna().shape[0]
        # return percentage of acronyms
        return float(round((total_num_acronyms/total_num_words)*100, 2))
