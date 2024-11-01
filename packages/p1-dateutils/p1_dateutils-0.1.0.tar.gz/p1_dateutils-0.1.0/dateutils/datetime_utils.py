import sys
from datetime import date as _date
from datetime import datetime as _datetime
from datetime import time as _time
from datetime import timedelta
from datetime import tzinfo
from typing import Any
from typing import Callable
from zoneinfo import ZoneInfo

from django.utils.timezone import get_default_timezone
if sys.version_info[0] < 3:
    DEFAULT_TIMEZONE: tzinfo = get_default_timezone()
else:
    DEFAULT_TIMEZONE = ZoneInfo('Asia/Jakarta')


class timeutils:

    @classmethod
    def make_aware(cls, time: _time) -> _time:
        if time.tzinfo is None:
            time.replace(tzinfo=DEFAULT_TIMEZONE)
        return time

    @classmethod
    def hour(cls, time: _time) -> int:
        return cls.make_aware(time).hour

    @classmethod
    def minute(cls, time: _time) -> int:
        return cls.make_aware(time).minute

    @classmethod
    def second(cls, time: _time) -> int:
        return cls.make_aware(time).second

    @classmethod
    def microsecond(cls, time: _time) -> int:
        return cls.make_aware(time).microsecond

    @classmethod
    def tzinfo(cls, time: _time) -> tzinfo | None:
        return time.tzinfo

    @classmethod
    def fold(cls, time: _time) -> int:
        return time.fold

    @classmethod
    def isoformat(cls, time: _time, timespec: str = 'auto') -> str:
        return cls.make_aware(time).isoformat(timespec)

    @classmethod
    def fromisoformat(cls, time_string: str) -> _time:
        res = _time.fromisoformat(time_string)
        return cls.make_aware(res)

    @classmethod
    def strftime(cls, time: _time, fmt: str) -> str:
        return cls.make_aware(time).strftime(fmt)

    @classmethod
    def utcoffset(cls, time: _time) -> timedelta | None:
        return time.utcoffset()

    @classmethod
    def tzname(cls, time: _time) -> str | None:
        return time.tzname()

    @classmethod
    def dst(cls, time: _time) -> timedelta | None:
        return time.dst()

    @classmethod
    def replace(cls, time: _time, hour: int | None = None, minute: int | None = None, second: int | None = None, microsecond: int | None = None,
                tzinfo: bool = True, *, fold: int | None = None) -> _time:
        return time.replace(hour, minute, second, microsecond, tzinfo, fold=fold)


class datetimeutils:

    @classmethod
    def make_aware(cls, datetime: _datetime) -> _datetime:
        if datetime.tzinfo is None:
            datetime.replace(tzinfo=DEFAULT_TIMEZONE)
        return datetime

    @classmethod
    def today(cls, datetime) -> _datetime:
        return cls.make_aware(datetime).today()

    @classmethod
    def fromordinal(cls, n: int) -> _datetime:
        return _datetime.fromordinal(n)

    @classmethod
    def fromisoformat(cls, date_string: str) -> _datetime:
        return _datetime.fromisoformat(date_string)

    @classmethod
    def fromisocalendar(cls, year: int, week: int, day: int) -> _datetime:
        return _datetime.fromisocalendar(year, week, day)

    @classmethod
    def strftime(cls, datetime: _datetime, fmt: str) -> str:
        return datetime.strftime(fmt)

    @classmethod
    def year(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).year

    @classmethod
    def month(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).month

    @classmethod
    def day(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).day

    @classmethod
    def timetuple(cls, datetime: _datetime) -> Any:
        return cls.make_aware(datetime).timetuple()

    @classmethod
    def toordinal(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).toordinal()

    @classmethod
    def weekday(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).weekday()

    @classmethod
    def isoweekday(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).isoweekday()

    @classmethod
    def isocalendar(cls, datetime: _datetime) -> Any:
        return cls.make_aware(datetime).isocalendar()

    @classmethod
    def hour(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).hour

    @classmethod
    def minute(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).minute

    @classmethod
    def second(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).second

    @classmethod
    def microsecond(cls, datetime: _datetime) -> int:
        return cls.make_aware(datetime).microsecond

    @classmethod
    def now(cls, tz=None) -> _datetime:
        if tz is not None:
            return _datetime.now(tz)
        return cls.make_aware(_datetime.now())

    @classmethod
    def utcnow(cls) -> _datetime:
        return _datetime.utcnow()

    @classmethod
    def combine(cls, date: _date, time: _time, tzinfo=True) -> _datetime:
        if tzinfo:
            return _datetime.combine(date, time, tzinfo)
        return cls.make_aware(_datetime.combine(date, time, tzinfo))

    @classmethod
    def timestamp(cls, datetime: _datetime) -> float:
        return cls.make_aware(datetime).timestamp()

    @classmethod
    def utctimetuple(cls, timestamp: float) -> _datetime:
        return _datetime.utcfromtimestamp(timestamp)

    @classmethod
    def date(cls, datetime: _datetime) -> _date:
        return cls.make_aware(datetime).date()

    @classmethod
    def time(cls, datetime: _datetime) -> _time:
        return cls.make_aware(datetime).time()

    @classmethod
    def timetz(cls, datetime: _datetime) -> _time:
        return cls.make_aware(datetime).timetz()

    @classmethod
    def replace(cls, datetime: _datetime, year=None, month=None, day=None, hour=None,
                minute=None, second=None, microsecond=None, tzinfo=True,
                *, fold=None):
        return cls.make_aware(datetime).replace(year, month, day, hour,
                                                minute, second, microsecond, tzinfo, fold=fold)

    @classmethod
    def astimezone(cls, datetime: _datetime, tz=None) -> _datetime:
        return datetime.astimezone(tz)

    @classmethod
    def ctime(cls, datetime: _datetime) -> str:
        return cls.make_aware(datetime).ctime()

    @classmethod
    def isoformat(cls, datetime: _datetime, sep='T', timespec='auto') -> str:
        return cls.make_aware(datetime).isoformat(sep, timespec)

    @classmethod
    def strptime(cls, datetime: _datetime, date_string, format) -> _datetime:
        return cls.make_aware(datetime).strptime(date_string, format)

    @classmethod
    def utcoffset(cls, datetime: _datetime) -> Callable | timedelta | None:
        return cls.make_aware(datetime).utcoffset

    @classmethod
    def tzname(cls, datetime: _datetime) -> Callable | timedelta | None:
        return cls.make_aware(datetime).tzname

    @classmethod
    def dst(cls, datetime: _datetime) -> Callable | timedelta | None:
        return cls.make_aware(datetime).dst
