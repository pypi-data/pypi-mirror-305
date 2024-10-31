# kpi_library/general/completeness.py
from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import json
import pandas as pd
from typing import Union, Optional, List, Dict


class GeneralCompleteness(MetricModel):
    """
    This method returns the number of empty values (null values) per column.

    Example
    -------
    >>> c = GeneralCompleteness()
    >>> c.run(pd.DataFrame({'ID': [1, 2, None, 4], 'Num': [None, 2, 0.5, 1.5], 'Cat': ['A', 'B', 'C', 'D']}))
    [{'column_name': 'ID', 'value': 1}, {'column_name': 'Num', 'value': 1}, {'column_name': 'Cat', 'value': 0}]
    >>> c.run(pd.Series([1, 2, None, 4], name='Num'))
    [{'column_name': 'Num', 'value': 1}]
    >>> c.run(pd.Series([1, 2, None, 4]))
    [{'column_name': '', 'value': 1}]
    >>> c.run(pd.Series())
    >>> c.to_dqv(pd.Series(pd.Series([1, 2, None, 4], name='Num')))
    [{'dqv_isMeasurementOf': 'general.completeness', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Integer', 'ddqv_hasParam\
eters': [], 'dqv_value': '1'}]
    >>> c.to_dqv(pd.Series())
    []
    """
    def __init__(self):
        super(GeneralCompleteness, self).__init__(
            identifier='general.completeness',
            keyword='GeneralCompleteness',
            title='Completeness',
            definition='Number of null values in each column.',
            expected_data_type=str(ResultTypes.INT.value),
            dimension='profile',
            category='inherent'
        )

    def to_dqv(self, data: Union[pd.Series, pd.DataFrame], **kwargs):
        """"""
        try:
            results = self.run(data, **kwargs)
        except EmptyDatasetError:
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': [],
                'dqv_value': json.dumps(None)
            }]
        # if data empty
        if results is None:
            return []
        # data not empty
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': result['column_name'],
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
            'dqv_value': json.dumps(int(result['value']))
        } for result in results]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[List[Dict[str, Union[str, int]]]]:
        """This method computes the number of elements in each column of the dataset.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the processed data and the number of values in that column
            (data).
        """
        # check dataset is not empty
        if data.empty:
            return None
        # compute column position
        num_miss: Union[pd.Series, int] = data.isna().sum()
        # if data is a pandas.Series
        if isinstance(data, pd.Series):
            column_name: str = '' if data.name is None else data.name
            return [{'column_name': column_name, 'value': num_miss}]
        # if data is pandas.DataFrame
        return [{'column_name': column_name, 'value': miss} for column_name, miss in num_miss.items()]
