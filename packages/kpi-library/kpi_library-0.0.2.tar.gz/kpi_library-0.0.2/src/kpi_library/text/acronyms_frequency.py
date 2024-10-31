# kpi_library/text/acronyms_frequency.py
import re
import json
import pandas as pd

from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextAcronymsFrequency(MetricModel):
    """
    This metric computes the number of acronyms in the texts.

    Example
    -------
    >>> c = TextAcronymsFrequency()
    >>> srs = pd.Series(["United Nations (UN) are back.", "I like to eat pasta.", None, "I don't know how to do it", \
    "Please, help me."], name='text')
    >>> c.run(srs)
    1
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.acronyms_frequency', 'dqv_computedOn': 'text', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '1'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.acronyms_frequency', 'dqv_computedOn': 'text', 'rdf_datatype': 'Integer\
', 'ddqv_hasParameters': [], 'dqv_value': '0'}]
    """
    def __init__(self):
        super(TextAcronymsFrequency, self).__init__(
            identifier='text.acronyms_frequency',
            keyword='TextAcronymsFrequency',
            title='Number of acronyms',
            definition='Number of acronyms that appear in the texts.',
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
        This method returns the number of acronyms that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: int
            Number of acronyms that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return 0
        # get acronyms
        count = srs.transform(lambda entry: len(re.findall(r'\b[A-Z.]{2,}s?\b', entry))).astype('int')
        return int(count.sum())
