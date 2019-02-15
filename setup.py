#!/usr/bin/python2.7 
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
        alg_file = os.path.join(pg_path, 'AlgorithmController.tar.gz')
        with tarfile.open(alg_file, 'r') as tar:
            tar.extractall(pg_path)

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
  
    cmdclass={'install': PostInstallCommand},

    packages=['pudge'],
    package_dir={'pudge': 'src/pudge'},
    package_data={'pudge': ['*.tar*']}, 
    platforms = "any",  
    install_requires = ['requests>=2.7.0', 'Click'],
    scripts = [],  
    entry_points = {  
        'console_scripts': [  
            'pudge = pudge.run_cli:cli' 
        ]  
    }  
)
