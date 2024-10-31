# kpi_library/uni_variable.py
import json
import pandas as pd
from typing import Union, List, Dict, Optional

from .errors import DatasetFormatError
from .general_model import GeneralMethodModel


class OneVarMethods(GeneralMethodModel):
    """
    Structure of the objects in the modules which process a column or the whole table (regarding the data type of each
    column, i.e., the general profiler module).

    Attributes
    ----------
    data: :obj:`pandas.DataFrame` or :obj:`pandas.Series`
        Object containing the data to be processed.
    _name: str
        Name of the column to process.
    _n_rows: int
        Number of rows before processing the data.

    Parameters
    ----------
    class_name: str
        Name of the class that has been implemented.
    dataset: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
        Pandas object containing the data to be processed.
    """
    _name: str
    _n_rows: int

    @property
    def n_rows(self) -> int:
        """:int: Variable containing the number of rows before processing the data."""
        return self._n_rows

    @property
    def name(self) -> str:
        """:str: Name of the data that is going to be processed."""
        return self._name

    def __init__(self, class_name: str, dataset: Union[pd.Series, pd.DataFrame], feature_one: Optional[str] = None):
        super(OneVarMethods, self).__init__(class_name=class_name, dataset=dataset)
        # check if data has a correct format (it is a pandas.Series object)
        if isinstance(dataset, pd.DataFrame):
            if dataset.shape[1] == 1:
                self.data = dataset.iloc[:, 0]
            elif feature_one is not None:
                self.data = dataset[feature_one]
            else:
                raise DatasetFormatError(f'The data should contain only one column, but it contains {dataset.shape[1]} '
                                         'columns.', code=400)
        else:
            self.data = dataset
        # get the other attributes
        self._name = '' if dataset.name is None else dataset.name
        self._n_rows = self.data.shape[0]

    def to_dqv(self, method_name: str, parameters: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Examples
        --------
        >>> from kpi_library import TextMethods
        >>> tm = TextMethods(pd.Series(["how are you", "I like to eat pasta.", None, "I don't know how to do it", \
        "Please. Help me."], name='text'))
        >>> tm.to_dqv(method_name='distribution_less_frequent_elements', parameters=[{'parameter_name': 'num_items', \
        'value': 3}, {'parameter_name': 'tokenization', 'value': True}])
        [{'dqv_isMeasurementOf': 'text.distribution_less_frequent_elements', 'dqv_computedOn': 'text', 'rdf_datatype': \
'List<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': 3}, {'parameter_name': \
'tokenization', 'value': True}], 'dqv_value': '[{"item": "are", "frequency": 1}, {"item": "you", "frequency": 1}, {\
"item": "like", "frequency": 1}]'}, {'dqv_isMeasurementOf': 'text.distribution_less_frequent_elements_percent', \
'dqv_computedOn': 'text', 'rdf_datatype': 'List<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': \
'num_items', 'value': 3}, {'parameter_name': 'tokenization', 'value': True}], 'dqv_value': '[{"item": "are", \
"frequency": 0.05263}, {"item": "you", "frequency": 0.05263}, {"item": "like", "frequency": 0.05263}]'}]
        >>> tm.to_dqv(method_name='distribution_most_frequent_elements', parameters=[{'parameter_name': 'num_items', \
        'value': 3}, {'parameter_name': 'tokenization', 'value': True}, {'parameter_name': 'stopwords_removal', \
        'value': False}, {'parameter_name': 'language', 'value': 'english'}])
        [{'dqv_isMeasurementOf': 'text.distribution_most_frequent_elements', 'dqv_computedOn': 'text', 'rdf_datatype': \
'List<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': 3}, {'parameter_name': \
'tokenization', 'value': True}, {'parameter_name': 'stopwords_removal', 'value': False}, {'parameter_name': 'language',\
 'value': 'english'}], 'dqv_value': '[{"item": "how", "frequency": 2}, {"item": "i", "frequency": 2}, {"item": "to", \
"frequency": 2}]'}, {'dqv_isMeasurementOf': 'text.distribution_most_frequent_elements_percent', \
'dqv_computedOn': 'text', 'rdf_datatype': 'List<Map<String,String>>', 'ddqv_hasParameters': [{'parameter_name': \
'num_items', 'value': 3}, {'parameter_name': 'tokenization', 'value': True}, {'parameter_name': 'stopwords_removal', \
'value': False}, {'parameter_name': 'language', 'value': 'english'}], 'dqv_value': '[{"item": "how", "frequency": \
0.10526}, {"item": "i", "frequency": 0.10526}, {"item": "to", "frequency": 0.10526}]'}]
        >>> tm.to_dqv(method_name='longest_words', parameters=[{'parameter_name': 'length', 'value': 5}])
        [{'dqv_isMeasurementOf': 'text.longest_words', 'dqv_computedOn': 'text', 'rdf_datatype': 'List<String>', \
'ddqv_hasParameters': [{'parameter_name': 'length', 'value': 5}], 'dqv_value': '["pasta", "please"]'}]
        """
        try:
            value = self.get(method_name)(**self._turn_parameter_to_dictionary(parameters))
        except Exception:
            # if error happen, return a QualityMeasurement object with Nan as value.
            return [{
                'dqv_isMeasurementOf': f'{self._class_name}.{method_name}',
                'dqv_computedOn': self.name,
                'rdf_datatype': "Error",
                'ddqv_hasParameters': parameters,
                'dqv_value': None
            }]
        # value contains different results
        if method_name in ['lexical_diversity', 'distribution_most_frequent_elements',
                           'distribution_less_frequent_elements']:
            return [{'dqv_isMeasurementOf': f'{self._class_name}.{element["method_name"]}',
                     'dqv_computedOn': self.name,
                     'rdf_datatype': element["data_type"],
                     'ddqv_hasParameters': parameters,
                     'dqv_value': element["value"]} for element in value]
        # value contains only one result
        return [{
            'dqv_isMeasurementOf': f'{self._class_name}.{method_name}',
            'dqv_computedOn': self.name,
            'rdf_datatype': self.data_type,
            'ddqv_hasParameters': parameters,
            'dqv_value': json.dumps(value)
        }]
