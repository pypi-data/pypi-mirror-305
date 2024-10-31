# kpi_library/categorical/mode_frequency_percent.py
import json
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class CategoricalModeFrequencyPercent(MetricModel):
    """
    This metric gets the percentage of occurrence of the most frequent category in the categorical column.

    Example
    -------
    >>> c = CategoricalModeFrequencyPercent()
    >>> srs = pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    50.0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.mode_frequency_percent', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '50.0'}]
    >>> srs = pd.Series(['a', None, None, 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    50.0
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.mode_frequency_percent', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '50.0'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'categorical.mode_frequency_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'dd\
qv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series([123.12313, 1231.23421, 1234124.2134]))
    [{'dqv_isMeasurementOf': 'categorical.mode_frequency_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'dd\
qv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series(["2022-03-23", "2022-03-24", "2022-03-25", "2022-03-26", "2022-03-27", "2022-03-28"]))
    [{'dqv_isMeasurementOf': 'categorical.mode_frequency_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'dd\
qv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'categorical.mode_frequency_percent', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(CategoricalModeFrequencyPercent, self).__init__(
            identifier='categorical.mode_frequency_percent',
            keyword='CategoricalModeFrequencyPercent',
            title='Percentage of occurrence of the most frequent category',
            definition='Percentage of occurrence of the most frequent category of the categorical data.',
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

    def run(self, data: pd.Series, **kwargs) -> Optional[float]:
        """
        This method returns the percentage of occurrence of the most frequent category of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Percentage of occurrence of the most frequent category.
        """
        srs = self._check_categorical_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        result = srs.value_counts(sort=True)
        return float(round((result.iloc[0]/data.shape[0])*100, 2))
