# kpi_library/visualization/bar_chart.py
import json
import numpy as np
import pandas as pd

from typing import List, Dict, Union
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class VisualizationBarChart(MetricModel):
    """
    This metric visualizes the relationship between a categorical and a numerical column. In order to do so, it groups
    the numeric data by the values of the categorical column and computes an operation such as sum, mean or median to
    the numeric data of each group and displaies the result as a bar chart, where each bar corresponds to each
    category/group.

    Example
    -------
    >>> c = VisualizationBarChart()
    >>> df = pd.DataFrame({'num': [0.84872161, 0.08834098, 0.26244298, 0.99457054, 0.69617695, 0.99161138, \
    0.39472289, 0.21352392], 'cat': ['a', 'b', 'a', 'a', 'b', 'b', 'a', 'b']})
    >>> c.run(df, feature_one='cat', feature_two='num', op='sum')
    [{'x_axis': 'a', 'y_axis': 2.50045802}, {'x_axis': 'b', 'y_axis': 1.98965323}]
    >>> c.run(df, feature_one='cat', feature_two='num', op='median')
    [{'x_axis': 'a', 'y_axis': 0.62172225}, {'x_axis': 'b', 'y_axis': 0.454850435}]
    >>> c.to_dqv(df, feature_one='cat', feature_two='num', op='mean')
    [{'dqv_isMeasurementOf': 'visualization.bar_chart', 'dqv_computedOn': 'cat, num', 'rdf_datatype': 'List<Map<String,\
String>>', 'ddqv_hasParameters': [{'parameter_name': 'op', 'value': '"mean"'}], 'dqv_value': '[{"x_axis": "a", "y_a\
xis": 0.625114505}, {"x_axis": "b", "y_axis": 0.4974133075}]'}]
    >>> c.to_dqv(df, feature_one='cat', feature_two='num', op='error')
    [{'dqv_isMeasurementOf': 'visualization.bar_chart', 'dqv_computedOn': 'cat, num', 'rdf_datatype': 'Error', 'ddqv_ha\
sParameters': [{'parameter_name': 'op', 'value': '"error"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_two='num', op='sum')
    [{'dqv_isMeasurementOf': 'visualization.bar_chart', 'dqv_computedOn': 'None, num', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [{'parameter_name': 'op', 'value': '"sum"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='cat', op='sum')
    [{'dqv_isMeasurementOf': 'visualization.bar_chart', 'dqv_computedOn': 'cat, None', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [{'parameter_name': 'op', 'value': '"sum"'}], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame({'num': [None, 0.08834098, None, 0.99457054, None, 0.99161138, None, 0.21352392], 'cat': [\
    'a', None, 'a', None, 'b', None, 'a', None]})
    >>> c.run(df, feature_one='cat', feature_two='num', op='sum')
    []
    >>> c.to_dqv(df, feature_one='cat', feature_two='num', op='sum')
    [{'dqv_isMeasurementOf': 'visualization.bar_chart', 'dqv_computedOn': 'cat, num', 'rdf_datatype': 'List<Map<\
String,String>>', 'ddqv_hasParameters': [{'parameter_name': 'op', 'value': '"sum"'}], 'dqv_value': '[]'}]
    """
    __BAR_OPS = {'sum': np.sum, 'mean': np.mean, 'median': np.median}

    def __init__(self):
        super(VisualizationBarChart, self).__init__(
            identifier='visualization.bar_chart',
            keyword='VisualizationBarChart',
            title='Bar chart',
            definition='Bar chart between a categorical and numeric variable.',
            expected_data_type=str(ResultTypes.PLOT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='op', data_type=str(ResultTypes.STRING.value), default_value='sum',
                           possible_values=['sum', 'mean', 'median'],
                           description='Method to apply whether the bar chart must compare the values of a categorical '
                                       'variables taking into account the values of a numerical variable.')]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # run method
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        param = {'op': kwargs.get('op', 'sum')}
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two, op=param['op'])
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': f"{feature_one}, {feature_two}",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=param),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': f"{feature_one}, {feature_two}",
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=param),
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
        self._check_bi_data(data=data, feature_one=feature_one, feature_two=feature_two)
        # check parameters
        op = kwargs.get('op', 'sum')
        self._check_enum_parameter(parameter=op, parameter_name='op', values=['sum', 'mean', 'median'])
        # check correct data types
        df = self.__check_data(data, cat_feature=feature_one, num_feature=feature_two)
        # check if dataset is empty
        if df.empty:
            return []
        # group data relating to the categorical variable
        groups = df[feature_two].groupby(df[feature_one])
        # compute `op` in each group of feat_num and save in answer the results obtained
        res = groups.agg(self.__BAR_OPS[op])
        return [{'x_axis': str(category), 'y_axis': float(result)} for category, result in res.items()]

    @staticmethod
    def __check_data(data: pd.DataFrame, cat_feature: str, num_feature: str) -> pd.DataFrame:
        """
        This method checks the data types of the dataset to make sure both columns contain numeric values.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        cat_feature: str
            Name of the categorical column.
        num_feature: str
            Name of the numeric column.

        Raises
        ------
        DataTypeError
            If any of the columns does not contain numeric values.
        """
        # check correct data type
        types: pd.Series = data.dtypes
        if types[num_feature] not in ['float64', 'int64']:
            raise DataTypeError(f'The column {num_feature} has an incorrect format, it must be numeric but it is '
                                f'{types[num_feature]}.', code=400)
        if types[cat_feature] not in ['category', 'string', 'object', 'int64']:
            raise DataTypeError(f'The column {cat_feature} has an incorrect format, it must contain ordinal values'
                                f' but it contains {types[cat_feature]} values.', code=400)
        # return the clean dataset as categories
        return data.dropna(inplace=False).astype({cat_feature: 'category'})
