#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
from setuptools import setup, find_packages
long_description = (this_directory / "README.md").read_text()
setup(
     name='hmmstuff',
     zip_safe=False,
     include_package_data=True,

     version='0.0.3',

     author="Gabriele Orlando",

     author_email="gabriele.orlando@kuleuven.be",

     description="A tool to get structural information about light chain amyloids",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/grogdrinker/hmmstuff",
     
     packages=['HMMSTUFF'],
     package_dir={'HMMSTUFF': 'HMMSTUFF/',"HMMSTUFF.templates":'HMMSTUFF/templates/',
                  "HMMSTUFF.models":'HMMSTUFF/models/',
                    "HMMSTUFF.models.6HUD":'HMMSTUFF/models/6HUD',
                    "HMMSTUFF.models.6IC3":'HMMSTUFF/models/6IC3',
                    "HMMSTUFF.models.6Z1O":'HMMSTUFF/models/6Z1O',
                    "HMMSTUFF.models.7NSL":'HMMSTUFF/models/7NSL',
                    "HMMSTUFF.models.6Z1I":'HMMSTUFF/models/6Z1I',
                    "HMMSTUFF.models.8CPE":'HMMSTUFF/models/8CPE',
                  },
     package_data={'HMMSTUFF': ["logo.jpg",'models/6HUD/*','models/6IC3/*','models/6Z1O/*','models/7NSL/*','models/6Z1I/*','models/8CPE/*','templates/*']},

     #packages = find_packages( include = ["models/*","templates/*"]),  # Includes models and all sub-packages

     python_requires='<3.8',

     install_requires=["pomegranate==0.14.0","numpy", "scikit-learn","Bio" ],

     classifiers=[

         "Programming Language :: Python :: 3",

         "Operating System :: OS Independent",

     ],

 )
