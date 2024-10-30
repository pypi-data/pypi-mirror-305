# Adaptyper

Старается конвертировать один тип данных в другой.

Обработка пользовательских данных из не строго типизированных значений.

```py
from adaptyper import convert

# to_type
convert.to_type(convert.ValueType.BOOL, 'FaLsE')  # False
convert.to_type('bool', 'some_str_value')  # True
convert.to_type('bool', 0)  # False
convert.to_type('bool', 1.0)  # True

convert.to_type(convert.ValueType.STR, True)  # "TRUE"
convert.to_type('str', -1)  # "-1"

convert.to_type(convert.ValueType.FLOAT, True)  # 1.0
convert.to_type('float', 'FaLsE')  # 0.0
convert.to_type('float', '.5')  # 0.5
convert.to_type('float', -1)  # -1.0

convert.to_type(convert.ValueType.INT, True)  # 1
convert.to_type('int', '1.5')  # 1
convert.to_type('int', '1.5', True)  # 2

convert.to_type(convert.ValueType.DATETIME, '2011-11-04')  # datetime(2011, 11, 4, 0, 0))
convert.to_type('datetime','4.11.2011', '%d.%m.%Y')  # datetime(2011, 11, 4, 0, 0)

# bool
convert.to_bool('')  # False
convert.to_bool('0')  # False
convert.to_bool('FaLsE')  # False
convert.to_bool('some_str_value')  # True

# str
convert.to_str(True)  # "TRUE"
convert.to_str('some_str_value')  # "some_str_value"
convert.to_str(1)  # "1"
convert.to_str(-1)  # "-1"
convert.to_str(123.456)  # "123.456"
convert.to_str(-123.456)  # "-123.456"

# float
convert.to_float(None)  # None
convert.to_float('')  # None
convert.to_float('123,456')  # 123.456
convert.to_float(' 123\xa0456\xa0')  # 123456.0
convert.to_float('tRuE')  # 1.0
convert.to_float(True)  # 1.0
convert.to_float(1)  # 1.0
convert.to_float('.3')  # 0.3

# int
# работает через float,
# банковское округление (по-умолчанию False)
convert.to_int('.6', False)  # 0
convert.to_int('.6', True)  # 1
convert.to_int('1.5', False)  # 1
convert.to_int('1.5', True)  # 2

# datetime
convert.to_datetime(None)  # None
convert.to_datetime('')  # None
convert.to_datetime('2011-11-04')  # datetime(2011, 11, 4, 0, 0)
convert.to_datetime('4.11.2011', '%d.%m.%Y')  # datetime(2011, 11, 4, 0, 0)
```