# kpi_library/bi_analysis/correlation.py
import json
import pandas as pd

from typing import Optional
from kpi_library.model import MetricModel, ParameterModel
from kpi_library.errors import DataTypeError, EmptyDatasetError, DatasetFormatError, IncorrectParameterError
from kpi_library.result_types import ResultTypes


class BiAnalysisCorrelation(MetricModel):
    """
    This metric computes the correlation between two numeric columns.

    Example
    -------
    >>> c = BiAnalysisCorrelation()
    >>> df = pd.DataFrame({'num1': [1,2,3,4,5,6], 'num2': [7,8,9,10,11,12]})
    >>> c.run(df, feature_one='num1', feature_two='num2')
    1.0
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'Float', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"pearson"'}], 'dqv_value': '1.0'}]
    >>> df = pd.DataFrame({'num1': [0.6670973082526919, 0.35820003122314226, 0.37100375427833787, 0.6559245173447851, \
    0.338551585676914, 0.8526950321061055], 'num2': [0.1367429640134662, 0.6287662379378166, 0.24883975550552173, \
    0.6832259385165146, 0.8955835606812507, 0.5154380709425771]})
    >>> c.run(df, feature_one='num1', feature_two='num2', method='spearman')
    -0.6
    >>> df = pd.DataFrame({'num1': [0.6670973082526919, 0.35820003122314226, 0.37100375427833787, 0.6559245173447851, \
    None, 0.8526950321061055], 'num2': [0.1367429640134662, 0.6287662379378166, 0.24883975550552173, \
    0.6832259385165146, 0.8955835606812507, 0.5154380709425771]})
    >>> c.run(df, feature_one='num1', feature_two='num2', method='spearman')
    -0.3
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2', method=-1)
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '-1'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='error', feature_two='num2', method='pearson')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'error, num2', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"pearson"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='num1', feature_two='error', method='pearson')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, error', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"pearson"'}], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame({'num1': [0.6670973082526919, 0.35820003122314226, 0.37100375427833787, 0.6559245173447851, \
    None, 0.8526950321061055], 'num2': ['2022-02-01', '2022-02-01', '2022-02-01', '2022-02-01', '2022-02-01', '2022-02'\
    '-01']})
    >>> df['num2'] = pd.to_datetime(df['num2'], format='%Y-%m-%d')
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2', method='pearson')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"pearson"'}], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame({'num1': ['A', 'B', 'A', 'C', 'A', 'B'], 'num2': [0.1367429640134662, 0.6287662379378166, \
    0.24883975550552173, 0.6832259385165146, 0.8955835606812507, 0.5154380709425771]})
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2', method='pearson')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"pearson"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(df, feature_one='num1', feature_two=None, method='spearman')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, None', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"spearman"'}], 'dqv_value': 'null'}]
    >>> df = pd.DataFrame({'num1': [None, None, None], 'num2': [None, None, None]})
    >>> c.to_dqv(df, feature_one='num1', feature_two='num2', method='pearson')
    [{'dqv_isMeasurementOf': 'biAnalysis.correlation', 'dqv_computedOn': 'num1, num2', 'rdf_datatype': 'Error', 'ddqv_\
hasParameters': [{'parameter_name': 'method', 'value': '"pearson"'}], 'dqv_value': 'null'}]

    """
    def __init__(self):
        super(BiAnalysisCorrelation, self).__init__(
            identifier='biAnalysis.correlation',
            keyword='BiAnalysisCorrelation',
            title='Correlation',
            definition='Correlation between two numeric datasets.',
            expected_data_type=str(ResultTypes.FLOAT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [ParameterModel(
            name="method", data_type="string", possible_values=["pearson", "spearman"], default_value="pearson",
            description="Type of correlation analysis, whereas Pearson correlation coefficient or Spearman rank "
                        "correlation.")]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # run method
        params = {'method': kwargs.get('method', 'pearson')}
        feature_one=kwargs.get('feature_one', None)
        feature_two=kwargs.get('feature_two', None)
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two, method=params['method'])
        except (EmptyDatasetError, DataTypeError, DatasetFormatError, IncorrectParameterError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': f"{feature_one}, {feature_two}",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': f"{feature_one}, {feature_two}",
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.DataFrame, **kwargs) -> Optional[float]:
        """
        This method returns the correlation between two numeric columns.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.

        Returns
        -------
        _: float
            Correlation.
        """
        # check dataset
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        self.__check_data(data, feature_one=feature_one, feature_two=feature_two)
        # check parameter
        method = kwargs.get('method', 'pearson')
        self._check_enum_parameter(parameter=method, parameter_name='method', values=["pearson", "spearman"])
        # compute correlation
        return float(data[feature_one].corr(other=data[feature_two], method=method))

    def __check_data(self, df: pd.DataFrame, feature_one: str, feature_two: str):
        """
        This method checks the correct structure and content of the data (`data`). The dataset must be not empty and
        contain two numeric columns (`feature_one`, `feature_two`).

        Parameters
        ----------
        df: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        feature_one: str
            Name of the first column of the dataset.
        feature_two: str
            Name of the second column of the dataset.

        Raises
        ------
        EmptyDatasetError
            Whether the dataset is empty or not.
        IncorrectParameterError
            Whether any of the parameters feature_one or feature_two is incorrect and does not correspond with any of
            the columns in the dataset.
        DataTypeError
            Whether any of the columns is not numeric.
        """
        # check structure and emptiness of the data
        self._check_bi_data(data=df, feature_one=feature_one, feature_two=feature_two)
        # check data types of the columns
        types: pd.Series = df.dtypes
        if str(types[feature_one]) not in ['float64', 'int64']:
            raise DataTypeError(f'The column {feature_one} has an incorrect format, it must be numeric but it is '
                                f'{types[feature_one]}.', code=400)
        if str(types[feature_two]) not in ['float64', 'int64']:
            raise DataTypeError(f'The column {feature_two} has an incorrect format, it must be numeric but it is '
                                f'{types[feature_two]}.', code=400)
