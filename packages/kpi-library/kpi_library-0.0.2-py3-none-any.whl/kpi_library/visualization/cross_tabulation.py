# kpi_library/visualization/cross_tabulation.py
import json
import pandas as pd

from typing import List, Dict, Union
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class VisualizationCrossTabulation(MetricModel):
    """
    This metric visualizes the relationship between two categorical columns. In order to do so, it counts the frequency
    of occurrence of each pair of values.

    Example
    -------
    >>> c = VisualizationCrossTabulation()
    >>> df = pd.DataFrame({'num': ['female', 'male', 'male', 'female', 'male', 'female', 'female', 'male'], \
        'cat': ['a', 'b', 'a', 'a', 'b', 'b', 'a', 'b']})
    >>> c.run(df, feature_one='num', feature_two='cat')
    [{'x_axis': 'female', 'y_axis': 'a', 'value': 3}, {'x_axis': 'female', 'y_axis': 'b', 'value': 1}, {'x_axis': '\
male', 'y_axis': 'a', 'value': 1}, {'x_axis': 'male', 'y_axis': 'b', 'value': 3}]
    >>> c.to_dqv(df, feature_one='num', feature_two='cat')
    [{'dqv_isMeasurementOf': 'visualization.cross_tabulation', 'dqv_computedOn': 'num, cat', 'rdf_datatype': 'List<Map\
<String,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"x_axis": "female", "y_axis": "a", "value": 3}, {"x_axis\
": "female", "y_axis": "b", "value": 1}, {"x_axis": "male", "y_axis": "a", "value": 1}, {"x_axis": "male", "y_axis": \
"b", "value": 3}]'}]
    >>> c.to_dqv(df, feature_two='num')
    [{'dqv_isMeasurementOf': 'visualization.cross_tabulation', 'dqv_computedOn': 'None, num', 'rdf_datatype': 'Error',\
 'ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='cat')
    [{'dqv_isMeasurementOf': 'visualization.cross_tabulation', 'dqv_computedOn': 'cat, None', 'rdf_datatype': 'Error',\
 'ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame({'num': ['female', None, 'male', None, 'male', None, 'female', None], 'cat': [None, 'b', \
    None, 'a', None, 'b', None, 'b']})
    >>> c.run(df, feature_one='cat', feature_two='num')
    []
    >>> c.to_dqv(df, feature_one='cat', feature_two='num')
    [{'dqv_isMeasurementOf': 'visualization.cross_tabulation', 'dqv_computedOn': 'cat, num', 'rdf_datatype': 'List<Map<\
String,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(VisualizationCrossTabulation, self).__init__(
            identifier='visualization.cross_tabulation',
            keyword='VisualizationCrossTabulation',
            title='Cross-tabulation',
            definition='Frequency of occurrence of the pair of values of two categorical columns.',
            expected_data_type=str(ResultTypes.CROSS_TABULATION.value),
            dimension='profile',
            category='inherent'
        )

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # run method
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': f"{feature_one}, {feature_two}",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': [],
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': f"{feature_one}, {feature_two}",
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.DataFrame, **kwargs) -> List[Dict[str, Union[str, float]]]:
        """
        This method returns the necessary points to build a bar chart between a numerical and a categorical variables.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that contains the following information:
                feature_one: str
                    Name of the categorical column.
                feature_two: str
                    Name of the numeric column.
                op: {sum, mean, median}, optional. Default sum
                    Method to apply whether the bar chart must compare the values of a categorical variables taking into
                    account the values of a numerical variable.

        Raises
        ------
        EmptyDatasetError
            Whether the dataset is empty or not.
        IncorrectParameterError
            Whether any of the parameters feature_one or feature_two are not corrects.
        DataTypeError
            Whether any of the columns of the dataset are not numeric.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries where each of them represents an element, and the value obtaining after applying the
            method (`op`) to the values of the numerical variable related to the element.
        """
        # check emptiness of the data and correctness of the parameters feature_one and feature_two
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        df = self.__check_data(data, feature_one=feature_one, feature_two=feature_two)
        # check if dataset is empty
        if df.empty:
            return []
        # group data and go by each pair of categories and count number of times it occurs
        groups = df.groupby(by=[feature_one, feature_two])
        return [{
            'x_axis': str(x_axis), 'y_axis': str(y_axis), 'value': int(times.shape[0])
        } for (x_axis, y_axis), times in groups]

    def __check_data(self, data: pd.DataFrame, feature_one: str, feature_two: str) -> pd.DataFrame:
        """
        This method checks the data types of the dataset to make sure both columns contain numeric values.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        feature_one: str
            Name of the first categorical column.
        feature_two: str
            Name of the second categorical column.

        Raises
        ------
        DataTypeError
            If any of the columns does not contain numeric values.
        """
        # check emptiness of the dataset and the correctness of the parameters feature_one and feature_two
        self._check_bi_data(data=data, feature_one=feature_one, feature_two=feature_two)
        # check correct data type
        types: pd.Series = data.dtypes
        for name_column, type_column in types.items():
            if type_column not in ['category', 'string', 'object', 'int64']:
                raise DataTypeError(f'The column {name_column} has an incorrect format, it must contain ordinal values '
                                    f'but it contains {type_column} values.', code=400)
        # return the clean dataset as categories
        return data.dropna(inplace=False).astype('category')
