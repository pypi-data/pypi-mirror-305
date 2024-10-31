# kpi_library/numeric/outliers_percent.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericOutliersPercent(MetricModel):
    """
    This metric returns the percentage of outliers in the numeric data.

    Example
    -------
    >>> c = NumericOutliersPercent()
    >>> c.run(pd.Series([1,2,3,4,5,6,7]))
    0.0
    >>> c.to_dqv(pd.Series([1,2,3,4,5,6,7,100]))
    [{'dqv_isMeasurementOf': 'numeric.outliers_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_has\
Parameters': [], 'dqv_value': '12.5'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.outliers_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.outliers_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Float', 'ddqv_ha\
sParameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericOutliersPercent, self).__init__(
            identifier='numeric.outliers_percent',
            keyword='NumericOutliersPercent',
            title='Outliers',
            definition='Number of outliers in the data.',
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
        This method returns the percentage of outliers in the data.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of outliers.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # obtain statistics
        srs = srs.to_numpy()
        statistics = np.percentile(a=srs, q=[25, 75])
        # get limits
        iqr_stat = statistics[1] - statistics[0]
        upper = statistics[1] + 1.5 * iqr_stat
        lower = statistics[0] - 1.5 * iqr_stat
        # return the element of the box plot
        return float(round((len(srs[(srs > upper) | (srs < lower)].tolist())/data.shape[0])*100, 2))
