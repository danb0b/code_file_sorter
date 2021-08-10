# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:49:30 2020

@author: danaukes
"""

import file_sorter.support as fus
import file_sorter.images as fui
import yaml
import os
import argparse



if __name__=='__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('path',metavar='path',type=str,help='path', default = './')
    parser.add_argument('-o','--output',dest='output',default = None)
    parser.add_argument('-r','--recursive',dest='recursive',action='store_true', default = None)
    parser.add_argument('-v','--verbose',dest='verbose',action='store_true', default = None)
    
    # parser.add_argument('-p','--preset',dest='preset',default = None)

    args = parser.parse_args()
    # print('path: ',args.path)

    # path1 = r'/home/danaukes/nas/photos/2021'
    # path2 = r'/home/danaukes/nas/photos/2020'
    hash1 = fus.scan_list(args.path,directories_recursive=args.recursive,file_filter=fus.filter_yaml,hasher=fus.hash_filesize,directory_hashfile_name='hash_filesize.yaml',verbose=args.verbose)
    print(yaml.dump(hash1))
    if args.output is not None:
        hash1.save(args.output)
