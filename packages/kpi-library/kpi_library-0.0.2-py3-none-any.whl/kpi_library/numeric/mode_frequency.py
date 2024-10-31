# kpi_library/numeric/mode_frequency.py
import json
import pandas as pd
from scipy import stats

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericModeFrequency(MetricModel):
    """
    This metric gets the frequency of the most frequent number in the numeric column.

    Example
    -------
    >>> c = NumericModeFrequency()
    >>> srs = pd.Series([1,2,3,4,4,6,7])
    >>> c.run(srs)
    2
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParam\
eters': [], 'dqv_value': '2'}]
    >>> c.run(pd.Series([1,None,3,4,6,None,6], name='Num'))
    2
    >>> c.to_dqv(pd.Series([1,None,3,6,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.mode_frequency', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Integer', 'ddqv_hasPa\
rameters': [], 'dqv_value': '2'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.mode_frequency', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericModeFrequency, self).__init__(
            identifier='numeric.mode_frequency',
            keyword='NumericModeFrequency',
            title='Mode frequency',
            definition='Frequency of the most frequent number of the numeric data.',
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
        This method returns the frequency of the most frequent number of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: int
            Mode frequency.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        return int(stats.mode(srs, keepdims=False, nan_policy='omit').count)
