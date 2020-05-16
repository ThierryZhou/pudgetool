#!/usr/bin/python3 
# -*- coding: utf-8 -*- 

from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.sysconfig import get_python_lib
import tarfile
import os

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(self)
 
        pkg_path = get_python_lib()
        pg_path = os.path.join(pkg_path, 'pudge')

setup(  
    name = "pudge",  
    version = "1.0", 
    keywords = ("pudge tools", "CLI tools"),
    description = "pudge tools is automatic coding tools",  
    long_description = "pudge tools is automatic coding tools",  
    license = "MIT Licence",  
  
    url = "https://github.com/ThePolarNight/pudgetools.git",
    author = "zhouh",  
    author_email = "zhouhui295@163.com",
  
    platforms = "any",  
    install_requires = ['requests', 'Click'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts = [],  
    entry_points = {  
        'console_scripts': [  
            'pudge = pudge.entry_point:entry_point' 
        ]  
    }  
)
