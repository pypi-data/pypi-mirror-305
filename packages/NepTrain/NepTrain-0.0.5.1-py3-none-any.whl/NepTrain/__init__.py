#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/24 16:22
# @Author  : 兵
# @email    : 1747193328@qq.com
import configparser
import os
from watchdog.utils import   platform

import shutil

from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver
from NepTrain import utils


__version__="0.0.5"

config_path = utils.get_config_path()

module_path = os.path.dirname(__file__)

if not os.path.exists(config_path)  :
    shutil.copy(os.path.join(module_path,"config.ini"), config_path)

Config = configparser.RawConfigParser()
Config.read(config_path,encoding="utf8")

if platform.is_linux():
    # wsl测试默认的有问题  强行切换到poll机制
    observer = PollingObserver()
else:
    observer = Observer()



