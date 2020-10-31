import os
import re
from typing import List


# todo move this to a documentation; good example of recursion
# def output(path: str) -> None:
#     root, *dirs = path.split('/')
#
#     for item in dirs:
#         new_root = '/'.join([root, item])
#         if item in os.listdir(root):
#             root = new_root
#         else:
#             root = new_root
#             os.mkdir(root)


def _get_paths(directory: str) -> List[str]:
    # todo may want to add a smart feature to compare names of files desired to folders
    # todo may want to add another smart feature that sorts and searches (if not sorted already)
    # todo may want to add a feature to find the first one and get out or depending on the application return a list of files

    paths = list()
    for item in os.listdir(directory):
        if item[0] == "_":
            continue
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            paths.extend(_get_paths(full_path))
        else:
            paths.append(full_path)

    return paths


def _filter_paths(paths: List[str], path_map: dict) -> dict:
    # todo either dump this and change out get_paths or add functionality to remove already found paths
    # todo may want to add a sorting feature as well

    return {key: list(filter(lambda x: re.match(value, x), paths)) for key, value in path_map.items()}


def get_desired_paths(directory: str, path_map: dict) -> dict:
    paths = _get_paths(directory)
    print(f'paths are:\n {paths}')
    return _filter_paths(paths, path_map)


def create_path(path: str) -> None:
    os.makedirs(path)


def standardize_path(path: str) -> str:
    return path[:-1] if path[-1] == '/' else path


if __name__ == '__main__':
    path = 'test/testtest/testtesttest/'

    standard_path = standardize_path(path)
    create_path(path)
    pass
