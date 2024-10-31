# kpi_library/general/duplicated_entries.py
import json
import pandas as pd
from typing import Union, Optional

from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes


class GeneralDuplicatedEntries(MetricModel):
    """
    This metric returns the number of duplicated rows in the dataset.

    Examples
    --------
    >>> gm = GeneralDuplicatedEntries()
    >>> gm.run(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
    3
    >>> gm.run(pd.Series([1, 2, 3, 1], name='num'))
    1
    >>> gm.run(pd.Series([1, 2, 3, 4], name='num'))
    0
    >>> gm.run(pd.Series([None, None, None, None]))
    3
    >>> gm.to_dqv(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
    [{'dqv_isMeasurementOf': 'general.duplicated_entries', 'dqv_computedOn': 'DATASET', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '2'}]
    """
    def __init__(self):
        super(GeneralDuplicatedEntries, self).__init__(
            identifier='general.duplicated_entries',
            keyword='GeneralDuplicatedEntries',
            title='Number of duplicated rows.',
            definition='Number of rows that are duplicated in the dataset.',
            expected_data_type=str(ResultTypes.INT.value),
            dimension='profile',
            category='inherent'
        )

    def to_dqv(self, data: Union[pd.Series, pd.DataFrame], **kwargs):
        """"""
        try:
            result = self.run(data, **kwargs)
        except EmptyDatasetError:
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': [],
                'dqv_value': json.dumps(None)
            }]
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': 'DATASET',
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[int]:
        """
        It computes the number of rows that are duplicated in the data.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.

        Return
        ------
        _: int
            Number of rows that are duplicated in the dataset.
        """
        if data.empty:
            return None
        # get the index of those rows that are duplicated and get length
        indices: pd.Series = data.duplicated()
        return int(indices.sum())
