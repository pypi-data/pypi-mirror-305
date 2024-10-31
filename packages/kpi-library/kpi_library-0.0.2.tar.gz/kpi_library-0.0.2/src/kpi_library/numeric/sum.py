# kpi_library/numeric/sum.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericSum(MetricModel):
    """
    This metric sums all values in the numeric column of data.

    Example
    -------
    >>> c = NumericSum()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    28.0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.sum', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasParam\
eters': [], 'dqv_value': '28.0'}]
    >>> c.run(pd.Series([1,None,3,4,5,6,7], name='Num'))
    26.0
    >>> c.to_dqv(pd.Series([1,None,3,4,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.sum', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': '26.0'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.sum', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.sum', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericSum, self).__init__(
            identifier='numeric.sum',
            keyword='NumericSum',
            title='Sum',
            definition='Sum of all values in the numeric data.',
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

    def run(self, data: pd.Series, **kwargs) -> Optional[float]:
        """
        This method sums the values of the given data.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Sum of the data.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        return float(np.sum(srs))
