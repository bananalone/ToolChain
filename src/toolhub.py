import re, shutil
from pathlib import Path
from typing import Any, List

from tqdm import tqdm

from factory import get_factory


factory = get_factory()


@factory.register('print_list')
def print_list(l: List[Any]):
    '''
    打印列表
    '''
    for e in l:
        print(e)


@factory.register('print')
def wrap_print(*args, **kwargs):
    '''
    打印
    '''
    print(*args, **kwargs)


@factory.register('sublist')
def sublist(l: List[Any], start: int, end: int) -> List[Any]:
    '''
    获取子列表
    '''
    return l[start: end]


@factory.register('index_of_list')
def index_of_list(l: List[Any], elem: Any) -> int:
    '''
    获取列表中元素的索引
    '''
    return l.index(elem)


@factory.register('list_lines')
def list_lines(file: str) -> List[str]:
    '''
    列出文件中的每一行
    '''
    f = Path(file)
    if not f.is_file():
        raise Exception(f'{str(f)} is not file')
    content = f.read_text()
    lines = content.strip().splitlines()
    return lines


@factory.register('write_list')
def write_list(l: List[str], dst: str):
    '''
    将列表内容写入文件
    '''
    dest = Path(dst)
    if dest.exists():
        raise Exception(f'{str(dest)} already exists')
    text = '\n'.join(l)
    dest.write_text(text)


@factory.register('glob')
def glob(dir: str, pattern: str = '*') -> List[str]:
    '''
    列出目录下的文件或子目录
    '''
    d = Path(dir)
    if not d.is_dir():
        raise Exception(f'{str(d)} is not dir')
    subs = [str(sub) for sub in d.glob(pattern)]
    return subs


def filter(l: List[Any], rule = lambda x: True) -> List[Any]:
    '''
    过滤列表
    '''
    ret_list = []
    for item in l:
        if rule(item):
            ret_list.append(item)
    return ret_list


def filter_blank_file(file: str) -> bool:
    f = Path(file)
    return f.is_file() and len(f.read_text().strip().split()) == 0 


@factory.register('filter_blank_files')
def filter_blank_files(files: List[str]) -> List[str]:
    '''
    过滤空白文件列表
    '''
    return filter(files, rule = filter_blank_file)


@factory.register('copyfiles')
def copyfiles(files: List[str], dst: str):
    '''
    复制列表里的文件到指定目录
    '''
    dest = Path(dst)
    if not dest.exists():
        dest.mkdir()
    if dest.is_file():
        raise Exception(f'{str(dest)} is a file')
    for file in tqdm(files):
        file = Path(file)
        if file.is_file():
            shutil.copy(str(file), str(dest / file.name))


@factory.register('movefiles')
def movefiles(files: List[str], dst: str):
    '''
    移动列表里的文件到指定目录
    '''
    dest = Path(dst)
    if not dest.exists():
        dest.mkdir()
    if dest.is_file():
        raise Exception(f'{str(dest)} is a file')
    for file in tqdm(files):
        file = Path(file)
        if file.is_file():
            shutil.move(str(file), str(dest / file.name))


@factory.register('removefiles')
def removefiles(files: List[str]):
    '''
    删除列表里的文件
    '''
    for file in tqdm(files):
        file = Path(file)
        if file.is_file():
            file.unlink()


@factory.register('sort')
def sort(l: List[Any]):
    '''
    从小到大排序
    '''
    l.sort()


@factory.register('natural_sort')
def natural_sort(list, key=lambda s:s):
    '''
    Sort the list into natural alphanumeric order.
    '''
    def get_alphanum_key_func(key):
        convert = lambda text: int(text) if text.isdigit() else text
        return lambda s: [convert(c) for c in re.split('([0-9]+)', key(s))]
    sort_key = get_alphanum_key_func(key)
    list.sort(key=sort_key)