#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/24 16:01
# @Author  : 兵
# @email    : 1747193328@qq.com
import os
from contextlib import contextmanager
from pathlib import Path

from typing import Generator, Union

from ase.io import read as ase_read
from tqdm import tqdm
def get_config_path():
    return os.path.join(os.path.expanduser('~'),".NepTrain")



@contextmanager
def cd(path: Union[str, Path]) -> Generator:
    """


        with cd("/my/path/"):
            do_something()

    Args:
        path: Path to cd to.
    """
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)
def iter_path_to_atoms(glob_strs: list,show_progress=True,**kkwargs):
    def decorator(func):
        def wrapper(path: Path | str, *args, **kwargs):
            if isinstance(path, str):
                path = Path(path)
            if path.is_dir():
                parent = path
            else:
                parent = path.parent
            result =[]

            filter_path_list=[]
            for glob_str in glob_strs:
                for i in parent.glob(glob_str):

                    if path.is_file():

                        if i.name != path.name:
                            continue
                    try:
                        atoms=ase_read(i.as_posix(),index=":")
                    except Exception as e:
                        print(f"文件：{i.as_posix()}读取错误!报错原因：{e}")
                        continue
                    if isinstance(atoms,list):

                        filter_path_list.extend(atoms)
                    else:
                        filter_path_list.append(atoms)

            if show_progress:
                iter_obj=tqdm(filter_path_list,
                              **kkwargs
                              )
            else:
                iter_obj=filter_path_list

            for i in iter_obj:

                try:
                    result.append(func(i, *args, **kwargs))
                except KeyboardInterrupt:
                    return result
                except Exception as e:
                    print(e)
                    pass
            return result
        return wrapper

    return decorator


def is_diff_path(path,path1):
    return os.path.abspath(path)!=os.path.abspath(path1)
