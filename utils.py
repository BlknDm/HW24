from typing import List, Iterator, Any, Dict, Union
import re


def query_filter(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda row: param in row, data))


def query_map(param: str, data: List[str]) -> List[str]:
    col_number = int(param)
    return list(map(lambda row: row.split(' ')[col_number], data))


def query_unique(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))


def query_sort(param: str, data: List[str]) -> List[str]:
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def query_limit(param: str, data: List[str]) -> List[str]:
    limit = int(param)
    return data[:limit]


def query_regex(param: str, data: List[str]) -> Iterator[str]:
    regex = re.compile(param)
    return filter(lambda x: re.search(regex, x), data)


CMD_TO_FUNCTION = {
    'filter': query_filter,
    'map': query_map,
    'unique': query_unique,
    'sort': query_sort,
    'limit': query_limit,
    'regex': query_regex
}


def query_build(cmd, param, filename, data=None) -> Iterator[str]:
    if not data:
        with open(f'data/{filename}') as file:
            data = list(map(lambda row: row.strip(), file))
    return CMD_TO_FUNCTION[cmd](param=param, data=data)
