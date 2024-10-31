# kpi_library/general/completeness_percent.py
from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import json
import pandas as pd
from typing import Union, Optional, List, Dict


class GeneralCompletenessPercent(MetricModel):
    """
    This method returns the percentage of empty values (null values) per column.

    Example
    -------
    >>> c = GeneralCompletenessPercent()
    >>> c.run(pd.DataFrame({'ID': [1, 2, None, 4], 'Num': [None, 2, 0.5, 1.5], 'Cat': ['A', 'B', 'C', 'D']}))
    [{'column_name': 'ID', 'value': 25.0}, {'column_name': 'Num', 'value': 25.0}, {'column_name': 'Cat', 'value': 0.0}]
    >>> c.run(pd.Series([1, 2, None, 4], name='Num'))
    [{'column_name': 'Num', 'value': 25.0}]
    >>> c.run(pd.Series([1, 2, None, 4]))
    [{'column_name': '', 'value': 25.0}]
    >>> c.run(pd.Series())
    >>> c.to_dqv(pd.Series(pd.Series([1, 2, None, 4], name='Num')))
    [{'dqv_isMeasurementOf': 'general.completeness_percent', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_\
hasParameters': [], 'dqv_value': '25.0'}]
    >>> c.to_dqv(pd.Series())
    []
    """
    def __init__(self):
        super(GeneralCompletenessPercent, self).__init__(
            identifier='general.completeness_percent',
            keyword='GeneralCompletenessPercent',
            title='Completeness',
            definition='Percentage of null values in each column.',
            expected_data_type=str(ResultTypes.FLOAT.value),
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
            'dqv_value': json.dumps(float(result['value']))
        } for result in results]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[List[Dict[str, Union[str, float]]]]:
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
        num_rows: int = data.shape[0]
        num_miss: Union[pd.Series, int] = data.isna().sum()
        # if data is a pandas.Series
        if isinstance(data, pd.Series):
            column_name: str = '' if data.name is None else data.name
            return [{'column_name': column_name, 'value': round((num_miss/num_rows)*100, 2)}]
        # if data is pandas.DataFrame
        return [{
            'column_name': column_name, 'value': round((miss/num_rows)*100, 2)
        } for column_name, miss in num_miss.items()]
