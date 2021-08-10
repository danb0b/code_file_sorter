# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:00:56 2021

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os
import shutil



# local_compare1 = fus.scan_list(r'G:\Shared drives\IDEAlab\videos',directories_recursive=True,file_filter=fus.filter_yaml,hasher=fus.hash_filesize,directory_hashfile_name='hash_filesize.yaml')

# with open(os.path.expanduser('~/test.yaml')) as f:
#     local_compare1 = yaml.load(f,Loader=yaml.Loader)

# files_to_check = []

# for key,value in local_compare1.hash_file_dict.items():
#     if len(value)>1:
#         # print(value)
#         files_to_check.extend(value)
        
# local_compare2 = fus.scan_list(*files_to_check,directories_recursive=False,file_filter = fus.filter_none,hasher=fus.hash_file,verbose=True)
# local_compare2.save('~/sha256_local.yaml')

with open(os.path.expanduser('~/sha256_local.yaml')) as f:
    local_compare2 = yaml.load(f,Loader=yaml.Loader)

duplicates = []

for key,value in local_compare2.hash_file_dict.items():
    if len(value)>1:
        # print(value)
        duplicates.append(value)

for files in duplicates[1:]:
    # l = len(files)
    # where = [1*('recovery' in path) for path in files]
    # m = sum(where)
    keep = files.pop(0)
    if not os.path.exists(keep):
        raise(Exception('re-run!'))
    # toss = files
    # print('keeping: ',keep,'\ntossing: ',files)
    for item in files:
        if os.path.exists(item):
            print('removing',item)
            os.remove(item)
    