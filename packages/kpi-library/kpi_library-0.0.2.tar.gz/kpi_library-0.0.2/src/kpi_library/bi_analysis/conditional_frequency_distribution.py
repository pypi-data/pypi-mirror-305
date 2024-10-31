# kpi_library/bi_analysis/conditional_frequency_distribution.py
import re
import json
import pandas as pd
from nltk.corpus import stopwords
from visions.functional import infer_type

from typing import List, Dict, Union
from ..custom_metric import CustomSet
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError, DatasetFormatError
from ..result_types import ResultTypes


class BiAnalysisConditionalFrequencyDistribution(MetricModel):
    """
    This metric computes the conditional frequency distribution. This distribution shows the most frequent words of a
    text column depending on the values of a categorical column.

    Example
    -------
    >>> c = BiAnalysisConditionalFrequencyDistribution()
    >>> srs = pd.DataFrame({'cat': ['a', 'b', 'a', 'c', 'a'], 'text': ['two cats and three dogs', 'the freedom the '\
    'most important thing', 'the cats are gorgeous', 'you are unbelievable', 'the dogs are the best animal ever']})
    >>> c.run(srs, feature_one='cat', feature_two='text', num_items=2, language='english')
    [{'x_axis': 'a', 'y_axis': [{'item': 'cats', 'frequency': 2}, {'item': 'dogs', 'frequency': 2}]}, {'x_axis': 'b', \
'y_axis': [{'item': 'freedom', 'frequency': 1}, {'item': 'important', 'frequency': 1}]}, {'x_axis': 'c', 'y_axis': [{'\
item': 'unbelievable', 'frequency': 1}]}]
    >>> c.to_dqv(srs, feature_one='cat', feature_two='text', num_items=2, language='english')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'cat, text', 'rdf_datat\
ype': 'List<Map<String,Serializable>>', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parame\
ter_name': 'language', 'value': '"english"'}], 'dqv_value': '[{"x_axis": "a", "y_axis": [{"item": "cats", "frequency":\
 2}, {"item": "dogs", "frequency": 2}]}, {"x_axis": "b", "y_axis": [{"item": "freedom", "frequency": 1}, {"item": "imp\
ortant", "frequency": 1}]}, {"x_axis": "c", "y_axis": [{"item": "unbelievable", "frequency": 1}]}]'}]
    >>> c.to_dqv(srs, feature_one='cat', feature_two='text', num_items=2, language='error')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'cat, text', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parameter_name': 'language', 'va\
lue': '"error"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(srs, feature_one='cat', feature_two='text', num_items=-1, language='english')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'cat, text', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '-1'}, {'parameter_name': 'language', 'v\
alue': '"english"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(srs, feature_one='cat', num_items=2, language='english')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'cat, None', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parameter_name': 'language', 'va\
lue': '"english"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(srs, feature_two='text', num_items=2, language='english')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'None, text', 'rdf_data\
type': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parameter_name': 'language', 'v\
alue': '"english"'}], 'dqv_value': 'null'}]
    >>> srs = pd.DataFrame({'cat': [20.512, 0.5123, 12, 1, 2], 'text': ['two cats and three dogs', 'the freedom the '\
    'most important thing', 'the cats are gorgeous', 'you are unbelievable', 'the dogs are the best animal ever']})
    >>> c.to_dqv(srs, feature_one='cat', feature_two='text', num_items=2, language='english')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'cat, text', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parameter_name': 'language', 'va\
lue': '"english"'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(srs, feature_one='text', feature_two='cat', num_items=2, language='english')
    [{'dqv_isMeasurementOf': 'biAnalysis.conditional_frequency_distribution', 'dqv_computedOn': 'text, cat', 'rdf_datat\
ype': 'Error', 'ddqv_hasParameters': [{'parameter_name': 'num_items', 'value': '2'}, {'parameter_name': 'language', 'va\
lue': '"english"'}], 'dqv_value': 'null'}]
    """
    LANGUAGES_STOPWORDS: List[str] = stopwords.fileids()

    def __init__(self):
        super(BiAnalysisConditionalFrequencyDistribution, self).__init__(
            identifier='biAnalysis.conditional_frequency_distribution',
            keyword='BiAnalysisConditionalFrequencyDistribution',
            title='Conditional Frequency Distribution',
            definition='The most frequent words of a text column depending on the values of a categorical column.',
            expected_data_type=str(ResultTypes.CAT_DISTRIBUTION_INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_items', data_type=str(ResultTypes.INT.value), possible_values=None,
                           default_value='10', description="Number of elements to show."),
            ParameterModel(
                name='language', data_type=str(ResultTypes.STRING.value), default_value="english",
                possible_values=self.LANGUAGES_STOPWORDS, description="Language in which the texts are written.")
        ]

    def to_dqv(self, data: pd.DataFrame, **kwargs):
        # run method
        feature_one = kwargs.get('feature_one')
        feature_two = kwargs.get('feature_two')
        params = {
            'num_items': kwargs.get('num_items', 10),
            'language': kwargs.get('language', 'english')
        }
        try:
            result = self.run(data, feature_one=feature_one, feature_two=feature_two, **params)
        except (EmptyDatasetError, DataTypeError, IncorrectParameterError, DatasetFormatError):
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

    def run(self, data: pd.DataFrame, **kwargs
            ) -> List[Dict[str, Union[str, List[Dict[str, Union[float, int]]]]]]:
        """
        This method collects separately the word frequency distribution of different groups of texts. These texts are
        grouped by the values of the categorical data.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        kwargs: :obj:`dict`
            Object that contains the following information:
                feature_one: str
                    Categorical column name.
                feature_two: str
                    Text column name.
                num_items: int, optional. Default 10
                    Number of elements to show in each word frequency distribution.
                language: str, optional. Default english
                    Language in which the texts are written.
        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            Dictionary containing the category of the categorical variable (x_axis) and the most word frequent
            distribution of this category (y_axis).
        """
        # check data
        feature_one = kwargs.get('feature_one', None)
        feature_two = kwargs.get('feature_two', None)
        srs = self.__check_data(data, feature_one=feature_one, feature_two=feature_two)
        # check parameter
        num_items = self._check_int_parameter(parameter=kwargs.get('num_items', 10), parameter_name='num_items', ge=1)
        language = kwargs.get('language', 'english')
        self._check_enum_parameter(parameter=language, parameter_name='language', values=self.LANGUAGES_STOPWORDS)
        # study frequency distribution of the different words in the data
        temp = srs.groupby(feature_one, dropna=True)
        return [{
            'x_axis': str(category),
            'y_axis': self.__word_distribution(cat_data[feature_two], num_items=num_items, language=language)
        } for category, cat_data in temp]

    def __check_data(self, df: pd.DataFrame, feature_one: str, feature_two: str) -> pd.DataFrame:
        """
        This method checks the correct structure and format of the dataset and returns the dataset with the correct data
        types.

        Parameters
        ----------
         df: :obj:`pandas.DataFrame`
            Object containing the data to be processed.
        feature_one: str
            Categorical column name.
        feature_two: str
            Text column name.

        Raises
        ------
        IncorrectParameterError
            Whether any of the parameters feature_one or feature_two are not corrects.
        DataTypeError
            Whether any of the columns does not have a correct format.

        Returns
        -------
        : :obj:`pd.DataFrame`
            Pandas object containing the data wuith the correct data types.
        """
        # check emptiness of the data and the correctness of feature_one and feature_two
        self._check_bi_data(df, feature_one=feature_one, feature_two=feature_two)
        # drop null values
        srs = df.dropna(inplace=False)
        # check categorical variable (feature_one)
        typeset = CustomSet()
        data_type = str(infer_type(srs[feature_one].iloc[:5], typeset))
        if str(data_type) not in ['Object', 'Categorical', 'String', 'Integer']:
            raise DataTypeError(f"The column {feature_one} format is incorrect, the values should be categories, "
                                f"but they are `{data_type}s`.", code=400)
        # check string variable
        data_type = str(infer_type(srs[feature_two].iloc[:5], typeset))
        if str(data_type) not in ['Object', 'Categorical', 'String']:
            raise DataTypeError(f'The column {feature_two} format is incorrect, the values should be strings, '
                                f'but they are {data_type}s.', code=400)
        # return data with the specified types
        return srs.astype({feature_one: 'category', feature_two: 'string'})

    @staticmethod
    def __word_distribution(srs: pd.Series, num_items: int, language: str) -> List[Dict[str, Union[str, int]]]:
        """"""
        # tokenize the sentences into words and remove the stopwords
        _stopwords = set(stopwords.words(language))
        temp = srs.transform(lambda entry: [word for word in re.split(r'\W+', entry.lower()) if word != ''])
        temp = temp.apply(lambda entry: [word for word in entry if word not in _stopwords]).explode()
        # compute the frequency of each word
        temp = temp.value_counts(sort=True, ascending=False, dropna=True)
        # return result in distribution format
        return [{'item': word, 'frequency': frequency} for word, frequency in temp.iloc[:num_items].items()]
