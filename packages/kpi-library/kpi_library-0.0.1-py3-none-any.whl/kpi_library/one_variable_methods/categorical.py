# kpi_library/one_variable_methods/categorical.py
import numpy as np
import pandas as pd
from visions.functional import infer_type
# commenting
from typing import Dict, List, Union
from collections.abc import Callable
# class uses
from ..general.customset import CustomSet
from ..uni_variable import OneVarMethods
from ..errors import DataTypeError
from ..result_types import ResultTypes


class CategoricalMethods(OneVarMethods):
    """
    Categorical column quality profiling methods.

    Parameters
    ----------
    dataset: :obj:`pandas.Series`
        Object containing the categorical data to be processed.

    Attributes
    ----------
    data: :obj:`pandas.Series`
        Object containing the categorical data to be processed.
    data_numpy: :obj:`numpy.ndarray`
        Numpy array containing the categorical data to be processed.
    v_len: :obj:`numpy.vectorize`
        Vectorized length function.
    data_lengths: :obj:`numpy.ndarray` or None
        Numpy array containing the length in characters of each entry.
    """
    # attributes
    data: pd.Series
    data_numpy: np.ndarray
    v_len: Callable
    data_lengths: np.ndarray

    # constructor
    def __init__(self, dataset: pd.Series):
        super(CategoricalMethods, self).__init__(class_name='categorical', dataset=dataset)
        # drop null values to check if there are data
        dataset_not_null: pd.Series = dataset.dropna(inplace=False)
        self.empty = dataset_not_null.empty
        # get correct format of the data and in a numpy array
        self.data = self.__check_data(dataset=dataset, not_null_dataset=dataset_not_null)
        self.data_numpy = dataset_not_null.to_numpy()
        # get function length
        self.v_len = np.vectorize(len)

    @staticmethod
    def __check_data(dataset: pd.Series, not_null_dataset: pd.Series) -> pd.Series:
        """
        Check the correct format and type of the dataset.

        Parameters
        ----------
        dataset: :obj:`pandas.Series`
            Pandas object containing the categorical data to be processed.

        Raises
        ------
        DataTypeError
            If the data type of `dataset` is not numeric.

        Returns
        -------
        dataset: :obj:`pandas.Series`
            Pandas object containing the numeric data to be processed.
        """
        # check if the data (dataset) is incorrect
        typeset = CustomSet()
        data_type = str(infer_type(not_null_dataset.iloc[:5], typeset))
        if data_type not in ['Generic', 'Categorical', 'String', 'Integer']:
            raise DataTypeError(f"The column format is incorrect, the values should be categories but they are "
                                f"`{data_type}`.", code=400)
        # return the data as category format
        return dataset.astype('category')

    def mode(self, return_element: str = 'element') -> Union[str, int, float, None]:
        """
        Obtains the most frequent element or its frequency of the data depending on the parameter `return_element`.

        Parameters
        ----------
        return_element: {'element', 'frequency', 'normalized'}. Default 'element'.
            Whether the method should return the most frequent element of the data, its frequency or its normalized
            frequency, i.e. the percentage of data that are this element.

        Examples
        --------
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID'))
        >>> nm.mode(return_element='element')
        'a'
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b']))
        >>> nm.mode(return_element='frequency')
        3
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b']))
        >>> nm.mode()
        'a'
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID'))
        >>> nm.mode(return_element='normalized')
        0.5
        >>> nm = CategoricalMethods(pd.Series([None, None, None], name='ID'))
        >>> nm.mode()

        Raises
        ------
        IncorrectParameterError
            Whether the `return_element` parameter is different from element, frequency or normalized.

        Returns
        -------
        _: str, int or float
            This method returns the most frequent element of the data, its frequency or it normalized frequency.
        """
        # check if the data is empty
        if self.empty:
            self.data_type = ResultTypes.STRING.value
            return None
        # check return_element parameter
        self._check_enum_parameter(
            parameter=return_element, parameter_name='return_element', values=['element', 'frequency', 'normalized'])
        # process data
        result = self.data.value_counts(sort=True)
        if return_element == 'element':
            self.data_type = ResultTypes.STRING.value
            return result.index[0]
        elif return_element == 'frequency':
            self.data_type = ResultTypes.INT.value
            return int(result.iloc[0])

        self.data_type = ResultTypes.FLOAT.value
        return float(round(result.iloc[0] / self.n_rows, 5))

    def length_distribution(self, normalized: Union[bool, str] = False) -> List[Dict[str, int]]:
        """
        Obtains statistics from the length distribution in characters of the categorical data. The method returns the
        minimum (`min`), maximum (`max`), median (`median`), average (`mean`), and standard deviation (`std`) length in
        characters of the different values in the data.

        Parameters
        ----------
        normalized: str, or bool. Default False
            Whether the output should be normalized or not.

        Examples
        --------
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID'))
        >>> nm.length_distribution()
        [{'item': 1, 'frequency': 6}]
        >>> nm = CategoricalMethods(pd.Series(['female', 'male', 'male', 'female', 'female', 'male']))
        >>> nm.length_distribution(normalized=False)
        [{'item': 4, 'frequency': 3}, {'item': 6, 'frequency': 3}]
        >>> nm = CategoricalMethods(pd.Series(['female', 'male', 'male', 'female', 'female', 'male']))
        >>> nm.length_distribution(normalized='false')
        [{'item': 4, 'frequency': 3}, {'item': 6, 'frequency': 3}]
        >>> nm = CategoricalMethods(pd.Series(['female', 'male', None, 'female', 'female', 'male'], name='ID'))
        >>> nm.length_distribution(normalized='True')
        [{'item': 4, 'frequency': 0.33333}, {'item': 6, 'frequency': 0.5}]
        >>> nm = CategoricalMethods(pd.Series(['female', 'male', 'male', 'female', 'female', 'male'], name='ID'))
        >>> nm.length_distribution(normalized=True)
        [{'item': 4, 'frequency': 0.5}, {'item': 6, 'frequency': 0.5}]
        >>> nm = CategoricalMethods(pd.Series([None, None, None], name='ID'))
        >>> nm.length_distribution()
        []

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of a dictionary containing the name of the given data and the length distribuion of the values.
        """
        # check if the data is empty
        if self.empty:
            self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value
            return []
        # check parameters
        normalized = self._check_boolean_parameter(parameter=normalized, parameter_name='normalized')
        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value if normalized else ResultTypes.DISTRIBUTION_INT.value

        # compute length of each entry
        self.data_lengths = getattr(self, 'data_lengths', self.v_len(self.data_numpy))
        # compute frequency of each length
        uniques, counts = np.unique(self.data_lengths, return_counts=True)
        return [{
            "item": int(item),
            "frequency": float(round(frequency/self.n_rows, 5)) if normalized else int(frequency)
        } for item, frequency in zip(uniques, counts)]

    def outliers(self, normalized: Union[bool, str] = False) -> Union[int, float]:
        """
        Checks the data, computes the length of each entry, obtains possible outliers of those lengths and returns the
        number of outliers found as an integer or float, if the output is normalized.

        Parameters
        ----------
        normalized: str, or bool. Default False
            Whether the output should be normalized or not.

        Examples
        --------
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name=''))
        >>> nm.outliers()
        0
        >>> nm = CategoricalMethods(pd.Series(['female', 'a', 'b', 'c', 'a', 'a'], name='ID'))
        >>> nm.outliers(normalized="false")
        1
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name=''))
        >>> nm.outliers(normalized="true")
        0.0
        >>> nm = CategoricalMethods(pd.Series(['female', 'a', 'b', 'c', 'a', 'a'], name='ID'))
        >>> nm.outliers(normalized=True)
        0.16667
        >>> nm = CategoricalMethods(pd.Series(['female', 'a', 'b', 'c', 'a', 'a'], name='ID'))
        >>> nm.outliers(normalized="true")
        0.16667
        >>> nm = CategoricalMethods(pd.Series([None, None, None], name='ID'))
        >>> nm.outliers()
        0

        Returns
        -------
        _: :obj:`dict`
            Dictionary containing the number of possible outliers (`number`) and where they are in the data, i.e., the
            index of those entries (`index`).
        """
        # check if the data is empty
        if self.empty:
            self.data_type = ResultTypes.INT.value
            return 0
        # check normalized parameter
        normalized = self._check_boolean_parameter(parameter=normalized, parameter_name='normalized')

        # computes the length of each entry and obtains statistics
        self.data_lengths = getattr(self, 'data_lengths', self.v_len(self.data_numpy))

        stats = np.percentile(a=self.data_lengths, q=[25, 75])
        iqr = stats[1] - stats[0]
        upper = stats[1] + 1.5*iqr
        lower = stats[0] - 1.5*iqr

        # obtain possible outliers and return the number of outliers found
        outliers = self.data_lengths[(self.data_lengths > upper) | (self.data_lengths < lower)].size

        if normalized:
            self.data_type = ResultTypes.FLOAT.value
            return round(outliers/self.n_rows, 5)

        self.data_type = ResultTypes.INT.value
        return outliers

    def frequency_distribution(
            self, num_items: Union[int, str, None] = None, normalized: Union[bool, str] = False
    ) -> List[Dict[str, Union[int, float, str]]]:
        """
        Computes the frequency distribution of the given data. It returns the number of occurrence of the first
        `num_items` most frequent elements or the percentage of occurrence, depending on the parameter `normalized`.

        Notes
        -----
        If `num_items` is None, all distinct elements are returned with its frequency of occurrence.

        Parameters
        ----------
        num_items: int
            Number of elements to show.
        normalized: str, or bool. Default False
            Whether the output should be normalized or not.

        Examples
        --------
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID'))
        >>> nm.frequency_distribution(num_items=None)
        [{'item': 'a', 'frequency': 3}, {'item': 'b', 'frequency': 2}, {'item': 'c', 'frequency': 1}]
        >>> nm.frequency_distribution(normalized='True')
        [{'item': 'a', 'frequency': 0.5}, {'item': 'b', 'frequency': 0.33333}, {'item': 'c', 'frequency': 0.16667}]
        >>> nm = CategoricalMethods(pd.Series(['b', 'a', 'b', 'c', 'a', 'a'], name='ID'))
        >>> nm.frequency_distribution(num_items=1, normalized='False')
        [{'item': 'a', 'frequency': 3}]
        >>> nm.frequency_distribution(num_items='1', normalized='true')
        [{'item': 'a', 'frequency': 0.5}]
        >>> nm = CategoricalMethods(pd.Series([None, 'a', None, 'c', 'a', 'a'], name='ID'))
        >>> nm.frequency_distribution(num_items='2', normalized=False)
        [{'item': 'a', 'frequency': 3}, {'item': nan, 'frequency': 2}]
        >>> nm.frequency_distribution(num_items=2, normalized=True)
        [{'item': 'a', 'frequency': 0.5}, {'item': nan, 'frequency': 0.33333}]
        >>> nm.frequency_distribution(num_items=-2, normalized=True)
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `num_items` must be larger or equal to \
1, but it is actual value is -2.
        >>> nm.frequency_distribution(normalized='sdhaf')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `normalized` is incorrect, it must be a \
boolean, but its value is sdhaf.
        >>> nm = CategoricalMethods(pd.Series([None, None, None], name='ID'))
        >>> nm.frequency_distribution()
        [{'item': nan, 'frequency': 3}]

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the category (`item`), and its frequency of occurrence (`frequency`) in
            numerical or percentage format.
        """
        # check parameters
        if num_items is not None:
            num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        normalized = self._check_boolean_parameter(parameter=normalized, parameter_name='normalized')

        self.data_type = ResultTypes.DISTRIBUTION_FLOAT.value if normalized else ResultTypes.DISTRIBUTION_INT.value
        # compute frequency of occurrence of each element
        distribution = self.data.value_counts(dropna=False)
        # get the first `num_items` most frequent elements and normalized the answer if its necessary
        result = (distribution if num_items is None else distribution.iloc[:num_items])
        return [{
            'item': category,
            'frequency': round(frequency/self.n_rows, 5) if normalized else frequency
        } for category, frequency in result.items()]

    def pie_chart(
            self, num_items: Union[int, str, None] = 5, normalized: Union[str, bool] = False
    ) -> List[Dict[str, Union[str, int, float]]]:
        """
        Computes the frequency distribution and returns the first `num_items` most frequent elements in the
        categorical data.

        Notes
        -----
        If the number of distinct elements is less than `num_items`, another field in the answer is added to specify
        the frequency of occurrence of the other elements ('other').

        Parameters
        ----------
        num_items: int
            Number of elements to show.
        normalized: str, or bool. Default False
            Whether the output should be normalized or not.

        Raises
        ------
        IncorrectParameterError
            Wheter the parameter `num_items` is lower than 1.

        Examples
        --------
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID'))
        >>> nm.pie_chart(num_items=None)
        [{'item': 'a', 'frequency': 3}, {'item': 'b', 'frequency': 2}, {'item': 'c', 'frequency': 1}]
        >>> nm.pie_chart(num_items=None, normalized=True)
        [{'item': 'a', 'frequency': 0.5}, {'item': 'b', 'frequency': 0.33333}, {'item': 'c', 'frequency': 0.16667}]
        >>> nm.pie_chart(num_items=2, normalized='false')
        [{'item': 'a', 'frequency': 3}, {'item': 'b', 'frequency': 2}, {'item': 'OTHERS', 'frequency': 1}]
        >>> nm.pie_chart(num_items=1, normalized='True')
        [{'item': 'a', 'frequency': 0.5}, {'item': 'OTHERS', 'frequency': 0.5}]
        >>> nm.pie_chart(num_items=-5, normalized='false')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `num_items` must be larger or equal to \
1, but it is actual value is -5.
        >>> nm.pie_chart(normalized='sdhaf')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `normalized` is incorrect, it must be a \
boolean, but its value is sdhaf.
        >>> nm = CategoricalMethods(pd.Series([None, None, None], name='ID'))
        >>> nm.pie_chart(num_items=None)
        [{'item': nan, 'frequency': 3}]
        >>> nm = CategoricalMethods(pd.Series([None, None, None, 'c', 'a', 'a'], name='ID'))
        >>> nm.pie_chart(num_items=3)
        [{'item': nan, 'frequency': 3}, {'item': 'a', 'frequency': 2}, {'item': 'c', 'frequency': 1}]

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the necessary information to build a pie chart. Each dictionary is made by
            one of the items in the data (`item`), and its frequency in number or percentage (`frequency`).
        """
        # check parameter `num_items`
        if num_items is not None:
            num_items = self._check_int_parameter(parameter=num_items, parameter_name='num_items', ge=1)
        # compute frequency of each element in data
        distribution = self.frequency_distribution(num_items=None, normalized=normalized)
        # add a last field ('other') with the frequency and percentage of occurrence of the other elements in the data
        if num_items is not None and len(distribution) > num_items:
            temp = [{
                'item': 'OTHERS',
                'frequency': sum(elem['frequency'] for elem in distribution[num_items:])
            }]
            distribution = distribution[:num_items] + temp
        # return the final result
        return distribution

    def bar_chart(self, normalized: Union[bool, str] = False) -> List[Dict[str, Union[str, int, float]]]:
        """
        Calculates the frequency distribution and returns the distinct elements with their frequency of
        occurrence in number or percentage.

        Examples
        --------
        >>> nm = CategoricalMethods(pd.Series(['a', 'b', 'c', 'a', 'a', 'b'], name='ID'))
        >>> nm.bar_chart()
        [{'item': 'a', 'frequency': 3}, {'item': 'b', 'frequency': 2}, {'item': 'c', 'frequency': 1}]
        >>> nm.bar_chart(normalized='True')
        [{'item': 'a', 'frequency': 0.5}, {'item': 'b', 'frequency': 0.33333}, {'item': 'c', 'frequency': 0.16667}]
        >>> nm = CategoricalMethods(pd.Series(['female', 'male', 'male', 'female', 'female', None], name='ID'))
        >>> nm.bar_chart(normalized='false')
        [{'item': 'female', 'frequency': 3}, {'item': 'male', 'frequency': 2}, {'item': nan, 'frequency': 1}]
        >>> nm.bar_chart(normalized=True)
        [{'item': 'female', 'frequency': 0.5}, {'item': 'male', 'frequency': 0.33333}, {'item': nan, 'frequency': \
0.16667}]
        >>> nm.bar_chart(normalized='sdhaf')
        Traceback (most recent call last):
            ...
        kpi_library.errors.errors_class.IncorrectParameterError: The parameter `normalized` is incorrect, it must be a \
boolean, but its value is sdhaf.
        >>> nm = CategoricalMethods(pd.Series([None, None, None], name='ID'))
        >>> nm.frequency_distribution()
        [{'item': nan, 'frequency': 3}]

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries containing the necessary information to build a bar chart. Each dictionary is made by
            one of the elements to show (`element`), its frequency (`frequency`) and percentage (`frequency_percentage`)
            of occurrence.
        """
        return self.frequency_distribution(num_items=None, normalized=normalized)
