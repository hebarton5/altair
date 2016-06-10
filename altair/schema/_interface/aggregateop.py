# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class AggregateOp(T.Enum):
    """One of ['values', 'count', 'valid', 'missing', 'distinct', 'sum', 'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'median', 'q1', 'q3', 'modeskew', 'min', 'max', 'argmin', 'argmax']"""
    def __init__(self, default_value=T.Undefined, **metadata):
        super(AggregateOp, self).__init__(['values', 'count', 'valid', 'missing', 'distinct', 'sum', 'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'median', 'q1', 'q3', 'modeskew', 'min', 'max', 'argmin', 'argmax'],
                                    default_value=default_value,
                                    **metadata)