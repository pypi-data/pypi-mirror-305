# kpi_library/general/unique_entries.py
from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import json
import pandas as pd
from typing import Union, Optional, List, Dict


class GeneralUniqueEntries(MetricModel):
    """
    This method returns the number of different values in the column.

    Example
    -------
    >>> c = GeneralUniqueEntries()
    >>> c.run(pd.DataFrame({'ID': [1, 2, 2, 4], 'Num': [1, 2, 0.5, 1.5], 'Cat': ['A', 'B', 'C', 'C']}))
    [{'column_name': 'ID', 'value': 3}, {'column_name': 'Num', 'value': 4}, {'column_name': 'Cat', 'value': 3}]
    >>> c.run(pd.Series([1, 2, None, 4], name='Num'))
    [{'column_name': 'Num', 'value': 3}]
    >>> c.run(pd.Series([1, 2, None, 4]))
    [{'column_name': '', 'value': 3}]
    >>> c.run(pd.Series())
    >>> c.to_dqv(pd.Series(pd.Series([1, 1, 1, 2], name='Num')))
    [{'dqv_isMeasurementOf': 'general.unique_entries', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Integer', 'ddqv_hasPar\
ameters': [], 'dqv_value': '2'}]
    >>> c.to_dqv(pd.Series())
    []
    """
    def __init__(self):
        super(GeneralUniqueEntries, self).__init__(
            identifier='general.unique_entries',
            keyword='GeneralUniqueEntries',
            title='Unique entries',
            definition='Number of different values in each column.',
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
        """This method computes the number of different elements in each column of the dataset.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the processed data and the number of different values in that
            column (data).
        """
        # check dataset is not empty
        if data.empty:
            return None
        # get the number of unique values of each column
        num_unique_entries: Union[pd.Series, int] = data.nunique()
        # if data is a pandas.Series
        if isinstance(data, pd.Series):
            column_name: str = '' if data.name is None else data.name
            return [{'column_name': column_name, 'value': num_unique_entries}]
        # if data is pandas.DataFrame
        return [{'column_name': column_name, 'value': miss} for column_name, miss in num_unique_entries.items()]
