import re
from datetime import datetime
from enum import (
    Enum,
    auto,
)


class ConvertValueException(Exception): ...


class PreActionException(Exception): ...


class ConvertToFloatException(Exception): ...


class ConvertToIntException(Exception): ...


class ConvertToStrException(Exception): ...


class ConvertToBoolException(Exception): ...


class NotSupportedType(Exception): ...


class ValueType(Enum):
    FLOAT = auto()
    INT = auto()
    STR = auto()
    BOOL = auto()
    DATETIME = auto()


def pre_action(value, func, *args, **kwargs):
    """
    Выполнение пользовательской функции перед конвертацией

    :param value: данные
    :param func: пользовательская функция
    :return: обработанные пользовательской функцией данные
    """
    try:
        return func(value, *args, **kwargs)
    except Exception as e:
        raise PreActionException(e)


def to_float(
    value: None | bool | str | int | float,
    additional_info=None,
    pre_convert_func=None,
    *args,
    **kwargs,
) -> float | None:
    """
    Конвертация значения в тип float.

    :param pre_convert_func: пользовательская функция, вызываемая до конвертации
    :param value: строковое значение
    :return: float
    """

    if pre_convert_func:
        value = pre_action(value, pre_convert_func, *args, **kwargs)

    try:
        if value is None:
            return None

        elif isinstance(value, bool):
            return 1.0 if value else 0.0

        elif isinstance(value, str):
            if value == "":
                return None

            if value.upper() == "TRUE":
                return 1.0
            elif value.upper() == "FALSE":
                return 0.0

            # Удаляем все пробелы и неразрывные пробелы
            value = re.sub(r"[\s\xa0\x20]+", "", value)

            # Заменяем первую запятую на точку
            value = re.sub(",", ".", value, 1)

            return float(value)

        elif isinstance(value, int):
            return float(value)

        elif isinstance(value, float):
            return value

        else:
            raise NotSupportedType(value)

    except Exception as e:
        raise ConvertToFloatException(e)


def to_int(
    value: None | bool | str | int | float,
    bankers_rounding: bool = False,
    pre_convert_func=None,
    *args,
    **kwargs,
) -> int | None:
    """
    Конвертация значения в тип int. Банковское округление.

    Значения с плавающей точкой нужно сначала перевести во float формат.


    :param value:
    :param pre_convert_func:
    :param bankers_rounding: алгоритм банковского округления
    :param args:
    :param kwargs:
    :return: int
    """
    if pre_convert_func:
        value = pre_action(value, pre_convert_func, *args, **kwargs)

    try:
        if not isinstance(value, (type(None), bool, str, int, float)):
            raise NotSupportedType(value)

        if value is None:
            return None

        elif isinstance(value, str):
            if value == "":
                return None

        if bankers_rounding:
            return round(to_float(value, pre_convert_func, *args, **kwargs))
        else:
            return int(to_float(value, pre_convert_func, *args, **kwargs))
    except Exception as e:
        raise ConvertToIntException(e)


def to_str(
    value: None | bool | str | int | float,
    additional_info=None,
    pre_convert_func=None,
    *args,
    **kwargs,
):
    """
    Конвертация значения в тип str.

     :param value: значение
     :param additional_info: дополнительная информация к типу данных
     :param pre_convert_func: пользовательская функция обработки значения до конвертации
     :param args:
     :param kwargs:
     :return:
    """

    if pre_convert_func:
        value = pre_action(value, pre_convert_func, *args, **kwargs)

    try:
        if value is None:
            return None

        elif isinstance(value, bool):
            return "TRUE" if value else "FALSE"

        elif isinstance(value, str):
            return value

        elif isinstance(value, int):
            return str(value)

        elif isinstance(value, float):
            return str(value)

        else:
            NotSupportedType(value)

    except Exception:
        raise ConvertToStrException(value)


def to_bool(
    value: None | bool | str | int | float,
    additional_info=None,
    pre_convert_func=None,
    *args,
    **kwargs,
):
    """
    Конвертация значения в тип bool.

    :param value: значение
    :param additional_info: дополнительная информация
    :param pre_convert_func: пользовательская функция перед конвертацией
    :param args: *
    :param kwargs: **
    :return:
    """
    if pre_convert_func:
        value = pre_action(value, pre_convert_func, *args, **kwargs)

    try:
        if value is None:
            return None

        elif isinstance(value, bool):
            return value

        elif isinstance(value, str):
            if value.upper() == "FALSE" or value == "0" or value == "":
                return False
            else:
                return True

        elif isinstance(value, int):
            return True if value != 0 else False

        elif isinstance(value, float):
            return True if value != 0.0 else False

        else:
            NotSupportedType(value)

    except Exception:
        raise ConvertToBoolException(value)


# TODO
def to_datetime(value, additional_info):
    try:
        return datetime.strptime(value, additional_info)  # .isoformat()
    except ValueError:
        return None


# TODO
def convert_value(value, value_type, additional_info=None):
    try:
        match value_type:
            case ValueType.BOOL:
                return to_bool(value, additional_info)
            case ValueType.STR:
                return to_str(value, additional_info)
            case ValueType.INT:
                return to_int(value, additional_info)
            case ValueType.FLOAT:
                return to_float(value, additional_info)
            case ValueType.DATETIME:
                return to_datetime(value, additional_info)
            case _:
                raise NotSupportedType((value, value_type))
    except Exception as e:
        raise ConvertValueException(e)
