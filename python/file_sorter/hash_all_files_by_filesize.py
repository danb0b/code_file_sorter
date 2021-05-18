# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os

#path1 = r'Y:\2020\DCIM'
#path1 = r'C:\Users\danaukes\Dropbox (Personal)\Pictures'
path1 = r'C:\Users\danaukes\Desktop\Camera'
# path2 = r'C:\Users\danaukes\Dropbox (Personal)\Camera Uploads from Sara'
# hash1 = fus.scan_compare_dir(path1, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_file,local_hashfile='hash_sha256.yaml')
hash1 = fus.scan_list(path1,directories_recursive=True,file_filter=fus.filter_none,hasher=fus.hash_filesize,directory_hashfile_name='hash_filesize.yaml')
hash1.save(os.path.expanduser('~'),'size_local.yaml')