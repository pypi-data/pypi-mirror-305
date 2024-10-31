# kpi_library/numeric/box_plot.py
import json
import numpy as np
import pandas as pd

from typing import Optional, Dict, List, Union
from ..model import MetricModel
from ..errors import DataTypeError, EmptyDatasetError
from ..result_types import ResultTypes


class NumericBoxPlot(MetricModel):
    """
    This metric computes the mean value of a numeric column.

    Example
    -------
    >>> c = NumericBoxPlot()
    >>> srs = pd.Series([1,2,3,4,5,6,7])
    >>> c.run(srs)
    {'min': 1.0, 'max': 7.0, 'first_quartile': 2.5, 'median': 4.0, 'third_quartile': 5.5, 'outliers': []}
    >>> c.to_dqv(srs)
    [{'dqv_isMeasurementOf': 'numeric.box_plot', 'dqv_computedOn': '', 'rdf_datatype': 'Map<String,String>', 'ddqv_has\
Parameters': [], 'dqv_value': '{"min": 1.0, "max": 7.0, "first_quartile": 2.5, "median": 4.0, "third_quartile": 5.5, \
"outliers": []}'}]
    >>> c.to_dqv(pd.Series())
    [{'dqv_isMeasurementOf': 'numeric.box_plot', 'dqv_computedOn': '', 'rdf_datatype': 'Error', 'ddqv_hasParam\
eters': [], 'dqv_value': 'null'}]
    >>> c.run(pd.Series([None, None, None]))
    >>> c.to_dqv(pd.Series([None, None, None]))
    [{'dqv_isMeasurementOf': 'numeric.box_plot', 'dqv_computedOn': '', 'rdf_datatype': 'Map<String,String>', 'ddqv_ha\
sParameters': [], 'dqv_value': 'null'}]
    """
    def __init__(self):
        super(NumericBoxPlot, self).__init__(
            identifier='numeric.box_plot',
            keyword='NumericBoxPlot',
            title='Box Plot',
            definition='Necessary values to build a box plot.',
            expected_data_type=str(ResultTypes.BOX_PLOT.value),
            dimension='profile',
            category='inherent'
        )

    def to_dqv(self, data: pd.Series, **kwargs):
        # run method
        try:
            result = self.run(data, **kwargs)
        except (EmptyDatasetError, DataTypeError):
            # error found
            return [{
                'dqv_isMeasurementOf': f'{self.identifier}',
                'dqv_computedOn': "",
                'rdf_datatype': "Error",
                'ddqv_hasParameters': [],
                'dqv_value': json.dumps(None)
            }]
        # no error, result obtained
        return [{
            'dqv_isMeasurementOf': f'{self.identifier}',
            'dqv_computedOn': "" if data.name is None else data.name,
            'rdf_datatype': self.expected_data_type,
            'ddqv_hasParameters': [],
            'dqv_value': json.dumps(result)
        }]

    def run(self, data: pd.Series, **kwargs) -> Optional[Dict[str, Union[str, List[Union[int, float]]]]]:
        """
        This method returns the necessary statistics to build a box plot of the numeric data.

        Parameters
        ----------
        data: :obj:`pandas.Series`
            Object containing the data to be processed.

        Returns
        -------
        _: :obj:`dict`
            Statistics to build a box plot.
        """
        srs = self._check_numeric_data(data)
        # check if dataset is empty
        if srs.empty:
            return None
        # obtain statistics
        srs = srs.to_numpy()
        statistics = np.percentile(a=srs, q=[0, 25, 50, 75, 100])
        # get limits
        iqr_stat = statistics[3] - statistics[1]
        upper = statistics[3] + 1.5 * iqr_stat
        lower = statistics[1] - 1.5 * iqr_stat
        # return the element of the box plot
        return {
            'min': statistics[0],
            'max': statistics[4],
            'first_quartile': statistics[1],
            'median': statistics[2],
            'third_quartile': statistics[3],
            'outliers': srs[(srs > upper) | (srs < lower)].tolist()
        }
