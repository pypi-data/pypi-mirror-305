# kpi_library/categorical/mode.py
import json
import pandas as pd

from typing import Optional
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class CategoricalMode(MetricModel):
    """
    This metric gets the most frequent category in the categorical column.

    Example
    -------
    >>> c = CategoricalMode()
    >>> srs = pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    'a'
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.mode', 'dqv_computedOn': 'ID', 'rdf_datatype': 'String', 'ddqv_hasParam\
eters': [], 'dqv_value': 'a'}]
    >>> srs = pd.Series(['a', None, None, 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    'a'
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.mode', 'dqv_computedOn': 'ID', 'rdf_datatype': 'String', 'ddqv_hasParam\
eters': [], 'dqv_value': 'a'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'categorical.mode', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series([123.12313, 1231.23421, 1234124.2134]))
    [{'dqv_isMeasurementOf': 'categorical.mode', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series(["2022-03-23", "2022-03-24", "2022-03-25", "2022-03-26", "2022-03-27", "2022-03-28"]))
    [{'dqv_isMeasurementOf': 'categorical.mode', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'categorical.mode', 'dqv_computedOn': '', 'rdf_datatype': 'String', 'ddqv_hasPa\
rameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(CategoricalMode, self).__init__(
            identifier='categorical.mode',
            keyword='CategoricalMode',
            title='Most frequent category',
            definition='Most frequent category of the categorical data.',
            expected_data_type=str(ResultTypes.STRING.value),
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
            'dqv_value': result if result is not None else json.dumps(None)
        }]

    def run(self, data: pd.Series, **kwargs) -> Optional[str]:
        """
        This method returns the most frequent category of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: str
            Most frequent category.
        """
        srs = self._check_categorical_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        result = srs.value_counts(sort=True)
        return str(result.index[0])
