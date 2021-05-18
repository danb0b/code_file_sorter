# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os

# path1 = '/mnt/photos/2020/DCIM/Camera'
# path1 = r'Y:\2020\DCIM\Camera'
# compare1 = fus.scan_compare_dir(path1, recursive=True,file_filter=fui.filter_img_filetype,hasher=fus.hash_filesize)
# compare1.save('./','hash1.yaml')
with open(os.path.join(os.path.expanduser('~'),'size_local.yaml')) as f:
    compare1 = yaml.load(f,Loader=yaml.Loader)

# path2 = '/mnt/photos/2020/unsorted'
# path2 = r'Y:\2019\unsorted'
# compare2 = fus.scan_compare_dir(path2, recursive=True,file_filter=fui.filter_img_filetype,hasher=fus.hash_filesize)
# compare2.save('./','hash2.yaml')
with open(os.path.join(os.path.expanduser('~'),'size_remote.yaml')) as f:
    compare2 = yaml.load(f,Loader=yaml.Loader)

same_size = set(compare1.hashes).intersection(set(compare2.hashes))

local_files_to_check = [item for key in same_size for item in compare1.hash_file_dict[key]]
remote_files_to_check = [item for key in same_size for item in compare2.hash_file_dict[key]]

local_compare2 = fus.scan_list(*local_files_to_check,directories_recursive=False,file_filter = fus.filter_none,hasher=fus.hash_file)
local_compare2.save('sha256_local.yaml')
local_compare2.save(os.path.expanduser('~'),'sha256_local.yaml')
# compare1i = fus.scan_compare_dir(path1, recursive=True,file_filter=fui.filter_img_filetype,hasher=fui.gen_p_hash_opt)
# compare1i.save('./','hash1i.yaml')
# with open('hash1i.yaml') as f:
#     compare1i = yaml.load(f,Loader=yaml.FullLoader)
# compare2i = fus.scan_compare_dir(path2, recursive=True,file_filter=fui.filter_img_filetype,hasher=fui.gen_p_hash_opt)
# compare2i.save('./','hash2i.yaml')
# with open('hash2i.yaml') as f:
#     compare2i = yaml.load(f,Loader=yaml.FullLoader)


# compare1i = fus.scan_compare_dir(path1, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_file)
# compare1i.save('./','hash1s.yaml')
# with open('hash1s.yaml') as f:
#     compare1s = yaml.load(f,Loader=yaml.FullLoader)
# compare2i = fus.scan_compare_dir(path2, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_file)
# compare2i.save('./','hash2s.yaml')
# with open('hash2s.yaml') as f:
#     compare2s = yaml.load(f,Loader=yaml.FullLoader)


# same_file = set(compare1s.hashes).intersection(set(compare2s.hashes))
# # same_file1 = [compare2s.hash_file_dict[key] for key in same_file]
# same_file2 = [filename for key in same_file for filename in compare1s.hash_file_dict[key]]
# # same_look = set(compare1i.hashes).intersection(set(compare2i.hashes))

# # # for key,value in compare2.hash_file_dict.items():
# # #     if len(value)>1:
# # #         print(value)

# # dcim_filenames1 = set([item2 for item in same_size for item2 in compare1.hash_file_dict[item]])
# # dcim_filenames2 = set([item2 for item in same_look for item2 in compare1i.hash_file_dict[item]])
# # dcim_filenames3 = dcim_filenames1.intersection(dcim_filenames2)

# with open ('matched_files2.yaml','w') as f:
#     yaml.dump(list(same_file2),f)
    
    
# for filename in same_file2:
#     os.remove(filename)
# # not_matched = dcim_filenames1.symmetric_difference(dcim_filenames2)
# # print(not_matched)

