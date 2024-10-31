# kpi_library/text/acronyms.py
import re
import json
import pandas as pd
from itertools import chain

from typing import List
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextAcronyms(MetricModel):
    """
    This metric returns a list of acronyms that appear in the texts.

    Example
    -------
    >>> c = TextAcronyms()
    >>> srs = pd.Series(["United Nations (UN) are back.", "I like to eat pasta.", None, "I don't know how to do it", \
    "Please, help me."], name='text')
    >>> c.run(srs)
    ['UN']
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.acronyms', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', \
'ddqv_hasParameters': [], 'dqv_value': '["UN"]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.acronyms', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>\
', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextAcronyms, self).__init__(
            identifier='text.acronyms',
            keyword='TextAcronyms',
            title='Acronyms',
            definition='List of acronyms that appear in the texts.',
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
        This method returns a list of acronyms that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of str
            List of acronyms that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # get words
        acronyms_list = srs.transform(lambda entry: re.findall(r'\b[A-Z.]{2,}s?\b', entry))
        return list(chain.from_iterable(acronyms_list.to_numpy()))
