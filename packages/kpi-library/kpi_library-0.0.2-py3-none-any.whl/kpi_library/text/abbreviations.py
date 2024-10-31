# kpi_library/text/abbreviations.py
import json
import contractions
import pandas as pd

from typing import List
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class TextAbbreviations(MetricModel):
    """
    This metric returns a list of abbreviations that appear in the texts.

    Example
    -------
    >>> c = TextAbbreviations()
    >>> srs = pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", "Please. Help me."],\
    name='text')
    >>> c.run(srs)
    ["don't"]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.abbreviations', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', \
'ddqv_hasParameters': [], 'dqv_value': '["don\\'t"]'}]
    >>> srs = pd.Series([None, None, None], name='text')
    >>> c.run(srs)
    []
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'text.abbreviations', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>\
', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(TextAbbreviations, self).__init__(
            identifier='text.abbreviations',
            keyword='TextAbbreviations',
            title='Abbreviations',
            definition='List of abbreviations that appear in the texts.',
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
        This method returns a list of abbreviations that appear in the texts.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of str
            List of abbreviations that appear in the texts.
        """
        srs = self._check_text_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # get words
        words = srs.str.split(" ").explode().dropna()
        # get abbreviations
        list_abbreviations = []
        for word in words:
            try:
                temp = contractions.fix(word)
                list_abbreviations += [word] if temp != word else []
            except IndexError:
                # pass when this error happens
                pass
        return list_abbreviations
