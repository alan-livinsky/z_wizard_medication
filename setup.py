#!/usr/bin/env python

from setuptools import setup
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path, encoding='utf-8') as handle:
        return handle.read()

setup(
    name='z_wizard_medication',
    version='4.2.0',
    description='GNU Health: asistente personalizado para alta de medicamentos',
    long_description=read('README.rst'),
    author='',
    author_email='',
    url='',
    download_url='',
    package_dir={'trytond.modules.z_wizard_medication': '.'},
    packages=[
        'trytond.modules.z_wizard_medication',
        'trytond.modules.z_wizard_medication.wizard',
    ],
    package_data={
        'trytond.modules.z_wizard_medication': [
            'tryton.cfg',
            'view/*.xml',
            'locale/*.po',
            'wizard/*.py',
            'wizard/*.xml',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    license='GPL-3',
    install_requires=[
        'gnuhealth == 4.2.0',
        'trytond >= 6.0, < 6.1',
    ],
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    z_wizard_medication = trytond.modules.z_wizard_medication
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
