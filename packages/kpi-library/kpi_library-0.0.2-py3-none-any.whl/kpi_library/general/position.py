# kpi_library/general/position.py
from ..model import MetricModel
import json
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import pandas as pd
from typing import Union, List


class GeneralPosition(MetricModel):
    """
    This metric returns the position of each column in the dataset.

    Examples
    --------
    >>> gm = GeneralPosition()
    >>> gm.run(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
    [{'column_name': 'ID', 'value': '0'}, {'column_name': 'Num', 'value': '1'}, {'column_name': 'Cat', 'value': '2'}]
    >>> gm.run(pd.Series([1, 1, 1, 1], name='num'))
    [{'column_name': 'num', 'value': '0'}]
    >>> gm.run(pd.Series([1, 1, 1, 1]))
    [{'column_name': '', 'value': '0'}]
    >>> gm.to_dqv(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
    [{'dqv_isMeasurementOf': 'general.position', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '0'}, {'dqv_isMeasurementOf': 'general.position', 'dqv_computedOn': 'Num', \
'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '1'}, {'dqv_isMeasurementOf': 'general.position', \
'dqv_computedOn': 'Cat', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '2'}]

    Returns
    -------
    _: :obj:`list` of :obj:`dict`
        List of dictionaries containing the name of the processed data and its position in the dataset.
    """
    def __init__(self):
        super(GeneralPosition, self).__init__(
            identifier='general.position',
            keyword='GeneralPosition',
            title='Position',
            definition='Position of the column in the dataset.',
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
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': result['column_name'],
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
            'dqv_value': result['value']
        } for result in results]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs):
        """"""
        # check dataset is not empty
        if data.empty:
            return None
        # compute column position
        columns: List[str]
        if isinstance(data, pd.Series):
            columns = [""] if data.name is None else [data.name]
        else:
            columns = data.columns
        return [{'column_name': column, 'value': json.dumps(index)} for index, column in enumerate(columns)]
