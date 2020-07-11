# -*- coding: utf-8 -*-
'''
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
'''

from setuptools import setup
import sys
import shutil

shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree('file_sorter.egg-info', ignore_errors=True)


packages = []
packages.append('file_sorter')

package_data = {}
package_data['file_sorter'] = []

setup_kwargs = {}
setup_kwargs['name']='file_sorter'
setup_kwargs['version']='0.0.1'
setup_kwargs['classifiers']=['Programming Language :: Python','Programming Language :: Python :: 3']   
setup_kwargs['description']='File Sorter is a collection of tools for hashing, identifying, and sorting unique files'
setup_kwargs['author']='Dan Aukes'
setup_kwargs['author_email']='danaukes@danaukes.com'
setup_kwargs['url']='https://github.com/danb0b/code_file_sorter'
setup_kwargs['license']='MIT'
setup_kwargs['packages']=packages
setup_kwargs['package_dir']={'file_sorter' : 'python/file_sorter'}
setup_kwargs['package_data'] = package_data
setup_kwargs['install_requires']=['pillow','matplotlib','numpy','yaml']
  
setup(**setup_kwargs)
