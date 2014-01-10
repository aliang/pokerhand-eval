# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pokereval',
    version='0.1.0',
    author=u'Alvin Liang, Zach Wissner-Gross, arlsr, Jim Kelly',
    author_email='ayliang@gmail.com',
    packages=['pokereval'],
    url='https://github.com/aliang/pokerhand-eval',
    license='Apache, see LICENSE.txt',
    description='A pure python poker hand evaluator for 5, 6, 7 cards',
    long_description=open('README.txt').read(),
)