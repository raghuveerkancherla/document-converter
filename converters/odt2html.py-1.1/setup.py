#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# $URL: svn://tengen/scripts/trunk/scripts/odt2html/setup.py $
#
# odt2html.py: Basic .odt to .html command line converter
# Copyright 2006 Ars Aperta http://arsaperta.com/
# Author: Jérôme Dumonteil <jerome.dumonteil@arsaperta.com>
# Included XSL file from Daniel Carrera taken from its odfreader perl 
# script.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import sys

def chk_py_version():
    ok_v=False
    try:
        if (sys.version_info[0]>2 or
                sys.version_info[0]==2 and sys.version_info[1]>=3):
            ok_v= True
    except:
        ok_v=False
    if not ok_v:
        print "Python version:",sys.version
        print "Requiring python 2.3 or above, intallation stopped."
        sys.exit(1)
    
chk_py_version()

from distutils.core import setup
from odt2html import VERSION

setup(  name            = "odt2html.py",
        version         = VERSION,
        license         = "GNU GPL version 2",
        description     = "Basic .odt to .html command line converter",
        long_description= """odt2html.py is a python command line script that 
                            makes a basic conversion of a .odt (OpenDocument) 
                            text into a HTML file. Other conversions are 
                            possible by changing the loaded XSL style sheet.""",
        author          = "Jerome Dumonteil",
        author_email    = "jerome.dumonteil@arsaperta.com",
        url             = "http://arsaperta.org/odftoolsen.html",
        download_url    = "http://arsaperta.org/odftoolsen.html",
        classifiers     = [
                        'Development Status :: 5 - Production/Stable',
                        'Environment :: Console',
                        'Intended Audience :: Information Technology',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: GNU General Public License (GPL)',
                        'Natural Language :: English',
                        'Operating System :: OS Independent',
                        'Programming Language :: Python',
                        'Topic :: Documentation',
                        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                        'Topic :: Office/Business :: Office Suites',
                        'Topic :: Text Processing',
                        'Topic :: Text Processing :: General',
                        'Topic :: Text Processing :: Markup :: HTML',
                        'Topic :: Text Processing :: Filters',
                        'Topic :: Text Editors :: Word Processors'
                            ],
        platforms        = 'Any',
        py_modules      = ['odt2html'],
        scripts         = ['odt2html'],
        data_files      = []
    )

