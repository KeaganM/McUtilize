import sys
from typing import get_type_hints

from settings.commands import COMMANDS


def _parse_args(*args, _arg_delimenter: str = '--', ) -> dict:
    return {args[index].replace('-', ''): item for index, item in enumerate(args[1:]) if '--' not in item}


def _check_and_convert_args(**kwargs):

    for key,value in kwargs.items():
        new_value = value
        try:
            new_value = eval(value)
            quit()
        except (NameError, SyntaxError):
            pass
        kwargs[key] = new_value
    return kwargs


def terminal_wrapper(function:str,*args,commands:dict,convert_args: bool = True):
    parsed_kwargs = _parse_args(*args)
    converted_kwargs = _check_and_convert_args(**parsed_kwargs) if convert_args else parsed_kwargs
    return commands[function](**converted_kwargs)

if __name__ == '__main__':

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

    # i = 'hi'
    #
    #
    # test = {
    #     int:lambda :print('im an int')
    # }
    #
    #

    # args = sys.argv[1:]
    args = ['test4','--items',"[['main.id','>','1],['main.id','<','100']]"]
    res = terminal_wrapper(*args,commands=COMMANDS,)
    print(res)

    pass
