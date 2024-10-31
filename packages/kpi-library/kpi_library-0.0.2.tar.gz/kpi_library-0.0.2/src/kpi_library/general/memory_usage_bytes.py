# kpi_library/general/memory_usage_bytes.py
from ..model import MetricModel
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import json
import pandas as pd
from typing import Union, Optional, List, Dict


class GeneralMemoryUsageBytes(MetricModel):
    """This method computes the memory each column needs.

        Examples
        --------
        >>> c = GeneralMemoryUsageBytes()
        >>> c.run(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
        [{'column_name': 'Index', 'value': 128}, {'column_name': 'ID', 'value': 32}, {'column_name': 'Num', 'value': \
32}, {'column_name': 'Cat', 'value': 32}]
        >>> c.run(pd.Series([1, 1, 1, 1], name='num'))
        [{'column_name': 'num', 'value': 160}]
        >>> c.run(pd.Series([1, None, 1, 1]))
        [{'column_name': '', 'value': 160}]
        >>> c.run(pd.Series())
        >>> c.to_dqv(pd.Series())
        []
        >>> c.to_dqv(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
        [{'dqv_isMeasurementOf': 'general.memory_usage_bytes', 'dqv_computedOn': 'Index', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '128'}, {'dqv_isMeasurementOf': 'general.memory_usage_bytes', 'dqv_computedOn'\
: 'ID', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '32'}, {'dqv_isMeasurementOf': 'general.mem\
ory_usage_bytes', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '32'}, {\
'dqv_isMeasurementOf': 'general.memory_usage_bytes', 'dqv_computedOn': 'Cat', 'rdf_datatype': 'Integer', 'ddqv_hasPar\
ameters': [], 'dqv_value': '32'}]
        """
    def __init__(self):
        super(GeneralMemoryUsageBytes, self).__init__(
            identifier='general.memory_usage_bytes',
            keyword='GeneralMemoryUsageBytes',
            title='Memory usage in bytes',
            definition='Number bytes the data needs to be stored in memory.',
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
            'dqv_value': json.dumps(result['value'])
        } for result in results]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[List[Dict[str, Union[str, int]]]]:
        """This method computes the number of bytes each column needs to be stored in the memory.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the column that is being processed (data) and the bytes of
            memory that column needs to be stored.
        """
        # check dataset is not empty
        if data.empty:
            return None
        # compute the memory usage by each column and the index, and convert the result into a dictionary
        usage: Union[pd.Series, int] = data.memory_usage(index=True)
        if isinstance(data, pd.Series):
            return [{'column_name': '' if data.name is None else data.name, 'value': usage}]
        # compute the memory usage for the whole dataset (self.data)
        return [{'column_name': name, 'value': value} for name, value in usage.items()]
