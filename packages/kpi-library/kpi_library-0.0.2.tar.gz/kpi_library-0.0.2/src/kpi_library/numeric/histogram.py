# kpi_library/numeric/histogram.py
import json
import numpy as np
import pandas as pd

from ..model import MetricModel, ParameterModel
from ..errors import DataTypeError, EmptyDatasetError, IncorrectParameterError
from ..result_types import ResultTypes


class NumericHistogram(MetricModel):
    """
    This metric computes the necessary information to visualize the data in a histogram.

    Note
    ----
    The histogram requires the number of bins to be visualized. If not specified, ten bins will be displayed.

    Examples
    --------
    >>> data = pd.Series([1,2,3,4,5,6,7], name='ID')
    >>> nm = NumericHistogram()
    >>> nm.run(data, num_bins=3)
    [{'limits': '[1.0, 3.0)', 'frequency': 2}, {'limits': '[3.0, 5.0)', 'frequency': 2}, {'limits': '[5.0, 7.0]', '\
frequency': 3}]
    >>> nm.run(data, num_bins='skfj')
    Traceback (most recent call last):
        ...
    kpi_library.errors.errors_class.IncorrectParameterError: The parameter `num_bins` must be an integer, but it's \
not. Its value is skfj.
    >>> nm.run(data, num_bins=-2)
    Traceback (most recent call last):
        ...
    kpi_library.errors.errors_class.IncorrectParameterError: The parameter `num_bins` must be larger or equal to 2, \
but it is actual value is -2.
    >>> nm.run(pd.Series(), num_bins=-2)
    Traceback (most recent call last):
        ...
    kpi_library.errors.errors_class.EmptyDatasetError: The given dataset is empty.
    >>> srs = pd.Series([None,None, None, None])
    >>> nm.run(srs, num_bins=3)
    []
    >>> nm.to_dqv(srs, num_bins=3)
    [{'dqv_isMeasurementOf': 'numeric.histogram', 'dqv_computedOn': '', 'rdf_datatype': 'List<Map<String,String>>', \
'ddqv_hasParameters': [{'parameter_name': 'num_bins', 'value': 3}], 'dqv_value': '[]'}]
    """
    def __init__(self):
        super(NumericHistogram, self).__init__(
            identifier='numeric.histogram',
            keyword='NumericHistogram',
            title='Histogram',
            definition='Necessary information to display a histogram of the given data.',
            expected_data_type=str(ResultTypes.HISTOGRAM.value),
            dimension='profile',
            category='inherent'
        )
        self.has_parameters = [
            ParameterModel(name='num_bins', data_type=str(ResultTypes.INT.value), description='Number of bins.',
                           possible_values=None, default_value='10')]

    def to_dqv(self, data: pd.Series, **kwargs):
        """"""
        params = {'num_bins': kwargs.get('num_bins', '10')}
        try:
            # get result
            result = self.run(data, **params)
        except (IncorrectParameterError, DataTypeError, EmptyDatasetError):
            # error
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
                'dqv_value': None
            }]
        # no error
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': '' if data.name is None else data.name,
            'rdf_datatype': ResultTypes.HISTOGRAM.value,
            'ddqv_hasParameters': self._turn_dictionary_to_parameter(parameters=params),
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.Series, **kwargs):
        """
        This method computes the necessary information to visualize the given data in a histogram.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Data to be processed.
        kwargs: :obj:`dict`
            Dictionary containing the number of bins that must be displayed. The default value of the number of bins to
            display is 10 in the case the number is not specified (`num_bins`).

        Raises
        ------
        IncorrectParameterError
            If num_bins is less than 2, or it is not a number.

        Returns
        -------
        _: :obj:`list` of :obj:`dict`
            List of dictionaries, where `limits` is the boundaries of the bin and `frequency` is the number of element
            that fit in it.
        """
        # check data
        srs = self._check_numeric_data(data)
        # check parameter (num_bins)
        num_bins = self._check_int_parameter(parameter=kwargs.get('num_bins', 10), parameter_name='num_bins', ge=2)
        # check if data is empty
        if srs.empty:
            return []
        # get histogram values
        y_freq, x_bins = np.histogram(srs, bins=num_bins)
        bins = zip(x_bins[:-2], x_bins[1:-1])
        result = [
            {'limits': f'[{round(b[0], 4)}, {round(b[1], 4)})', 'frequency': int(freq)}
            for b, freq in zip(bins, y_freq[:-1])
        ] + [{'limits': f'[{round(x_bins[-2], 4)}, {round(x_bins[-1], 4)}]', 'frequency': int(y_freq[-1])}]
        # return
        return result
