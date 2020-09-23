# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os

path1 = r'Y:\2020\DCIM'
# path1 = r'C:\Users\danaukes\Dropbox (Personal)\projects\2019-12-24 passport photos'
# path1 = r'C:\Users\danaukes\Dropbox (Personal)\projects\2020-04-15 Garden Tour'
# hash1 = fus.scan_compare_dir(path1, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_file,local_hashfile='hash_sha256.yaml')
hash1 = fus.scan_compare_dir(path1, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_filesize,local_hashfile='hash_filesize.yaml')
