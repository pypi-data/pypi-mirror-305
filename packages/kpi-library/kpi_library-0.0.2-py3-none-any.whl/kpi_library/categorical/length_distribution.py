# kpi_library/categorical/length_distribution.py
import json
import numpy as np
import pandas as pd

from typing import List, Dict
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class CategoricalLengthDistribution(MetricModel):
    """
    This metric gets the length distribution in characters of the categorical data given as parameter.

    Example
    -------
    >>> c = CategoricalLengthDistribution()
    >>> srs = pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    [{'item': 1, 'frequency': 6}]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.length_distribution', 'dqv_computedOn': 'ID', 'rdf_datatype': 'List<Map<Stri\
ng,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"item": 1, "frequency": 6}]'}]
    >>> srs = pd.Series(['a', None, None, 'a', 'a', 'b'], name='ID')
    >>> c.run(srs)
    [{'item': 1, 'frequency': 4}]
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'categorical.length_distribution', 'dqv_computedOn': 'ID', 'rdf_datatype': 'List<Map<Stri\
ng,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"item": 1, "frequency": 4}]'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'categorical.length_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_h\
asParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series([123.12313, 1231.23421, 1234124.2134]))
    [{'dqv_isMeasurementOf': 'categorical.length_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_h\
asParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(pd.Series(["2022-03-23", "2022-03-24", "2022-03-25", "2022-03-26", "2022-03-27", "2022-03-28"]))
    [{'dqv_isMeasurementOf': 'categorical.length_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_h\
asParameters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    []
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'categorical.length_distribution', 'dqv_computedOn': '', 'rdf_datatype': 'List<Map<String,\
String>>', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(CategoricalLengthDistribution, self).__init__(
            identifier='categorical.length_distribution',
            keyword='CategoricalLengthDistribution',
            title='Length distribution',
            definition='Length distribution in characters of the categorical data.',
            expected_data_type=str(ResultTypes.DISTRIBUTION_INT.value),
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

    def run(self, data: pd.Series, **kwargs) -> List[Dict[str, int]]:
        """
        This method returns the length distribution in characters of the data given as parameter.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            Length distribution.
        """
        srs = self._check_categorical_data(data)
        # check if dataset is empty
        if srs.empty:
            return []
        # prepare data
        srs = srs.to_numpy()
        v_len = np.vectorize(len)
        # compute length of each entry and frequency of each length
        data_lengths = v_len(srs)
        uniques, counts = np.unique(data_lengths, return_counts=True)
        return [{"item": int(item), "frequency": int(frequency)} for item, frequency in zip(uniques, counts)]
