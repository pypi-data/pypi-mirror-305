# kpi_library/categorical/outliers.py
import json
import numpy as np
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class CategoricalOutliers(MetricModel):
    """
    This metric computes the length of each entry, and obtains the number of possible outliers of those lengths.

    Example
    -------
    >>> c = CategoricalOutliers()
    >>> srs = pd.Series(['a', 'b', 'c', 'a', 'a', 'female'], name='ID')
    >>> c.run(srs)
    1
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.outliers', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', 'ddqv_hasParame\
ters': [], 'dqv_value': '1'}]
    >>> srs = pd.Series(['a', None, None, 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.outliers', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', 'ddqv_hasParame\
ters': [], 'dqv_value': '0'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'categorical.outliers', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_has\
Parameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series([123.12313, 1231.23421, 1234124.2134]))
    [{'dqv_isMeasurementOf': 'categorical.outliers', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_has\
Parameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series(["2022-03-23", "2022-03-24", "2022-03-25", "2022-03-26", "2022-03-27", "2022-03-28"]))
    [{'dqv_isMeasurementOf': 'categorical.outliers', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_has\
Parameters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'categorical.outliers', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', 'ddqv_hasParame\
ters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(CategoricalOutliers, self).__init__(
            identifier='categorical.outliers',
            keyword='CategoricalOutliers',
            title='Number of outliers',
            definition='Number of outliers in the categorical data.',
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
        Checks the data, computes the length of each entry, obtains possible outliers of those lengths and returns the
        number of outliers found.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: int, optional.
            Number of outliers found.
        """
        srs = self._check_categorical_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # prepare data
        srs = srs.to_numpy()
        v_len = np.vectorize(len)
        # compute length of each entry and frequency of each length
        data_lengths = v_len(srs)
        # compute statistics to obtain possible outliers
        stats = np.percentile(a=data_lengths, q=[25, 75])
        iqr = stats[1] - stats[0]
        upper = stats[1] + 1.5*iqr
        lower = stats[0] - 1.5*iqr
        # obtain possible outliers and return the number of outliers found
        return data_lengths[(data_lengths > upper) | (data_lengths < lower)].size
