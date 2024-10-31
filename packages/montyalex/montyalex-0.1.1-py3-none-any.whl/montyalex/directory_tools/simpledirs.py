import os

from montyalex.console_tools import richconsole, success_stm
from .helpdirs import remove_formated__dir

print = richconsole.print


def create_simple_directories(
    range_: int = 1,
    name_: str = None,
    prefix: str = None,
    suffix: str = None,
    silent: bool = False):
    for i in range(range_):
        formatted_directory_name = name_ if name_ else f'{i:03}'
        if prefix:
            formatted_directory_name = f'{prefix}{formatted_directory_name}'
        if suffix:
            formatted_directory_name = f'{formatted_directory_name}{suffix}'
        os.makedirs(os.path.join(os.getcwd(), formatted_directory_name), exist_ok=True)
        if not silent:
            print(
                f'{success_stm}, Created {formatted_directory_name!r} in {os.getcwd()!r}')

def remove_simple_directories(
    range_: int = 1,
    name_: str = None,
    prefix: str = None,
    suffix: str = None,
    silent: bool = False):
    for i in range(range_):
        formatted_directory_name = name_ if name_ else f'{i:03}'
        if prefix:
            formatted_directory_name = f'{prefix}{formatted_directory_name}'
        if suffix:
            formatted_directory_name = f'{formatted_directory_name}{suffix}'
        formatted_directory = os.path.join(os.getcwd(), formatted_directory_name)
        remove_formated__dir(formatted_directory, silent)

        if not os.path.exists(formatted_directory) and not silent:
            print(
                f'{success_stm}, Removed {formatted_directory_name!r} from {os.getcwd()!r}')
