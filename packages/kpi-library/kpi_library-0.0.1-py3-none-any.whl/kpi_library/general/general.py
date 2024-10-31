# kpi_library/general/general.py
import json
import pandas as pd
from visions.functional import infer_type

from typing import List, Dict, Union

from kpi_library.result_types import ResultTypes
from kpi_library.general.customset import CustomSet
from kpi_library.general_model import GeneralMethodModel


class GeneralMethods(GeneralMethodModel):
    """
    General module of methods in the quality KPI library. This module returns a list of dictionaries which contains the
    name of the processed column (`column_name`) and the value after processing a column/dataset with a method
    (`result`).

    Note
    ----
    If instead of processing a column, the method processes a dataset, the result will return a list with a single
    dictionary containing as column name `DATASET`.

    Attributes
    ----------
    data: :obj:`pandas.DataFrame` or :obj:`pandas.Series`
        Object containing the data to be processed.
    is_series: bool
        Whether the data is a pandas.DataFrame or a pandas.Series

    Parameters
    ----------
    dataset: :obj:`pandas.DataFrame` or :obj:`pandas.Series`
        Object containing the data to be processed.
    """
    MAX_SAMPLE_SIZE = 20

    # constructor, getter, and setter
    def __init__(self, dataset: Union[pd.Series, pd.DataFrame]) -> None:
        super(GeneralMethods, self).__init__(class_name='general', dataset=dataset)
        self.is_series = True if isinstance(dataset, pd.Series) else False
        self.data = dataset
        self.n_rows = self.data.shape[0]

    def to_dqv(self, method_name: str, parameters: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        This method returns the result of processing the data with the specified method in the dqv format.

        Examples
        --------
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
        >>> gm.to_dqv(method_name='position', parameters=[])
        [{'dqv_isMeasurementOf': 'general.position', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '0'}, {'dqv_isMeasurementOf': 'general.position', 'dqv_computedOn': 'Num', \
'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '1'}, {'dqv_isMeasurementOf': 'general.position', \
'dqv_computedOn': 'Cat', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '2'}]
        >>> gm.to_dqv(method_name='count', parameters=[])
        [{'dqv_isMeasurementOf': 'general.count', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '4'}, {'dqv_isMeasurementOf': 'general.count', 'dqv_computedOn': 'Num', \
'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '4'}, {'dqv_isMeasurementOf': 'general.count', \
'dqv_computedOn': 'Cat', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '3'}]
        >>> gm.to_dqv(method_name='duplicated_entries', parameters=[])
        [{'dqv_isMeasurementOf': 'general.duplicated_entries', 'dqv_computedOn': 'DATASET', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [], 'dqv_value': '2'}, {'dqv_isMeasurementOf': 'general.duplicated_entries_percent', \
'dqv_computedOn': 'DATASET', 'rdf_datatype': 'Float', 'ddqv_hasParameters': [], 'dqv_value': '50.0'}]
        >>> gm.to_dqv(method_name='completeness', parameters=[])
        [{'dqv_isMeasurementOf': 'general.completeness', 'dqv_computedOn': 'ID', 'rdf_datatype': 'Integer', 'ddqv_ha\
sParameters': [], 'dqv_value': '0'}, {'dqv_isMeasurementOf': 'general.completeness_percent', 'dqv_computedOn': 'ID',\
 'rdf_datatype': 'Float', 'ddqv_hasParameters': [], 'dqv_value': '0.0'}, {'dqv_isMeasurementOf': 'general.completene\
ss', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Integer', 'ddqv_hasParameters': [], 'dqv_value': '0'}, {'dqv_isMeasu\
rementOf': 'general.completeness_percent', 'dqv_computedOn': 'Num', 'rdf_datatype': 'Float', 'ddqv_hasParameters': \
[], 'dqv_value': '0.0'}, {'dqv_isMeasurementOf': 'general.completeness', 'dqv_computedOn': 'Cat', 'rdf_datatype': '\
Integer', 'ddqv_hasParameters': [], 'dqv_value': '1'}, {'dqv_isMeasurementOf': 'general.completeness_percent', 'dqv\
_computedOn': 'Cat', 'rdf_datatype': 'Float', 'ddqv_hasParameters': [], 'dqv_value': '25.0'}]

        Returns
        -------
        _: :obj:`list` of :obj:`dict`

        """
        try:
            values = self.get(method_name)(**self._turn_parameter_to_dictionary(parameters))
        except Exception:
            return [{
                'dqv_isMeasurementOf': f'{self._class_name}.{method_name}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': parameters,
                'dqv_value': None
            }]
        return [{
            'dqv_isMeasurementOf': f'{self._class_name}.{result["method_name"]}',
            'dqv_computedOn': result['column_name'],
            'rdf_datatype': result["data_type"],
            'ddqv_hasParameters': parameters,
            'dqv_value': result['value']
        } for result in values]

    # methods
    def position(self) -> List[Dict[str, str]]:
        """This method returns the position of each column in the dataset.

        Examples
        --------
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
        >>> gm.position()
        [{'column_name': 'ID', 'method_name': 'position', 'data_type': 'Integer', 'value': '0'}, {'column_name': 'Num',\
 'method_name': 'position', 'data_type': 'Integer', 'value': '1'}, {'column_name': 'Cat', 'method_name': 'position', \
'data_type': 'Integer', 'value': '2'}]
        >>> gm = GeneralMethods(pd.Series([1, 1, 1, 1], name='num'))
        >>> gm.position()
        [{'column_name': 'num', 'method_name': 'position', 'data_type': 'Integer', 'value': '0'}]
        >>> gm = GeneralMethods(pd.Series([1, 1, 1, 1]))
        >>> gm.position()
        [{'column_name': '', 'method_name': 'position', 'data_type': 'Integer', 'value': '0'}]

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the processed data and its position in the dataset.
        """
        columns: List[str]
        if self.is_series:
            columns = [""] if self.data.name is None else [self.data.name]
        else:
            columns = self.data.columns

        return [
            {'column_name': column, 'method_name': 'position', 'data_type': ResultTypes.INT.value,
             'value': json.dumps(index)} for index, column in enumerate(columns)]

    def count(self) -> List[Dict[str, str]]:
        """This method computes the number of elements in each column of the dataset.

        Examples
        --------
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', None, 'A']}))
        >>> gm.count()
        [{'column_name': 'ID', 'method_name': 'count', 'data_type': 'Integer', 'value': '4'}, {'column_name': 'Num', \
'method_name': 'count', 'data_type': 'Integer', 'value': '4'}, {'column_name': 'Cat', 'method_name': 'count', \
'data_type': 'Integer', 'value': '3'}]
        >>> gm = GeneralMethods(pd.Series([1, 1, 1, 1], name='num'))
        >>> gm.count()
        [{'column_name': 'num', 'method_name': 'count', 'data_type': 'Integer', 'value': '4'}]
        >>> gm = GeneralMethods(pd.Series([1, None, 1, 1]))
        >>> gm.count()
        [{'column_name': '', 'method_name': 'count', 'data_type': 'Integer', 'value': '3'}]

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the processed data and the number of values in that column
            (data).
        """
        count: Union[pd.DataFrame, int] = self.data.count()
        if self.is_series:
            return [{'column_name': '' if self.data.name is None else self.data.name,
                     'method_name': 'count', 'data_type': ResultTypes.INT.value, 'value': str(count)}]

        return [{
            'column_name': str(column), 'method_name': 'count', 'data_type': ResultTypes.INT.value,
            'value': str(num_values)
        } for column, num_values in count.items()]

    def num_rows(self) -> List[Dict[str, str]]:
        """
        This method returns the number of rows in the data.

        Examples
        --------
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
        >>> gm.num_rows()
        [{'column_name': 'DATASET', 'method_name': 'num_rows', 'data_type': 'Integer', 'value': '4'}]
        >>> gm = GeneralMethods(pd.Series([1, 1, 1, 1], name='num'))
        >>> gm.num_rows()
        [{'column_name': 'DATASET', 'method_name': 'num_rows', 'data_type': 'Integer', 'value': '4'}]

        Return
        ------
        _: :obj:`dict`
            Dictionary containing two elements, the column name (`column_name`, it refers to the dataset, so it always
            contains the same value, 'DATASET') and the number of rows (`result`).
        """
        return [{'column_name': 'DATASET', 'method_name': 'num_rows', 'data_type': ResultTypes.INT.value,
                 'value': str(self.data.shape[0])}]

    def num_columns(self) -> List[Dict[str, str]]:
        """
        Returns the number of columns in the data.

        Examples
        --------
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
        >>> gm.num_columns()
        [{'column_name': 'DATASET', 'method_name': 'num_columns', 'data_type': 'Integer', 'value': 3}]
        >>> gm = GeneralMethods(pd.Series([1, 1, 1, 1], name='num'))
        >>> gm.num_columns()
        [{'column_name': 'DATASET', 'method_name': 'num_columns', 'data_type': 'Integer', 'value': 1}]

        Return
        ------
        _: :obj:`dict`
            Dictionary containing two elements, the column name (`column_name`, it refers to the dataset, so it always
            contains the same value, 'DATASET') and the number of columns (`result`).
        """
        return [{'column_name': 'DATASET', 'method_name': 'num_columns', 'data_type': ResultTypes.INT.value,
                 'value': 1 if self.is_series else self.data.shape[1]}]

    def duplicated_entries(self) -> List[Dict[str, str]]:
        """
        This method returns the number of duplicated entries in the data. The result can be an integer (number of
        entries) or a float (percentage of duplicated entries in the data).

        Examples
        --------
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 1, 1, 1], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
        >>> gm.duplicated_entries()
        [{'column_name': 'DATASET', 'method_name': 'duplicated_entries', 'data_type': 'Integer', 'value': '3'}, \
{'column_name': 'DATASET', 'method_name': 'duplicated_entries_percent', 'data_type': 'Float', 'value': '75.0'}]
        >>> gm = GeneralMethods(pd.DataFrame(\
        {'ID': [1, 2, 3, 3], 'Num': [0.2, 1.5, 4.6, 4.6], 'Cat': ['A', 'B', 'C', 'C']}))
        >>> gm.duplicated_entries()
        [{'column_name': 'DATASET', 'method_name': 'duplicated_entries', 'data_type': 'Integer', 'value': '1'}, \
{'column_name': 'DATASET', 'method_name': 'duplicated_entries_percent', 'data_type': 'Float', 'value': '25.0'}]
        >>> gm = GeneralMethods(pd.DataFrame({'ID': [1, 2, 3, 4], 'Num': [2, 2, 2, 2], 'Cat': ['A', 'A', 'A', 'A']}))
        >>> gm.duplicated_entries()
        [{'column_name': 'DATASET', 'method_name': 'duplicated_entries', 'data_type': 'Integer', 'value': '0'}, \
{'column_name': 'DATASET', 'method_name': 'duplicated_entries_percent', 'data_type': 'Float', 'value': '0.0'}]
        >>> gm = GeneralMethods(pd.Series([1, 2, 4, 4]))
        >>> gm.duplicated_entries()
        [{'column_name': 'DATASET', 'method_name': 'duplicated_entries', 'data_type': 'Integer', 'value': '1'}, \
{'column_name': 'DATASET', 'method_name': 'duplicated_entries_percent', 'data_type': 'Float', 'value': '25.0'}]

        Return
        ------
        _: :obj:`dict`
            Dictionary containing two elements, the column name (`column_name`, it refers to the dataset, so it always
            contains the same value, 'DATASET') and the number or percentage of duplicated entries (`result`).
        """
        # get the index of those rows which are duplicated
        indices: pd.Series = self.data.duplicated()
        # get the number of duplicated entries
        num_dupl: int = int(indices.sum())
        # return the result
        return [
            {'column_name': 'DATASET', 'method_name': 'duplicated_entries', 'data_type': ResultTypes.INT.value,
             'value': str(num_dupl)},
            {'column_name': 'DATASET', 'method_name': 'duplicated_entries_percent',
             'data_type': ResultTypes.FLOAT.value, 'value': str(round((num_dupl/self.n_rows)*100, 2))}
        ]

    def completeness(self) -> List[Dict[str, str]]:
        """
        This method returns the number of empty values (null values) per column.

        Example
        -------
        >>> gm = GeneralMethods(\
        pd.DataFrame({'ID': [1, 2, None, 4], 'Num': [None, 2, 0.5, 1.5], 'Cat': ['A', 'B', 'C', 'D']}))
        >>> gm.completeness()
        [{'column_name': 'ID', 'method_name': 'completeness', 'data_type': 'Integer', 'value': '1'}, \
{'column_name': 'ID', 'method_name': 'completeness_percent', 'data_type': 'Float', 'value': '25.0'}, \
{'column_name': 'Num', 'method_name': 'completeness', 'data_type': 'Integer', 'value': '1'}, \
{'column_name': 'Num', 'method_name': 'completeness_percent', 'data_type': 'Float', 'value': '25.0'}, \
{'column_name': 'Cat', 'method_name': 'completeness', 'data_type': 'Integer', 'value': '0'}, \
{'column_name': 'Cat', 'method_name': 'completeness_percent', 'data_type': 'Float', 'value': '0.0'}]
        >>> gm = GeneralMethods(pd.Series([1, 2, None, 4], name='Num'))
        >>> gm.completeness()
        [{'column_name': 'Num', 'method_name': 'completeness', 'data_type': 'Integer', 'value': '1'}, \
{'column_name': 'Num', 'method_name': 'completeness_percent', 'data_type': 'Float', 'value': '25.0'}]
        >>> gm = GeneralMethods(pd.Series([1, 2, None, 4]))
        >>> gm.completeness()
        [{'column_name': '', 'method_name': 'completeness', 'data_type': 'Integer', 'value': '1'}, \
{'column_name': '', 'method_name': 'completeness_percent', 'data_type': 'Float', 'value': '25.0'}]

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the missing value information of each column, i.e., the number or percentage
            of missing values per column.
        """
        # compute the number of missing values per column
        num_miss: Union[pd.Series, int] = self.data.isna().sum()
        return self.__get_result(num_miss, method_name='completeness')

    def __get_result(self, info: Union[pd.Series, int], method_name: str) -> List[Dict[str, str]]:
        """
        This method returns a list of dictionaries containing the normalized data given as parameter.

        Parameters
        ----------
        info: :obj:`pandas.Series` or int
            Statistics computed in the dataset.
        method_name: str
            Name of the method that has been implemented.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the name of the processed data (`column_name`) and the normalized statistics
            (`result`).
        """
        if self.is_series:
            column_name: str = '' if self.data.name is None else self.data.name
            return [
                {'column_name': column_name, 'method_name': method_name,
                 'data_type': ResultTypes.INT.value, 'value': str(info)},
                {'column_name': column_name, 'method_name': f'{method_name}_percent',
                 'data_type': ResultTypes.FLOAT.value, 'value': str(round((info/self.n_rows)*100, 5))}
            ]

        result: List[Dict[str, Union[str, float, int]]] = []
        for column_name, miss in info.items():
            result += [
                {'column_name': column_name, 'method_name': method_name,
                 'data_type': ResultTypes.INT.value, 'value': str(miss)},
                {'column_name': column_name, 'method_name': f'{method_name}_percent',
                 'data_type': ResultTypes.FLOAT.value, 'value': str(round((miss/self.n_rows)*100, 2))}
            ]
        return result

    def unique_entries(self) -> List[Dict[str, str]]:
        """
        Computes the number of different elements in each column (feature) and its percentage considering all the
        values.

        Examples
        --------
        >>> gm = GeneralMethods(\
        pd.DataFrame({'ID': [1, 2, 3, 4], 'Num': [0.2, 1.5, 4.6, 3.7], 'Cat': ['A', 'B', 'B', 'A']}))
        >>> gm.unique_entries()
        [{'column_name': 'ID', 'method_name': 'unique_entries', 'data_type': 'Integer', 'value': '4'}, \
{'column_name': 'ID', 'method_name': 'unique_entries_percent', 'data_type': 'Float', 'value': '100.0'}, \
{'column_name': 'Num', 'method_name': 'unique_entries', 'data_type': 'Integer', 'value': '4'}, \
{'column_name': 'Num', 'method_name': 'unique_entries_percent', 'data_type': 'Float', 'value': '100.0'}, \
{'column_name': 'Cat', 'method_name': 'unique_entries', 'data_type': 'Integer', 'value': '2'}, \
{'column_name': 'Cat', 'method_name': 'unique_entries_percent', 'data_type': 'Float', 'value': '50.0'}]
        >>> gm = GeneralMethods(pd.Series([0.2, 1.5, 4.6, 3.7, 0.2], name='num'))
        >>> gm.unique_entries()
        [{'column_name': 'num', 'method_name': 'unique_entries', 'data_type': 'Integer', 'value': '4'}, \
{'column_name': 'num', 'method_name': 'unique_entries_percent', 'data_type': 'Float', 'value': '80.0'}]
        >>> gm = GeneralMethods(pd.Series([0.2, 1.5, 4.6, 3.7]))
        >>> gm.unique_entries()
        [{'column_name': '', 'method_name': 'unique_entries', 'data_type': 'Integer', 'value': '4'}, \
{'column_name': '', 'method_name': 'unique_entries_percent', 'data_type': 'Float', 'value': '100.0'}]

        Return
        ------
        _: :obj:`list`
            Dictionary containing the information (number and percentage) related with the unique values per column.
        """
        # get the number of unique values of each column
        num_unique_entries: Union[pd.Series, int] = self.data.nunique()
        return self.__get_result(num_unique_entries, method_name='unique_entries')

    def data_types(self) -> List[Dict[str, str]]:
        """
        Obtains the data types of each column in df.

        Example
        -------
        >>> gm = GeneralMethods(pd.DataFrame(\
        {'ID': [1, 2, 3, 4], 'Num': [0.2, 1.5, 4.6, 3.7], 'Cat': ['A', 'B', 'B', 'A']}))
        >>> gm.data_types()
        [{'column_name': 'ID', 'method_name': 'data_types', 'data_type': 'String', 'value': 'Integer'}, \
{'column_name': 'Num', 'method_name': 'data_types', 'data_type': 'String', 'value': 'Float'}, \
{'column_name': 'Cat', 'method_name': 'data_types', 'data_type': 'String', 'value': 'String'}]
        >>> gm = GeneralMethods(pd.DataFrame(\
        {'Date': ['2000/01/01', '2000/01/02', '2000/01/03', '2000/01/04'], 'Time': ['12:01:02', '12:02:02', '12:03:02',\
 '12:04:02'], 'DateTime': ['2000-01-01 00:01:00', '2000-01-02 00:01:00', '2000-01-03 00:01:00', \
'2000-01-04 00:01:00']}))
        >>> gm.data_types()
        [{'column_name': 'Date', 'method_name': 'data_types', 'data_type': 'String', 'value': 'Date'}, \
{'column_name': 'Time', 'method_name': 'data_types', 'data_type': 'String', 'value': 'DateTime'}, \
{'column_name': 'DateTime', 'method_name': 'data_types', 'data_type': 'String', 'value': 'DateTime'}]
        >>> gm = GeneralMethods(pd.Series(\
        ['2000/01/01', '2000/01/02', '2000/01/03', '2000/01/04'], name='Date'))
        >>> gm.data_types()
        [{'column_name': 'Date', 'method_name': 'data_types', 'data_type': 'String', 'value': 'Date'}]

        Return
        ------
        _: List[Dict[str, str]]
            List of dictionaries containing the column name (`column_name`), and its type (`type`).
        """
        # get model to infer the data types of each column
        typeset = CustomSet()
        # infer the data type
        if self.is_series:
            return [self.__infer_data_types(srs=self.data, typeset=typeset,
                                            column_name='' if self.data.name is None else self.data.name)]

        return [self.__infer_data_types(
            self.data[column_name], typeset=typeset, column_name=column_name) for column_name in self.data]

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
        return {'column_name': column_name, 'method_name': 'data_types', 'data_type': ResultTypes.STRING.value,
                'value': str(tt)}

    def memory_usage_bytes(self) -> List[Dict[str, str]]:
        """
        Return the memory usage of each column and the entire dataset in bytes

        Examples
        --------
        >>> gm = GeneralMethods(\
        pd.DataFrame({'ID': [1, 2, 3, 4], 'Num': [0.2, 1.5, 4.6, 3.7], 'Cat': ['A', 'B', 'B', 'A']}))
        >>> gm.memory_usage_bytes()
        [{'column_name': 'Index', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 128}, \
{'column_name': 'ID', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 32}, \
{'column_name': 'Num', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 32}, \
{'column_name': 'Cat', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 32}]
        >>> gm = GeneralMethods(pd.Series([0.2, 1.5, 4.6, 3.7], name='Num'))
        >>> gm.memory_usage_bytes()
        [{'column_name': 'Num', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 160}]
        >>> gm = GeneralMethods(pd.DataFrame({'num': [0.2, 1.5, 4.6, 3.7]}))
        >>> gm.memory_usage_bytes()
        [{'column_name': 'Index', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 128}, \
{'column_name': 'num', 'method_name': 'memory_usage_bytes', 'data_type': 'Integer', 'value': 32}]

        Return
        ------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the number of bytes used by the dataset or each feature.
        """
        # compute the memory usage by each column and the index, and convert the result into a dictionary
        usage: Union[pd.Series, int] = self.data.memory_usage(index=True)
        res: List[Dict[str, Union[str, int]]]
        if self.is_series:
            res = [{'column_name': '' if self.data.name is None else self.data.name,
                    'method_name': 'memory_usage_bytes', 'data_type': ResultTypes.INT.value, 'value': usage}]
        else:
            # compute the memory usage for the whole dataset (self.data)
            res = [{'column_name': name, 'method_name': 'memory_usage_bytes', 'data_type': ResultTypes.INT.value,
                    'value': value} for name, value in usage.items()]
        return res
