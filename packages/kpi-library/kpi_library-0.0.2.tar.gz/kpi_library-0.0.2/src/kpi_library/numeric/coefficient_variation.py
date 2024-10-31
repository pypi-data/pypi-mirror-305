# kpi_library/numeric/coefficient_variation.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericCoefficientVariation(MetricModel):
    """
    This metric computes the coefficient of variation of the numeric column.

    Example
    -------
    >>> c = NumericCoefficientVariation()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    0.5
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.coefficient_variation', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasP\
arameters': [], 'dqv_value': '0.5'}]
    >>> c.run(pd.Series([1,None,3,4,5,6,7], name='Num'))
    0.45508306023843204
    >>> c.to_dqv(pd.Series([1,None,3,4,5,6,7], name='Num'))
    [{'dqv_isMeasurementOf': 'numeric.coefficient_variation', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_h\
asParameters': [], 'dqv_value': '0.45508306023843204'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.coefficient_variation', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasP\
arameters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.coefficientVariation', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericCoefficientVariation, self).__init__(
            identifier='numeric.coefficient_variation',
            keyword='NumericCoefficientVariation',
            title='Coefficient of variation',
            definition='Coefficient of variation of the numeric data.',
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
        This method returns the coefficient of variation of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Coefficient of variation of the data.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        srs = srs.to_numpy()
        std_var = np.std(srs)
        mean_var = np.mean(srs)
        # edge cases (different behaviour)
        if mean_var == 0:
            if std_var == 0:
                # If both the mean and the standard deviation are zero, nan is returned
                return float("nan")
            # If the mean is zero and the standard deviation is nonzero, inf is returned.
            return float('inf')
        # normal cases
        return float(std_var/mean_var)
