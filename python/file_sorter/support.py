# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:38:49 2019

@author: danaukes
"""

import os
import yaml

class HashFile(object):
    def __init__(self,hash_file_dict,file_hash_dict,hashes):
        self.hash_file_dict = hash_file_dict
        self.file_hash_dict = file_hash_dict
        self.hashes = hashes
#        self.comparison_type = comparison_type

    @classmethod
    def build(cls,compare_files,hasher):
        compare_hash_dict = {}
        compare_hashes = []
        compare_hash_dict_rev={}
            
        ii = 0
        l = len(compare_files)
        for filename in compare_files:
            filename = os.path.normpath(filename)
            img_hash= hasher(filename)
            compare_hash_dict[filename] = img_hash
            compare_hashes.append(img_hash)
            if img_hash not in compare_hash_dict_rev:
                compare_hash_dict_rev[img_hash] = [filename]
            else:
                compare_hash_dict_rev[img_hash].append(filename)
            if ii%10==0:
                print('getting file info',ii,l)
            ii+=1
        
        compare_hash_set = list(set(compare_hashes))
        new = cls(compare_hash_dict_rev,compare_hash_dict,compare_hash_set)
        
        return new
    
    def save(self,*args):
        with open(os.path.join(*args),'w') as f:
            yaml.dump(self,f)

    @classmethod            
    def load(cls,*args):
        with open(os.path.join(*args)) as f:
            new = yaml.load(f,Loader=yaml.FullLoader)
        return new
    
    def merge(self,other):
        for key, value in other.hash_file_dict.items():
            if key in self.hash_file_dict:
                self.hash_file_dict[key].extend(value)
            else:
                self.hash_file_dict[key]=value.copy()
        self.file_hash_dict.update(other.file_hash_dict)
        self.hashes.extend(other.hashes)

        
def filter_files(items,file_filter):
    return [item for item in items if (file_filter(item))]

# def scan_file_list(list):
#     return HashFile.build(all_compare_files,hasher)

def scan_compare_dir(*compare_dirs,hasher = None, file_filter = None, recursive=False,local_hashfile = None):
    hasher = hasher or hash_filesize 
    file_filter = file_filter or filter_none
    
    all_compare_files = []    

    for compare_dir in compare_dirs:
        if recursive:
            for dirpath,dirnames,filenames in os.walk(compare_dir):
                filenames = [os.path.join(dirpath,item) for item in filenames]
                filenames = filter_files(filenames,file_filter)
                
                if local_hashfile is not None:
                    hash_file = HashFile.build(filenames,hasher)
                    hash_file.save(dirpath,local_hashfile)

                print('finding files',dirpath)

                all_compare_files.extend(filenames)
        else:
            dirpath = compare_dir
            filenames = os.listdir(dirpath)
            filenames = [os.path.join(dirpath,item) for item in filenames]
            filenames = [item for item in filenames if os.path.isfile(item)]
            filenames = filter_files(filenames,file_filter)
        
            if local_hashfile is not None:
                hash_file = HashFile.build(filenames,hasher)
                hash_file.save(dirpath,local_hashfile)

            print('finding files',dirpath)

            all_compare_files.extend(filenames)
            
        if local_hashfile is None:
        
            global_hash_file = HashFile.build(all_compare_files,hasher)
            return global_hash_file
        else:
            return None


def filter_none(filename):
    return True

def hash_filesize(filename):
    size = os.path.getsize(filename)
    return size

def hash_file(filename):
    import hashlib
    
    # file = ".\myfile.txt" # Location of the file (can be set a different way)
    BLOCK_SIZE = 65536 # The size of each read from the file
    
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(filename, 'rb') as f: # Open the file to read it's bytes
        try:
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        except OSError:
            pass
    
    return file_hash.hexdigest() # Get the hexadecimal digest of the hash
    
    
def check_match(filea,fileb):
    with open(filea,'rb') as  fa:
        with open(fileb,'rb') as  fb:
            result = set(fa).symmetric_difference(fb)
    match= (len(result)==0)
    return match


def save_progress(source_files,matched_files,unmatched_files):           
    with open('progress.yaml','w') as f:
        yaml.dump([source_files,matched_files, unmatched_files],f)

def rebuild_compare_info(*compare_dirs, filename = 'compare_info.yaml',**kwargs):
    if os.path.exists(filename):
        os.remove(filename)
    compare_info = scan_compare_dir(*compare_dirs, **kwargs)
    compare_info.save('./',filename)
    
def find_items_with_matching_sizes(compare_size_dict_rev):
    items = []
    for key,value in compare_size_dict_rev.items():
        if len(value)>1:
            items.append((key,value))
    return items

if __name__=='__main__':
    pass