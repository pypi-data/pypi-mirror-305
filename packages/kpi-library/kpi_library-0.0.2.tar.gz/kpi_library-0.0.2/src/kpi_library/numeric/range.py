# kpi_library/numeric/range.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericRange(MetricModel):
    """
    This metric computes the range between the maximum and minimum value of the numeric column given as parameter.

    Example
    -------
    >>> c = NumericRange()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    6.0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.range', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasParam\
eters': [], 'dqv_value': '6.0'}]
    >>> c.run(pd.Series([1,None,3,4,5,6,7], name='Num'))
    6.0
    >>> c.to_dqv(pd.Series([1,None,3,4,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.range', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': '6.0'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.range', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.range', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericRange, self).__init__(
            identifier='numeric.range',
            keyword='NumericRange',
            title='Range',
            definition='Range between the maximum and minimum value of the numeric data.',
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
        This method returns the range between the maximum and minimum values of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Range of the data.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        srs = srs.to_numpy()
        return float(np.max(srs) - np.min(srs))
