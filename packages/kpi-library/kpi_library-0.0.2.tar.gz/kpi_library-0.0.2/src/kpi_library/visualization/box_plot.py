# kpi_library/visualization/box_plot.py
import json
import pandas as pd

from typing import List, Dict, Union
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class VisualizationBoxPlot(MetricModel):
    """
    This metric visualizes the relationship between a categorical and a numerical column. In order to do so, it groups
    the numeric data by the values of the categirical column and computes the necessary statistics to build a box plot
    per group.

    Example
    -------
    >>> c = VisualizationBoxPlot()
    >>> df = pd.DataFrame({'num': [0.84872161, 0.08834098, 0.26244298, 0.99457054, 0.69617695, 0.99161138, \
    0.39472289, 0.21352392], 'cat': ['a', 'b', 'a', 'a', 'b', 'b', 'a', 'b']})
    >>> c.run(df, feature_one='cat', feature_two='num')
    [{'x_axis': 'a', 'y_axis': {'min': 0.26244298, 'max': 0.99457054, 'first_quartile': 0.3616529125, 'median': \
0.62172225, 'third_quartile': 0.8851838425, 'outliers': []}}, {'x_axis': 'b', 'y_axis': {'min': 0.08834098, 'max': \
0.99161138, 'first_quartile': 0.182228185, 'median': 0.454850435, 'third_quartile': 0.7700355575, 'outliers': []}}]
    >>> c.to_dqv(df, feature_one='cat', feature_two='num')
    [{'dqv_isMeasurementOf': 'visualization.box_plot', 'dqv_computedOn': 'cat, num', 'rdf_datatype': 'List<Map<String,\
Serializable>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"x_axis": "a", "y_axis": {"min": 0.26244298, "max": 0.9945\
7054, "first_quartile": 0.3616529125, "median": 0.62172225, "third_quartile": 0.8851838425, "outliers": []}}, {"x_axi\
s": "b", "y_axis": {"min": 0.08834098, "max": 0.99161138, "first_quartile": 0.182228185, "median": 0.454850435, "thir\
d_quartile": 0.7700355575, "outliers": []}}]'}]
    >>> c.to_dqv(df, feature_two='num')
    [{'dqv_isMeasurementOf': 'visualization.box_plot', 'dqv_computedOn': 'None, num', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='cat')
    [{'dqv_isMeasurementOf': 'visualization.box_plot', 'dqv_computedOn': 'cat, None', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame({'num': [None, 0.08834098, None, 0.99457054, None, 0.99161138, None, 0.21352392], 'cat': [\
    'a', None, 'a', None, 'b', None, 'a', None]})
    >>> c.run(df, feature_one='cat', feature_two='num')
    []
    >>> c.to_dqv(df, feature_one='cat', feature_two='num')
    [{'dqv_isMeasurementOf': 'visualization.box_plot', 'dqv_computedOn': 'cat, num', 'rdf_datatype': 'List<Map<\
String,Serializable>>', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(VisualizationBoxPlot, self).__init__(
            identifier='visualization.box_plot',
            keyword='VisualizationBoxPlot',
            title='Box plot',
            definition='Box plot per category',
            expected_data_type=str(ResultTypes.CAT_BOX_PLOT.value),
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

    def run(self, data: pd.DataFrame, **kwargs) -> List[Dict[str, Union[str, Dict[str, Union[float, List[float]]]]]]:
        """
        This method returns the important values to build a box plot per category.

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
            List of dictionaries where each dictionary contains the important information to build a box plot, i.e.,
            each dictionary is a different box plot
        """
        # check emptiness of the data and correctness of the parameters feature_one and feature_two
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        self._check_bi_data(data=data, feature_one=feature_one, feature_two=feature_two)
        # check correct data types
        df = self.__check_data(data, cat_feature=feature_one, num_feature=feature_two)
        # check if dataset is empty
        if df.empty:
            return []
        # group by cat_feature
        srs = df.groupby(by=feature_one)
        stats = srs.describe()[feature_two]
        # interquartile range
        iqr: pd.Series = stats['75%'] - stats['25%']
        upper: pd.Series = stats['75%'] + 1.5 * iqr
        lower: pd.Series = stats['25%'] - 1.5 * iqr
        # get box plot values
        return [
            {
                'x_axis': category,
                'y_axis': {
                    'min': stats.loc[category, 'min'],
                    'max': stats.loc[category, 'max'],
                    'first_quartile': stats.loc[category, '25%'],
                    'median': stats.loc[category, '50%'],
                    'third_quartile': stats.loc[category, '75%'],
                    'outliers': elements[feature_two].loc[
                        (elements[feature_two] > upper[category]) | (elements[feature_two] < lower[category])
                    ].tolist()
                }
            } for category, elements in srs
        ]

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
