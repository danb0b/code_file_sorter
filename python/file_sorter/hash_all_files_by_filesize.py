# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os

path1 = r'/home/danaukes/nas/photos/2021'
path2 = r'/home/danaukes/nas/photos/2020'
hash1 = fus.scan_list(path1,path2,directories_recursive=True,file_filter=fus.filter_none,hasher=fus.hash_filesize,directory_hashfile_name='hash_filesize.yaml')
hash1.save(os.path.expanduser('~'),'size_remote.yaml')
