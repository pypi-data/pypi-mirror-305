# kpi_library/numeric/count_zeros_percent.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericCountZerosPercent(MetricModel):
    """
    This metric computes the percentage of zeros in the data.

    Example
    -------
    >>> c = NumericCountZerosPercent()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    0.0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.count_zeros_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': '0.0'}]
    >>> c.run(pd.Series([1,None,-3,4,0,6,7], name='Num'))
    14.29
    >>> c.to_dqv(pd.Series([1,None,0,4,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.count_zeros_percent', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_ha\
sParameters': [], 'dqv_value': '14.29'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.count_zeros_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.count_zeros_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericCountZerosPercent, self).__init__(
            identifier='numeric.count_zeros_percent',
            keyword='NumericCountZerosPercent',
            title='Percentage of zeros',
            definition='Percentage of zeros.',
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
        This method returns the percentage of zeros in the data.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of zeros.
        """
        num_rows = data.shape[0]
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        return float(round((np.sum(srs == 0)/num_rows) * 100, 2))
