# kpi_library/numeric/kurtosis.py
import json
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericKurtosis(MetricModel):
    """
    This metric computes the kurtosis of a numeric column.

    Example
    -------
    >>> c = NumericKurtosis()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    -1.2000000000000002
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.kurtosis', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasParam\
eters': [], 'dqv_value': '-1.2000000000000002'}]
    >>> c.run(pd.Series([1,None,3,4,5,6,7], name='Num'))
    -0.3000000000000025
    >>> c.to_dqv(pd.Series([1,None,3,4,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.kurtosis', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': '-0.3000000000000025'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.kurtosis', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.kurtosis', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericKurtosis, self).__init__(
            identifier='numeric.kurtosis',
            keyword='NumericKurtosis',
            title='Kurtosis',
            definition='Kurtosis of the numeric data.',
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
        This method returns the kurtosis value of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Kurtosis of the data.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        return float(srs.kurtosis(skipna=False))
