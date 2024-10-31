# kpi_library/numeric/count_zeros.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericCountZeros(MetricModel):
    """
    This metric computes the number of zeros in the data.

    Example
    -------
    >>> c = NumericCountZeros()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.count_zeros', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParam\
eters': [], 'dqv_value': '0'}]
    >>> c.run(pd.Series([1,None,-3,4,0,6,7], name='Num'))
    1
    >>> c.to_dqv(pd.Series([1,None,0,4,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.count_zeros', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Integer', 'ddqv_hasPa\
rameters': [], 'dqv_value': '1'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.count_zeros', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.count_zeros', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericCountZeros, self).__init__(
            identifier='numeric.count_zeros',
            keyword='NumericCountZeros',
            title='Number of zeros',
            definition='Counts the number of zeros.',
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

    def run(self, data: pd.Series, **kwargs) -> Optional[int]:
        """
        This method counts the number of zeros in the data.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: int
            Number of zeros.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        return int(np.sum(srs == 0))
