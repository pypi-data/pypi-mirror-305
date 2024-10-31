# kpi_library/text/uppercase.py
import re
import json
import pandas as pd
from itertools import chain

from typing import List
from kpi_library.model import MetricModel
from kpi_library.errors import DataTypeError, EmptyDatasetError
from kpi_library.result_types import ResultTypes


class TextUppercase(MetricModel):
    """
    This metric returns a list of capitalized words that appear in the texts.

    Example
    -------
    >>> c = TextUppercase()
    >>> srs = pd.Series(["The United Nations (UN) are back.", "I like to eat pasta.", "I don't know how to do it", \
    "Please, help me."], name='text')
    >>> c.run(srs)
    ['UN', 'I', 'I']
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.uppercase', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', \
'ddqv_hasParameters': [], 'dqv_value': '["UN", "I", "I"]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.uppercase', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>\
', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextUppercase, self).__init__(
            identifier='text.uppercase',
            keyword='TextUppercase',
            title='Capitalized words',
            definition='List of capitalized words that appear in the texts.',
            expected_data_type=str(ResultTypes.LIST_STR.value),
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

    def run(self, data: pd.Series, **kwargs) -> List[str]:
        """
        This method returns a list of capitalized words that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of str
            List of capitalized words that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # get capitalized words
        capt_list = srs.transform(lambda entry: re.findall(r'\b[A-Z]+s?\b', entry))
        return list(chain.from_iterable(capt_list.to_numpy()))
