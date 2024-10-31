# kpi_library/general/count.py
from ..model import MetricModel
import json
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import pandas as pd
from typing import Union, Optional, List, Dict


class GeneralCount(MetricModel):
    """This method computes the number of elements in each column of the dataset.

        Examples
        --------
        >>> c = GeneralCount()
        >>> c.run(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
        [{'column_name': 'ID', 'value': '4'}, {'column_name': 'Num', 'value': '4'}, {'column_name': 'Cat', 'value'\
: '3'}]
        >>> c.run(pd.Series([1, 1, 1, 1], name='num'))
        [{'column_name': 'num', 'value': '4'}]
        >>> c.run(pd.Series([1, None, 1, 1]))
        [{'column_name': '', 'value': '3'}]
        >>> c.run(pd.Series())
        >>> c.to_dqv(pd.Series())
        []
        >>> c.to_dqv(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
        [{'dqv_isMeasurementOf': 'general.count', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '4'}, {'dqv_isMeasurementOf': 'general.count', 'dqv_computedOn': 'Num', \
'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '4'}, {'dqv_isMeasurementOf': 'general.count', \
'dqv_computedOn': 'Cat', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '3'}]
        """
    def __init__(self):
        super(GeneralCount, self).__init__(
            identifier='general.count',
            keyword='GeneralCount',
            title='Count',
            definition='Number of non-null values in each column.',
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
        if results is None:
            return []
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': result['column_name'],
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
            'dqv_value': result['value']
        } for result in results]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[List[Dict[str, Union[str, int]]]]:
        """This method computes the number of null values in each column of the dataset.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the null values in the column is being processed (data).
        """
        # check dataset is not empty
        if data.empty:
            return None
        # compute column position
        count: Union[pd.DataFrame, int] = data.count()
        if isinstance(data, pd.Series):
            return [{'column_name': '' if data.name is None else data.name, 'value': str(count)}]
        return [{'column_name': str(column), 'value': str(num_values)} for column, num_values in count.items()]
