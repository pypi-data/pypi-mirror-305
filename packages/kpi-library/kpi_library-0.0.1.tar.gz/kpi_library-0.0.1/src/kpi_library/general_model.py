# kpi_library/general_model.py
from abc import ABC, abstractmethod

import pandas as pd
from typing import Union, List, Dict
from .errors import IncorrectParameterError, EmptyDatasetError
from .result_types import ResultTypes


class GeneralMethodModel(ABC):
    """
    Structure of the objects in the modules which process a column or the whole table (regarding the data type of each
    column, i.e., the general profiler module).

    Attributes
    ----------
    _data: :obj:`pandas.DataFrame` or :obj:`pandas.Series`
        Object containing the data to be processed.
    _data_type: :obj:`ResultType` or None
        Object containing the type of data of the last value returned.
    """
    _data: Union[pd.Series, pd.DataFrame]
    _data_type: Union[ResultTypes, None]
    _class_name: str

    @property
    def data(self) -> Union[pd.Series, pd.DataFrame]:
        """:obj:`pandas.Series` or :obj:`pandas.DataFrame`: object containing the data to be processed."""
        return self._data

    @data.setter
    def data(self, dataset: Union[pd.Series, pd.DataFrame]):
        self._data = dataset

    @property
    def data_type(self) -> ResultTypes:
        """:obj:`ResultTypes`: object containing the data type of metric response."""
        return self._data_type

    @data_type.setter
    def data_type(self, data_type: ResultTypes):
        self._data_type = data_type

    def __init__(self, class_name: str, dataset: Union[pd.Series, pd.DataFrame]):
        """
        Create a GeneralMethods object which stores the data to be processed in a pandas object.

        Parameters
        ----------
        class_name: str
            Name of the class that has been implemented.
        dataset: :obj:`pandas.Series` or :obj:`pandas.DataFrame`
            Pandas object containing the data to be processed.
        """
        # check if the dataset is empty
        if dataset.empty:
            raise EmptyDatasetError("The given dataset is empty.", code=400)
        # save dataset information
        self._class_name = class_name
        self.data = dataset
        self.data_type = None

    def get(self, function_name: str):
        """
        Gets the function specified in `function_name` and returns it.

        Parameters
        ----------
        function_name: str
            Name of the function that it is needed.

        Raises
        ------
        AttributeError
            Whether the method exists in the class.

        Returns
        -------
        :function:`GeneralMethods`
            Returns a function of the class specified by `function_name`.
        """
        return getattr(self, function_name, None)

    @abstractmethod
    def to_dqv(self, method_name: str, parameters: List[Dict[str, str]]):
        """
        This method process the data with the given method (`method_name`) and parameters (`porameters`) and returns the
        result with the DQV notation.

        Parameters
        ----------
        method_name: str
            Name of the method that must be run.
        parameters: :obj:`list` of :obj:`dict`
            List of dictionaries containing the parameter information, its name (`parameter_name`) and its value
            (`value`).

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            Result, in dqv format, after processing the data with the specified method and parameters.
        """
        pass

    @staticmethod
    def _turn_parameter_to_dictionary(parameters: List[Dict[str, str]]) -> Dict[str, str]:
        """"""
        return {element["parameter_name"]: element["value"] for element in parameters}

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
