#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author　: Lemon pineapple
# @FileName: look_app_os.py
# @Software: PyCharm
# @Github  : SkyBlueEternal.github.io Or skyblueeternal.gitee.io/blog

import os
import zipfile
from lib_script import PackNameList


def app_os_name_list(app_path):
    folder_path, file_name = os.path.split(app_path)
    os.chdir(folder_path)
    try:
        read_hey = zipfile.ZipFile(file_name)
    except:
        return "上传文件无法识别。"
    else:
        read_hey_name_list = read_hey.namelist()
        for name in PackNameList.pack_name.keys():
            for i in read_hey_name_list:
                if i.find(name) > 0:
                    return PackNameList.pack_name.get(name)
        return "未识别壳。"

