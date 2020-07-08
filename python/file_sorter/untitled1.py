# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml

path1 = r'Y:\2020\DCIM\Camera'
# compare1 = fus.scan_compare_dir(path1, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_filesize)
# compare1.save('./','hash1.yaml')
with open('hash1.yaml') as f:
    compare1 = yaml.load(f)

path2 = r'Y:\2020\unsorted'
# compare2 = fus.scan_compare_dir(path2, recursive=True,file_filter=fus.filter_none,hasher=fus.hash_filesize)
# compare2.save('./','hash2.yaml')
with open('hash2.yaml') as f:
    compare2 = yaml.load(f)

same_size = set(compare1.hashes).intersection(set(compare2.hashes))

# compare1i = fus.scan_compare_dir(path1, recursive=True,file_filter=fui.filter_img_filetype,hasher=fui.gen_p_hash_opt)
# compare1i.save('./','hash1i.yaml')
with open('hash1i.yaml') as f:
    compare1i = yaml.load(f)
# compare2i = fus.scan_compare_dir(path2, recursive=True,file_filter=fui.filter_img_filetype,hasher=fui.gen_p_hash_opt)
# compare2i.save('./','hash2i.yaml')
with open('hash2i.yaml') as f:
    compare2i = yaml.load(f)


# for key,value in compare2.hash_file_dict.items():
#     if len(value)>1:
#         print(value)