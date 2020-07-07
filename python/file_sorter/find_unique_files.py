# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:15:20 2019

@author: danaukes
"""

import pydevtools.find_unique_files.support as fus
import os
import sys
import yaml


print('###########################')
print('argv:')
print(sys.argv)

#paths = 'Y:/2017', 'Y:/2018', 'Y:/2019'
#fus.rebuild_compare_info(p1, recursive=True)
#fus.rebuild_compare_info(p1, recursive=True,local_ha
#p1 = 'C:/Users/danaukes/Dropbox (Personal)/Camera Uploads'
#p1 = 'C:/Users/danaukes/Dropbox (ASU)/Mendeley Desktop/Archive1'
compare_info = fus.scan_compare_dir(p1, recursive=True)
compare_info.save('./','hash_size.yaml')
    
with open('hash_size.yaml') as f:
    compare_info = yaml.load(f)

#source_dir = 'C:/shared/duplicate phone photos'
#source_dir = 'C:/Users/danaukes/Desktop/duplicate phone photos'

source_dirs = []
#source_dirs.append('C:/Users/danaukes/Dropbox (ASU)/Mendeley Desktop/Archive1')
#source_dirs.append('C:/Users/danaukes/Dropbox (ASU)/Mendeley Desktop/Archive2')
#source_dirs.append('C:/Users/danaukes/Dropbox (ASU)/Mendeley Desktop/Archive3')
#source_dirs.append('C:/Users/danaukes/Dropbox (ASU)/Mendeley Desktop/Archive4')

original = 'original'
#duplicate = 'duplicate'

        
compare_size_dict_rev = compare_info.hash_file_dict
compare_size_set = compare_info.hashes
#compare_size_dict_rev = compare_info['size_file_dict']
#compare_size_set = compare_info['sizes']

print('###########################')
print('')

#items = fus.find_items_with_matching_sizes(compare_size_dict_rev)
#print(items)

source_files = []

for source_dir in source_dirs:
    for dirpath,dirnames,filenames in os.walk(source_dir):
        full_file_names = [os.path.join(dirpath,item) for item in filenames]
        source_files.extend(full_file_names)

source_size_dict = {}
source_sizes  = []

candidate = []
comparison_set = []

matched_files = []
unmatched_files = []
    
l= len(source_files)

ii = 0
while not not source_files:
#for ii,filename in enumerate(source_files):
    filename=source_files.pop(0)
#    print('{0:.0f}/{1:.0f}'.format(ii,l))
    size = os.path.getsize(filename)
    source_size_dict[filename] = size
    source_sizes.append(size)
    if size in compare_size_set:
#        candidate.append(filename)
        matched = False
        for item in compare_size_dict_rev[size]:
            if filename != item:
                comparison_set.append((filename,item))
                if fus.check_match(filename,item):
                    matched = True
                    break
        if matched:
            matched_files.append((filename,item))
        else:
            unmatched_files.append(filename)
    else:
        unmatched_files.append(filename)
    print(ii,len(source_files),l,len(matched_files),len(unmatched_files))
    if ii%10==0:
        fus.save_progress(source_files,matched_files,unmatched_files)
    ii+=1


fus.save_progress(source_files,matched_files,unmatched_files)

#
#            for a,b in f1.readlines(), f2.readlines():
#            a=fa.readline()
#            b=fb.readline()
#   
#results = []         
#for item in comparison_set:
##    print(item)
#    results.append(compare_file_data(*item))
#        
#    
#print('###########################')
#print('unmatched files')
#print(unmatched)