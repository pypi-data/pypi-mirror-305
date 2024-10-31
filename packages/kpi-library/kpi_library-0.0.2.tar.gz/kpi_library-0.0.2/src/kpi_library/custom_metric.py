# kpi_library/general/custom_metric.py
from visions.typesets import VisionsTypeset
from visions.types import Generic, Object, Float, Integer, Categorical, Date, DateTime, Time, String


class CustomSet(VisionsTypeset):
    """
    Typeset that exclusively supports the types implemented in iti_ds_eda, i.e.:

    - Generic
    - Float
    - Integer
    - Categorical
    - DateTime
    - Date
    - Time
    - String
    """
    def __init__(self):
        types = {Generic, Object, Float, Integer, Categorical, DateTime, Date, Time, String}
        super().__init__(types)
