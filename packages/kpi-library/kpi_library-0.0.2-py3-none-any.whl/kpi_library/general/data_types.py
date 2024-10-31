# kpi_library/general/data_types.py
from ..model import MetricModel
from ..custom_metric import CustomSet
from ..errors import EmptyDatasetError
from ..result_types import ResultTypes
# typing
import json
import pandas as pd
from visions.functional import infer_type
from typing import Union, Optional, List, Dict


class GeneralDataTypes(MetricModel):
    """
    This method returns the type of the data of each column.

    Example
    -------
    >>> c = GeneralDataTypes()
    >>> c.run(pd.DataFrame({'ID': [1, 2, 2, 4], 'Num': [1, 2, 0.5, 1.5], 'Cat': ['A', 'B', 'C', 'C']}))
    [{'column_name': 'ID', 'value': 'Integer'}, {'column_name': 'Num', 'value': 'Float'}, {'column_name': 'Cat', \
'value': 'String'}]
    >>> c.run(pd.Series([1, 2, None, 4], name='Num'))
    [{'column_name': 'Num', 'value': 'Integer'}]
    >>> c.run(pd.Series([1, 2, None, 4.5]))
    [{'column_name': '', 'value': 'Float'}]
    >>> c.run(pd.Series())
    >>> c.to_dqv(pd.Series(pd.Series([1, 1, 1, 2], name='Num')))
    [{'dqv_isMeasurementOf': 'general.data_types', 'dqv_computedOn': 'Num', 'rdf_datatype': 'String', 'ddqv_hasPar\
ameters': [], 'dqv_value': 'Integer'}]
    >>> c.to_dqv(pd.Series())
    []
    """
    MAX_SAMPLE_SIZE: int = 5

    def __init__(self):
        super(GeneralDataTypes, self).__init__(
            identifier='general.data_types',
            keyword='GeneralDataTypes',
            title='Data types',
            definition='Type of the data of each column.',
            expected_data_type=str(ResultTypes.STRING.value),
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
            'dqv_value': str(result['value'])
        } for result in results]

    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs) -> Optional[List[Dict[str, str]]]:
        """This method infers the data types of each column.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the processed data and the data type of each column.
        """
        # check dataset is not empty
        if data.empty:
            return None
        # get model to infer the data types of each column
        typeset = CustomSet()
        # infer the data type
        if isinstance(data, pd.Series):
            return [
                self.__infer_data_types(srs=data, typeset=typeset, column_name="" if data.name is None else data.name)]
        return [
            self.__infer_data_types(data[column_name], typeset=typeset, column_name=column_name) for column_name in data
        ]

    def __infer_data_types(
            self, srs: pd.Series, typeset: "CustomSet", column_name: str) -> Dict[str, str]:
        """
        Infer the data type of the data in srs.

        Parameters
        ----------
        srs: :obj:`pandas.Series`
            Data in which the computations are done
        column_name: str
            Name of the data that is going to be processed.
        typeset: :obj:`CustomSet`
            Object of the library `visions` which helps to infer the data types of each column.

        Return
        ------
        _: dict
            Dictionary containing the name of the column ('column_name'), its type ('type') and its position
            ('position') in the dataset.
        """
        # drop nan values
        srs.dropna(inplace=True)
        # infer data type (get a sample for that)
        tt = str(infer_type(srs.iloc[:self.MAX_SAMPLE_SIZE] if srs.size > self.MAX_SAMPLE_SIZE else srs, typeset))
        # check if the datatype could not be inferred
        if tt in ['General', 'Object'] and srs.shape[0] > self.MAX_SAMPLE_SIZE:
            for index in range(1, 3):
                tt = str(infer_type(srs.iloc[index*self.MAX_SAMPLE_SIZE:(index+1)*self.MAX_SAMPLE_SIZE], typeset))
                if tt not in ['General', 'Object']:
                    break
        # return
        return {'column_name': column_name, 'value': str(tt)}
