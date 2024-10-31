# kpi_library/general/duplicated_entries_percent.py
import json
import pandas as pd
from typing import Union, Optional

from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes


class GeneralDuplicatedEntriesPercent(MetricModel):
    """
    This metric returns the percentage of rows that are duplicated in the dataset.

    Examples
    --------
    >>> gm = GeneralDuplicatedEntriesPercent()
    >>> gm.run(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
    75.0
    >>> gm.run(pd.Series([1, 2, 3, 1], name='num'))
    25.0
    >>> gm.run(pd.Series([1, 2, 3, 4], name='num'))
    0.0
    >>> gm.run(pd.Series([None, None, None, None]))
    75.0
    >>> gm.to_dqv(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
    [{'dqv_isMeasurementOf': 'general.duplicated_entries_percent', 'dqv_computedOn': 'DATASET', 'rdf_datatype': 'Int\
eger', 'ddqv_hasParameters': [], 'dqv_value': '50.0'}]
    """
    def __init__(self):
        super(GeneralDuplicatedEntriesPercent, self).__init__(
            identifier='general.duplicated_entries_percent',
            keyword='GeneralDuplicatedEntriesPercent',
            title='Percentage of duplicated rows.',
            definition='Percentage of rows that are duplicated in the dataset.',
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

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[float]:
        """
        It computes the percentage of rows that are duplicated in the data.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.

        Return
        ------
        _: float
            Percentage of rows that are duplicated in the dataset.
        """
        if data.empty:
            return None
        # get the index of those rows that are duplicated and get length
        indices: pd.Series = data.duplicated()
        return float(round((indices.sum()/data.shape[0])*100, 2))
