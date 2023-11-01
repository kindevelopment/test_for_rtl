from enum import Enum


class GroupTypeChoices(str, Enum):
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'


class GroupTypeFormat(str, Enum):
    HOUR = '%Y-%m-%dT%H:00:00'
    DAY = '%Y-%m-%dT00:00:00'
    MONTH = '%Y-%m-01T00:00:00'
