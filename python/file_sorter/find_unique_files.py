# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os

# # path1 = '/mnt/photos/2020/DCIM/Camera'
# # path1 = r'Y:\2020\DCIM\Camera'
# # compare1 = fus.scan_compare_dir(path1, recursive=True,file_filter=fui.filter_img_filetype,hasher=fus.hash_filesize)
# # compare1.save('./','hash1.yaml')
# with open(os.path.join(os.path.expanduser('~'),'size_local.yaml')) as f:
#     compare1 = yaml.load(f,Loader=yaml.Loader)

# # path2 = '/mnt/photos/2020/unsorted'
# # path2 = r'Y:\2019\unsorted'
# # compare2 = fus.scan_compare_dir(path2, recursive=True,file_filter=fui.filter_img_filetype,hasher=fus.hash_filesize)
# # compare2.save('./','hash2.yaml')
# with open(os.path.join(os.path.expanduser('~'),'size_remote.yaml')) as f:
#     compare2 = yaml.load(f,Loader=yaml.Loader)

# same_size = set(compare1.hashes).intersection(set(compare2.hashes))

# local_files_to_check = [item for key in same_size for item in compare1.hash_file_dict[key]]
# remote_files_to_check = [item for key in same_size for item in compare2.hash_file_dict[key]]

# local_compare2 = fus.scan_list(*local_files_to_check,directories_recursive=False,file_filter = fus.filter_none,hasher=fus.hash_file)
# local_compare2.save(os.path.expanduser('~'),'sha256_local.yaml')
# remote_compare2 = fus.scan_list(*remote_files_to_check,directories_recursive=False,file_filter = fus.filter_none,hasher=fus.hash_file)
# remote_compare2.save(os.path.expanduser('~'),'sha256_remote.yaml')

with open(os.path.join(os.path.expanduser('~'),'sha256_local.yaml')) as f:
    local_compare2 = yaml.load(f,Loader=yaml.Loader)
with open(os.path.join(os.path.expanduser('~'),'sha256_remote.yaml')) as f:
    remote_compare2 = yaml.load(f,Loader=yaml.Loader)


same_file_hashes = set(local_compare2.hashes).intersection(set(remote_compare2.hashes))
same_file_names = [filename for key in same_file_hashes for filename in remote_compare2.hash_file_dict[key]]

new_path = os.path.join(os.path.expanduser('~'),'Desktop','dup')
os.mkdir(new_path)
for filename in same_file_names[:1]:
    
    new_file = os.path.join(new_path,os.path.split(filename)[1])
    # os.rename(filename, new_file)
    # os.remove(filename)
