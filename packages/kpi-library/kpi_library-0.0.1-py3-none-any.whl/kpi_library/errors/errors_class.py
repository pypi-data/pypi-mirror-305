# kpi_library/errors/errors_class.py


# New exceptions (examples)
class IncorrectParameterError(Exception):
    """
    The IncorrectParameterError object contains the error message of getting incorrect values in the input parameter.

    Parameters
    ----------
    msg: str
        Human readable string describing the exception.
    code: :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg: str
        Human readable string describing the exception.
    code: int
        Numeric error code.
    """
    __code: int

    def __init__(self, msg: str, code: int):
        super(IncorrectParameterError, self).__init__(msg)

        self.msg = msg
        self.code = code

    @property
    def code(self) -> int:
        """int: Numeric error code."""
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code


class DataTypeIndexError(Exception):
    """
    Exception raised when the index of the dataset is incorrect, i.e., when the index of a time series does not contain
    date_methods values.

    Parameters
    ----------
    msg: str
        Human readable string describing the exception.
    code: :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg: str
        Human readable string describing the exception.
    code: int
        Numeric error code.
    """
    __code: int

    def __init__(self, msg: str, code: int):
        super(DataTypeIndexError, self).__init__(msg)

        self.msg = msg
        self.code = code

    @property
    def code(self) -> int:
        """int: Numeric error code."""
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code


class DataTypeError(Exception):
    """
    Exception raised when the specified data types is incorrect.

    Parameters
    ----------
    msg: str
        Human readable string describing the exception.
    code: :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg: str
        Human readable string describing the exception.
    code: int
        Numeric error code.
    """
    __code: int

    def __init__(self, msg: str, code: int):
        super(DataTypeError, self).__init__(msg)
        self.msg = msg
        self.code = code

    @property
    def code(self) -> int:
        """int: Numeric error code."""
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code


class DatasetFormatError(Exception):
    """
    Exception raised when the specified data set contains more data that necessary or does not contain sufficient data.

    Parameters
    ----------
    msg: str
        Human readable string describing the exception.
    code: :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg: str
        Human readable string describing the exception.
    code: int
        Numeric error code.
    """
    __code: int

    def __init__(self, msg: str, code: int):
        super(DatasetFormatError, self).__init__(msg)
        self.msg = msg
        self.code = code

    @property
    def code(self) -> int:
        """int: Numeric error code."""
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code


class EmptyDatasetError(Exception):
    """
    Exception raised when the given dataset is empty.

    Parameters
    ----------
    msg: str
        Human readable string describing the exception.
    code: :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg: str
        Human readable string describing the exception.
    code: int
        Numeric error code.
    """
    __code: int

    def __init__(self, msg: str, code: int):
        super(EmptyDatasetError, self).__init__(msg)
        self.msg = msg
        self.code = code

    @property
    def code(self) -> int:
        """int: Numeric error code."""
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code
