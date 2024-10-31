# kpi_library/visualization/scatter_chart.py
import json
import pandas as pd

from typing import List, Dict
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class VisualizationScatterChart(MetricModel):
    """
    This metric extracts from a dataframe of two numeric columns the necessary information to visualize the data in a
    scatter plot.

    Example
    -------
    >>> c = VisualizationScatterChart()
    >>> df = pd.DataFrame([{"num1":0.2414967139,"num2":0.127630639},{"num1":0.4481320923,"num2":0.2740067199},\
    {"num1":0.0717208358,"num2":0.3938141558},{"num1":0.6105066501,"num2":0.5307449389},\
    {"num1":0.8955528729,"num2":0.8586566748},{"num1":0.2001987326,"num2":0.514215983}])
    >>> c.run(df, feature_one='num1', feature_two='num2')
    [{'x_axis': 0.2414967139, 'y_axis': 0.127630639}, {'x_axis': 0.4481320923, 'y_axis': 0.2740067199}, {'x_axis': 0.\
0717208358, 'y_axis': 0.3938141558}, {'x_axis': 0.6105066501, 'y_axis': 0.5307449389}, {'x_axis': 0.8955528729, 'y_ax\
is': 0.8586566748}, {'x_axis': 0.2001987326, 'y_axis': 0.514215983}]
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2')
    [{'dqv_isMeasurementOf': 'visualization.scatter_chart', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'List<Map<\
String,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[{"x_axis": 0.2414967139, "y_axis": 0.127630639}, {"x_axis"\
: 0.4481320923, "y_axis": 0.2740067199}, {"x_axis": 0.0717208358, "y_axis": 0.3938141558}, {"x_axis": 0.6105066501, "\
y_axis": 0.5307449389}, {"x_axis": 0.8955528729, "y_axis": 0.8586566748}, {"x_axis": 0.2001987326, "y_axis": 0.514215\
983}]'}]
    >>> c.to_dqv(df, feature_two='num2')
    [{'dqv_isMeasurementOf': 'visualization.scatter_chart', 'dqv_computedOn': 'None, num2', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='num1')
    [{'dqv_isMeasurementOf': 'visualization.scatter_chart', 'dqv_computedOn': 'num1, None', 'rdf_datatype': 'Error', '\
ddqv_hasParameters': [], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame([{"num1":None,"num2":0.127630639},{"num1":None,"num2":0.2740067199}, {"num1":0.0717208358,\
    "num2":None},{"num1":None,"num2":0.5307449389},{"num1":None,"num2":0.8586566748},{"num1":0.2001987326,"num2":None}])
    >>> c.run(df, feature_one='num1', feature_two='num2')
    []
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2')
    [{'dqv_isMeasurementOf': 'visualization.scatter_chart', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'List<Map<\
String,String>>', 'ddqv_hasParameters': [], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(VisualizationScatterChart, self).__init__(
            identifier='visualization.scatter_chart',
            keyword='VisualizationScatterChart',
            title='Scatter chart',
            definition='Visualize the data by a scatter chart',
            expected_data_type=str(ResultTypes.PLOT.value),
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

    def run(self, data: pd.DataFrame, **kwargs) -> List[Dict[str, float]]:
        """
        Extracts from the dataframe of two numeric columns the necessary information to visualize the data in a scatter
        plot.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that contains the following information:
                feature_one: str
                    Name of the first numeric column.
                feature_two: str
                    Name of the second numeric column.

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
            List of dictionaries containing the necessary information to visualize the numerical columns in a scatter
            plot (`x_axis`, `y_axis`).
        """
        # check emptiness of the data and correctness of the parameters feature_one and feature_two
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        self._check_bi_data(data=data, feature_one=feature_one, feature_two=feature_two)
        # check correct data types
        df = self.__check_data(data)
        # check if dataset is empty
        if df.empty:
            return []
        # compute statistic
        return [{'x_axis': num1, 'y_axis': num2} for num1, num2 in df.itertuples(index=False)]

    @staticmethod
    def __check_data(data: pd.DataFrame):
        """
        This method checks the data types of the dataset to make sure both columns contain numeric values.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.

        Raises
        ------
        DataTypeError
            If any of the columns does not contain numeric values.
        """
        # check correct format
        types: pd.Series = data.dtypes
        for name_column, type_column in types.items():
            if type_column not in ['float64', 'int64']:
                raise DataTypeError(f'The column {name_column} has an incorrect format, it must be numeric but it is '
                                    f'{type_column}.', code=400)
        # return clean dataframe
        return data.dropna(inplace=False)
