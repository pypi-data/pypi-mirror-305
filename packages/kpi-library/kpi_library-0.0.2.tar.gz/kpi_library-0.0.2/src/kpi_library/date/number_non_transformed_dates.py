# kpi_library/date/number_non_transformed_dates.py
import json
import pandas as pd

from typing import Optional
from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class DateNumberNonTransformedDates(MetricModel):
    """
    This metric computes the number of values that could not be transformed into the given or inferred date format.

    Example
    -------
    >>> srs = pd.Series(["2022-20-03 00:00:00", "2022-21-03 00:00:00", "2022-22-03 00:00:00", "2022-23-03 00:00:00", \
    "2022-24-03 00:00:00", "2022-25-03 00:00:00"], name='timestamp')
    >>> c = DateNumberNonTransformedDates()
    >>> c.run(srs, date_format=r'%Y-%d-%m %H:%M:%S')
    0
    >>> c.run(srs)
    6
    >>> srs = pd.Series(["2022-20-03", "2022-03-21", "2022-22-03", "2022-23-03", "2022-24-03", "2022-25-03"])
    >>> c.run(srs, date_format=r'%Y-%d-%m')
    1
    >>> c.to_dqv(srs, date_format=r'%Y-%d-%m')
    [{'dqv_isMeasurementOf': 'date.number_non_transformed_dates', 'dqv_computedOn': '', 'rdf_datatype': 'Integer', \
'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%d-%m"'}], 'dqv_value': '1'}]
    >>> srs = pd.Series([None, None, None], name='timestamp')
    >>> c.run(srs)
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'date.number_non_transformed_dates', 'dqv_computedOn': 'timestamp', 'rdf_datatype': 'In\
teger', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': 'null'}], 'dqv_value': 'null'}]
    >>> c.to_dqv(srs, date_format='%Y-%d-%m')
    [{'dqv_isMeasurementOf': 'date.number_non_transformed_dates', 'dqv_computedOn': 'timestamp', 'rdf_datatype': 'In\
teger', 'ddqv_hasParameters': [{'parameter_name': 'date_format', 'value': '"%Y-%d-%m"'}], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(DateNumberNonTransformedDates, self).__init__(
            identifier='date.number_non_transformed_dates',
            keyword='DateNumberNonTransformedDates',
            title='Number of non-transformed dates',
            definition='Number of non-transformed dates.',
            expected_data_type=str(ResultTypes.INT.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='date_format', data_type=str(ResultTypes.STRING.value), possible_values=None,
                           default_value=None, description='The format to parse the dates.')]

    def to_dqv(self, data: pd.Series, **kwargs):
        params = {'date_format': kwargs.get('date_format', None)}
        # run method
        try:
            result = self.run(data, **kwargs)
        except (EmptyDatasetError, DataTypeError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': "" if data.name is None else data.name,
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.Series, **kwargs) -> Optional[float]:
        """
        This method returns the number of entries that could not be transformed into dates.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: int, optional.
            Number of non-transformed dates.
        """
        # check data
        date_format = kwargs.get('date_format', None)
        srs = self._check_date_data(data, date_format)
        # check if dataset is empty
        if srs.empty:
            return None
        # compute statistic
        return int(srs.isna().sum())
