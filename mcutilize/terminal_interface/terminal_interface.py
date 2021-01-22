import sys
from typing import get_type_hints


def test(x: int, y: int):
    return x + y


def _parse_args(*args, _arg_delimenter: str = '--', ) -> dict:
    return {args[index].replace('-', ''): item for index, item in enumerate(args[1:]) if '--' not in item}


def _check_and_convert_args(**kwargs):
    # todo may want to add more type checking

    conversions = [
        lambda x: int(x),
        lambda x: float(x),
    ]

    for kwarg in kwargs:
        value = kwargs[kwarg]
        for conversion in conversions:
            if value == kwargs[kwarg]:
                try:
                    value = conversion(kwargs[kwarg])
                except Exception:
                    pass
        kwargs[kwarg] = value
    return kwargs


def terminal_wrapper(function, *args, convert_args: bool = True):
    parsed_kwargs = _parse_args(*args)
    converted_kwargs = _check_and_convert_args(**parsed_kwargs) if convert_args else parsed_kwargs
    return function(**converted_kwargs)


if __name__ == '__main__':
    # todo may want to consider some sort of type checking functionality, for now if it looks like a int/float/whatever,
    #  it will try to get converted
    # args = ['1','1.5','hey']
    #
    # t = _check_and_convert_args(*args)
    # print(t)
    #
    # print(bool(test.isdigit()))
    # print(bool(test2.isnumeric()))
    # test_function_types = get_type_hints(test)
    # print(test_function_types)
    # args = {'x':1,'y':2}
    #
    # for arg in args:
    #     print(type(args[arg]))
    #     print(type(test_function_types[arg]))
    #     print('*'*200)
    #     if type(args[arg]) == type(test_function_types[arg]):
    #         print(f'arg:{arg} is the same type as {test_function_types[arg]}')

    args = sys.argv
    # args = ['--x', '1', '--y', '10.897']

    res = terminal_wrapper(test, *args)
    print(res)

    pass
