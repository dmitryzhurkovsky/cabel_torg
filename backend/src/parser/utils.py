import re

from xml.etree.ElementTree import Element


def get_tag_name(raw_field: Element) -> str:
    return raw_field.tag.split('}')[-1]


def clean_string_from_spaces_and_redundant_symbols(dirty_string: str) -> str | None:
    """Clean an input element from any redundant symbols and spaces."""
    if dirty_string == '.' or not dirty_string.strip():
        return None
    try:
        clean_string = re.findall(pattern='[А-Яа-яЁёa-zA-Z0-9].+[А-Яа-яЁёa-zA-Z.0-9)"]', string=dirty_string)[0]
        return clean_string
    except Exception:  # todo add to logger
        return None


def clean_fields(fields: dict) -> dict:
    """Delete None elements from dict"""
    prepared_fields = dict()
    for key, value in fields.items():
        if value:
            prepared_fields[key] = value

    return prepared_fields