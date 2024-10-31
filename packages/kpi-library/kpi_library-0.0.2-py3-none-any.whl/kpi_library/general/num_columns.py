# kpi_library/general/num_columns.py
from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import json
import pandas as pd
from typing import Union


class GeneralNumColumns(MetricModel):
    """
    This metric returns the number of rows in the dataset.

    Examples
    --------
    >>> gm = GeneralNumColumns()
    >>> gm.run(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
    3
    >>> gm.run(pd.Series([1, 1, 1, 1], name='num'))
    1
    >>> gm.run(pd.Series([None, None, None, None]))
    1
    >>> gm.to_dqv(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
    [{'dqv_isMeasurementOf': 'general.num_columns', 'dqv_computedOn': 'DATASET', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '3'}]
    """
    def __init__(self):
        super(GeneralNumColumns, self).__init__(
            identifier='general.num_columns',
            keyword='GeneralNumColumns',
            title='Number of columns.',
            definition='Number of columns in the dataset.',
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

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> int:
        """
        It computes the number of columns in the data.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.

        Return
        ------
        _: int
            Number of columns in the dataset.
        """
        return 1 if isinstance(data, pd.Series) else data.shape[1]
