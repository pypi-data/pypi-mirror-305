#    pyOwlBoard - The Python client for the OwlBoard API
#    Copyright (C) 2024  Frederick Boniface

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name='pyOwlBoard',
    version='0.0.2',
    author='Frederick Boniface',
    author_email='api@owlboard.info',
    description='OwlBoard API Client',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://git.fjla.uk/owlboard/pyowlboard',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.20.0',
        'urllib3>=2.2.3',
    ]
)