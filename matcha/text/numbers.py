"""Vietnamese number normalization for TTS
"""
import re

_units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
_special_units = {1: "mốt", 4: "tư", 5: "lăm"}
_positions = ["", "nghìn", "triệu", "tỷ"]

_number_re = re.compile(r"[0-9]+")


def read_three_digits(number):
    number = int(number)
    hundreds = number // 100
    tens = (number % 100) // 10
    units = number % 10
    result = []

    if hundreds != 0:
        result.append(_units[hundreds] + " trăm")
    elif tens != 0 or units != 0:
        result.append("không trăm")

    if tens != 0:
        if tens == 1:
            result.append("mươi")
        else:
            result.append(_units[tens] + " mươi")
    elif units != 0:
        result.append("linh")

    if units != 0:
        if tens >= 2 and units in _special_units:
            result.append(_special_units[units])
        else:
            result.append(_units[units])

    return " ".join(result)


def split_number_to_groups(number):
    s = str(number)
    groups = []
    while s:
        groups.insert(0, s[-3:])
        s = s[:-3]
    return groups


def number_to_vietnamese_words(number):
    number = int(number)
    if number == 0:
        return "không"

    groups = split_number_to_groups(number)
    result = []
    for i, group in enumerate(groups):
        group_int = int(group)
        if group_int != 0:
            words = read_three_digits(group.zfill(3))
            position = _positions[len(groups) - i - 1]
            result.append(words + (" " + position if position else ""))
        elif i == len(groups) - 1 and not result:
            result.append("không")

    return " ".join(result).strip()


def _expand_number(m):
    return number_to_vietnamese_words(m.group(0))


def normalize_numbers(text):
    return re.sub(_number_re, _expand_number, text)
