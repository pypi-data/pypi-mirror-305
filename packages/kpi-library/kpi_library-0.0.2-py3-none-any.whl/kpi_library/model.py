# kpi_library/general_model.py
import json
from abc import ABC, abstractmethod

import pandas as pd
from visions.functional import infer_type
from typing import Union, List, Dict, Optional

from .custom_metric import CustomSet
from .errors import IncorrectParameterError, EmptyDatasetError, DataTypeError, DatasetFormatError
from .errors import DataTypeIndexError


class ParameterModel(ABC):
    """
    Parameter model

    Parameters
    ----------
    name: str
        Name of the parameter.
    data_type: str
        Type of the value that is expecting.
    description: str
        Description of the parameter.
    possible_values: :obj:`list` of str, optional
        If its enum, this column contains the possible values that this parameter could contain.
    default_value: str, optional
        default values

    Attributes
    ----------
    _name: str
        Parameter name.
    _data_type: str
        Type of the parameter.
    _description: str
        Description of the parameter.
    _possible_values: :obj:`list` of str or None
        If its enum, this column contains the possible values that this parameter could contain.
    _default_value: str or None
        The default value.
    """
    _name: str
    _data_type: str
    _description: str
    _possible_values: Optional[List[str]]
    _default_value: Optional[str]

    @property
    def name(self) -> str:
        """str: Name of the parameter."""
        return self._name

    @property
    def data_type(self) -> str:
        """str: Data type of the value the parameter expects."""
        return self._data_type

    @property
    def description(self) -> str:
        """str: Definition of the parameter."""
        return self._description

    @property
    def possible_values(self) -> Optional[List[str]]:
        """:obj:`list` of `str`: List of possible values that the parameter can have."""
        return self._possible_values

    @property
    def default_value(self) -> Optional[str]:
        """:str: Default value of the parameter."""
        return self._default_value

    def __init__(self, name: str, data_type: str, description: str, possible_values: Optional[List[str]] = None,
                 default_value: Optional[str] = None):
        # save metric information
        self._name = name
        self._data_type = data_type
        self._description = description
        self._possible_values = possible_values
        self._default_value = default_value


class MetricModel(ABC):
    """
    Metric model according the DQV data-model standard.

    Attributes
    ----------
    _identifier: str
        Key to identify the metric.
    _keyword: str
        Name of the metric in the library.
    _title: str
        Name of the metric.
    _definition: str
        Definition of the metric.
    _expected_data_type: str
        Type of the result.
    _dimension: str
        Name of the dimension in which this metric belong to.
    _category: str
        Name of the category in which this metric belong to.

    Parameters
    ----------
    identifier: str
        Key to identify the metric.
    keyword: str
        Name of the metric in the library.
    title: str
        Name of the metric.
    definition: str
        Definition of the metric.
    expected_data_type: str
        Type of the result.
    dimension: str
        Name of the dimension in which this metric belong to.
    category: str
        Name of the category in which this metric belong to.

    Methods
    -------
    to_dqv:
        Runs the metric in the data given as parameter and returns the result in dqv format.
    run:
        Runs the metric in the data given as parameter.
    """
    _identifier: str
    _keyword: str
    _title: str
    _definition: str
    _expected_data_type: str
    _has_parameters: Optional[List[ParameterModel]]
    _dimension: str
    _category: str

    @property
    def identifier(self) -> str:
        """str: Key of the method."""
        return self._identifier

    @property
    def keyword(self) -> str:
        """str: Name of the metric in the library."""
        return self._keyword

    @property
    def title(self) -> str:
        """str: Name of the metric."""
        return self._title

    @property
    def definition(self) -> str:
        """str: Definition of the metric."""
        return self._definition

    @property
    def expected_data_type(self) -> str:
        """str: Type of the value the metric returns."""
        return self._expected_data_type

    @property
    def has_parameters(self) -> Optional[List[ParameterModel]]:
        """str: Type of the value the metric returns."""
        return self._has_parameters

    @has_parameters.setter
    def has_parameters(self, parameters: List[ParameterModel]) -> None:
        self._has_parameters = parameters

    @property
    def dimension(self) -> str:
        """str: Name of the dimension in which this metric belong to."""
        return self._dimension

    @property
    def category(self) -> str:
        """str: Name of the category in which this metric belong to."""
        return self._category

    def __init__(self, identifier: str, keyword: str, title: str, definition: str, expected_data_type: str,
                 dimension: str, category: str):
        # save metric information
        self._identifier = identifier
        self._keyword = keyword
        self._title = title
        self._definition = definition
        self._expected_data_type = expected_data_type
        self._dimension = dimension
        self._category = category
        self._has_parameters = None

    @abstractmethod
    def run(self, data: Union[pd.Series, pd.DataFrame], **kwargs):
        """
        Profiles `data`.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.
        kwargs:
            Parameters of the metric.

        Returns
        -------
        _:
            Returns the expected value after processing the data.
        """
        pass

    @abstractmethod
    def to_dqv(self, data: Union[pd.Series, pd.DataFrame], **kwargs):
        """
        Profiles `data` and returns the result following the DQV data-model standard.

        Parameters
        ----------
        data: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Data to be profiled.
        kwargs:
            Parameters of the metric.

        Returns
        -------
        _:
            Returns the expected value after processing the data in the DQV data-model format.
        """
        pass

    @staticmethod
    def _turn_dictionary_to_parameter(parameters: Dict[str, str]) -> List[Dict[str, str]]:
        """"""
        return [{"parameter_name": key, "value": json.dumps(value)} for key, value in parameters.items()]

    @staticmethod
    def __check_data_empty(data: Union[pd.Series, pd.DataFrame]) -> None:
        """
        This method studies if the given data is empty. If it is raises the EmptyDatasetError error.

        Parameters
        ----------
        data: :obj:`pandas.DataFrame` or :obj:`pandas.Series`
            Pandas object containing the data to be processed.

        Raises
        ------
        EmptyDatasetError:
            Whether the data is emtpy or not.
        """
        if data.empty:
            raise EmptyDatasetError("The given dataset is empty.", code=400)

    @staticmethod
    def _check_boolean_parameter(parameter: Union[str, bool], parameter_name: str):
        """
        This method checks if the input (parameter) is a boolean or not. In the case, the parameter format is string, it
        checks if the parameter is similar to true or false, to transform it into a boolean.

        Parameters
        ----------
        parameter: str or bool
            Element to transform into a boolean object.
        parameter_name: str
            Parameter name.

        Raises
        ------
        IncorrectParameterError
            Whether the parameter is incorrect, and it is not a boolean.

        Returns
        -------
        _: bool
            The parameter as boolean, in the case its format was string.
        """
        if isinstance(parameter, str):
            parameter = parameter.lower()
            if parameter in ["true", "false"]:
                return parameter == "true"
        elif isinstance(parameter, bool):
            return parameter

        raise IncorrectParameterError(
            f"The parameter `{parameter_name}` is incorrect, it must be a boolean, but its value is {parameter}.",
            code=400)

    @staticmethod
    def _check_int_parameter(
            parameter: Union[str, int], parameter_name: str, ge: Union[int, None] = None, le: Union[int, None] = None
    ) -> int:
        """
        This method checks if the input (parameter) is an integer or not. In the case, the parameter format is string,
        it checks if the parameter can be converted into integer.

        Parameters
        ----------
        parameter: str or int
            Element to transform into an integer object.
        parameter_name: str
            Parameter name.
        ge: int or None
            Lower limit of `parameter`, i.e., `parameter` must be greater or equal than `ge`.
        le: int or None
            Upper limit of `parameter`, i.e., `parameter` must be less or equal than `te`.

        Raises
        ------
        IncorrectParameterError
            Whether the parameter is incorrect, is not an integer or does not meet the conditions of the boundaries
            `greater_than` and `lower_than`.

        Returns
        -------
        _: int
            The parameter as integer.
        """
        # whether it is in a string format or other than integer
        if isinstance(parameter, str):
            try:
                # turn it into integer and check boundaries
                parameter = int(parameter)
            except ValueError:
                raise IncorrectParameterError(f"The parameter `{parameter_name}` must be an integer, but it's not. Its "
                                              f"value is {parameter}.", code=400)
        elif not isinstance(parameter, int):
            raise IncorrectParameterError(f"The parameter `{parameter_name}` must be an integer, but it's not. Its "
                                          f"value is {parameter}.", code=400)
        # check boundary conditions (`greater_than`, `lower_than`)
        if ge is not None and parameter < ge:
            raise IncorrectParameterError(f"The parameter `{parameter_name}` must be larger or equal to {ge}"
                                          f", but it is actual value is {parameter}.", code=400)

        if le is not None and parameter > le:
            raise IncorrectParameterError(f"The parameter `{parameter_name}` must be less or equal to {le}"
                                          f", but it is actual value is {parameter}.", code=400)
        # return correct value
        return parameter

    @staticmethod
    def _check_float_parameter(
            parameter: Union[str, float], parameter_name: str, ge: Union[int, None] = None, le: Union[int, None] = None
    ) -> float:
        """
        This method checks if the input (parameter) is a float or not. In the case, the parameter format is string,
        it checks if the parameter can be converted into float.

        Parameters
        ----------
        parameter: str or float
            Element to transform into a float object.
        parameter_name: str
            Parameter name.
        ge: int or None
            Lower limit of `parameter`, i.e., `parameter` must be greater or equal than `ge`.
        le: int or None
            Upper limit of `parameter`, i.e., `parameter` must be less or equal than `te`.

        Raises
        ------
        IncorrectParameterError
            Whether the parameter is incorrect, is not a float or does not meet the conditions of the boundaries `ge`
            and `le`.

        Returns
        -------
        _: float
            The parameter as float.
        """
        # whether it is in a string format or other than float
        if isinstance(parameter, str):
            try:
                # turn it into integer and check boundaries
                parameter = float(parameter)
            except ValueError:
                raise IncorrectParameterError(f"The parameter `{parameter_name}` must be a float, but it's not. Its "
                                              f"value is {parameter}.", code=400)
        elif not isinstance(parameter, float):
            raise IncorrectParameterError(f"The parameter `{parameter_name}` must be a float, but it's not. Its value"
                                          f" is {parameter}.", code=400)
        # check boundary conditions (`greater_than`, `lower_than`)
        if ge is not None and parameter < ge:
            raise IncorrectParameterError(f"The parameter `{parameter_name}` must be larger or equal to {ge}"
                                          f", but it is actual value is {parameter}.", code=400)

        if le is not None and parameter > le:
            raise IncorrectParameterError(f"The parameter `{parameter_name}` must be less or equal to {le}"
                                          f", but it is actual value is {parameter}.", code=400)
        # return correct value
        return parameter

    @staticmethod
    def _check_enum_parameter(parameter: Union[str, int], parameter_name: str, values: List[str]) -> None:
        """
        This method checks if the input (parameter) is any of the values specified in `values`.

        Parameters
        ----------
        parameter: str or int
            Element to transform into an integer object.
        parameter_name: str
            Parameter name.
        values: :obj:`list` of str
            List of possible values in parameter.

        Raises
        ------
        IncorrectParameterError
            Whether the parameter is incorrect.
        """
        # whether it is in a string format or other than integer
        if parameter not in values:
            raise IncorrectParameterError(
                f'The parameter `{parameter_name}` is not correct, it should be any of the following values: {values}, '
                f'but it is {parameter}.', code=400)

    def _check_numeric_data(self, data: pd.Series) -> pd.Series:
        """
        Check the correct format and type of the dataset.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Pandas object containing the numeric data to be processed.

        Raises
        ------
        EmptyDatasetError
            Whether the data is empty or not.
        DataTypeError
            If the data type of `dataset` is not numeric.

        Returns
        -------
        dataset: :obj:`pandas.Series`
            Pandas object containing the numeric data to be processed.
        """
        # check whether the data is empty
        self.__check_data_empty(data)
        # drop null values and check if dataset is empty
        srs = data.dropna(inplace=False)
        if not srs.empty and str(srs.dtype) not in ['int64', 'float64']:
            raise DataTypeError(f'The column format is incorrect, the values should be numeric but they are not. The '
                                f'type of the data is {srs.dtype}.', code=400)
        # return the data with the null values deleted
        return srs

    def _check_categorical_data(self, data: pd.Series) -> pd.Series:
        """
        Check the correct format and type of categorical data.

        Notes
        -----
        This metric checks if the data are not floats or dates. It allows text and integer data.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Pandas object containing the categorical data to be processed.

        Raises
        ------
        EmptyDatasetError
            Whether the data is empty or not.
        DataTypeError
            If the data type of the entries in `data` is not numeric or dates.

        Returns
        -------
        data: :obj:`pandas.Series`
            Pandas object containing the categorical data to be processed.
        """
        # check whether the data is empty
        self.__check_data_empty(data)
        # drop null values
        srs = data.dropna(inplace=False)
        # check if the data type is correct
        typeset = CustomSet()
        data_type = str(infer_type(srs.iloc[:5], typeset))
        if not srs.empty and data_type not in ['Generic', 'Categorical', 'String', 'Integer']:
            raise DataTypeError(f"The column format is incorrect, the values should be categories but they are "
                                f"`{data_type}`.", code=400)
        # return the data as category format
        return srs.astype('category')

    def _check_date_data(self, data: pd.Series, date_format: Optional[str]) -> pd.Series:
        """
        Check the correct format and type of time data.

        Notes
        -----
        This metric checks if the data are not numeric and if it is not, it tries to turn it into date format. In the
        case, the given or inferred format is incorrect, all values that cannot be transformed are turned into null
        values.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Pandas object containing the categorical data to be processed.
        date_format: str
            The format to parse time, e.g. "%d/%m/%Y". See strftime documentation for more information on choices.

        Raises
        ------
        EmptyDatasetError
            Whether the data is empty or not.
        DataTypeError
            If the data type of the entries in `data` are numeric.

        Returns
        -------
        data: :obj:`pandas.Series`
            Pandas object containing time data to be processed.
        """
        # check whether the data is empty
        self.__check_data_empty(data)
        # drop null values
        srs: pd.Series = data.dropna(inplace=False)
        # check if data are numbers, if they are, launch exception
        if str(srs.dtype) in ["float64", "int64"]:
            raise DataTypeError("The given column should follow a date_methods format and is currently a numerical"
                                " column.", code=400)
        # if they are not, turn entries into date values
        return pd.to_datetime(srs, errors='coerce', format=date_format)

    def _check_text_data(self, data: pd.Series) -> pd.Series:
        """
        This method checks if the dataset is emtpy and if it is not, it cleans the data and returns the values as
        strings.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Pandas object containing the categorical data to be processed.

        Raises
        ------
        EmptyDatasetError
            Whether the data is empty or not.

        Returns
        -------
        data: :obj:`pandas.Series`
            Pandas object containing the text data to be processed.
        """
        self.__check_data_empty(data)
        return data.dropna(inplace=False).astype('string')

    def _check_bi_data(self, data: pd.DataFrame, feature_one: str, feature_two: str):
        # check emptiness of the data
        self.__check_data_empty(data)
        # check parameters feature_one and feature_two
        if feature_one is None or feature_one not in data.columns:
            raise IncorrectParameterError(f"The name of the column `{feature_one}` is incorrect.", code=400)
        if feature_two is None or feature_two not in data.columns:
            raise IncorrectParameterError(f"The name of the column `{feature_two}` is incorrect.", code=400)

    def _check_timeseries(
            self, data: pd.DataFrame, feature_one: str, feature_two: str, date_format: Optional[str]) -> pd.Series:
        """
        Checks if the given data corresponds with a time-series object. For that, it makes the following tests: whether
        the dataset is empty or contains too much information (more than two columns of data),---

        Parameters
        ----------
        data: :obj:`pandas.DataFrame`
            Pandas object containing the data that must be processed.
        feature_one: str
            Name of the index column that should contain time data.
        feature_two: str
            Name of the data column that should contain numeric data.
        date_format: str, optional.
            The format to parse time, e.g. "%d/%m/%Y". See strftime documentation for more information on choices.

        Raises
        ------
        EmptyDatasetError
            Whether the dataset is empty or not.
        DataTypeError
            Whether the data column (feature_two) does not contain numeric data.
        DataTypeIndexError
            Whether the index column (feature_one) contains data that are not time values, or whether the transformation
            to time values could not be carried out because the given or inferred format is incorrect.

        Returns
        -------
        _: :obj:`pandas.Series`
            Pandas object containing the time series.
        """
        # check whether the dataset is empty
        self._check_bi_data(data=data, feature_one=feature_one, feature_two=feature_two)
        # check correct type of the column data and the index
        types = data.dtypes
        if str(types[feature_two]) not in ['int64', 'float64']:
            raise DataTypeError(f'The column {feature_two} has an incorrect format, it must be a numeric '
                                f'variable, but it is a {types[feature_two]} variable.', code=400)
        if str(types[feature_one]) in ['int64', 'float64']:
            raise DataTypeIndexError(f'The column {feature_one} has an incorrect format, it must be a date '
                                     f'variable, but it is a {types[feature_one]} variable.', code=400)
        # build the time series (transform the index column into time data and drop null values in feature_one)
        ts = data.copy()
        ts[feature_one] = pd.to_datetime(ts[feature_one], errors='coerce', format=date_format)
        ts = ts.dropna(subset=[feature_one], inplace=False)
        return ts.set_index(feature_one, drop=True, inplace=False)[feature_two]
