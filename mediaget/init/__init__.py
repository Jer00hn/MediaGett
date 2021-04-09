#from __future__ import print_function
#from __future__ import unicode_literals

#import codecs
#import datetime
#import mimetypes
#import os
#import shutil
#import site
import sys

#from medusa import app


def initialize():
    """Initialize all fixes and workarounds."""
    _check_python_version()
#    _configure_syspath()
    
def _check_python_version():
    if sys.version_info < (2, 7) or (3,) < sys.version_info < (3, 5):
        print('Sorry, requires Python 2.7.x or Python 3.5 and above')
        sys.exit(1)
        
#def _get_lib_location(relative_path):
#    return os.path.abspath(os.path.join(os.path.#dirname(__file__), '..', '..', relative_path))


#def _configure_syspath():

#    paths_to_insert = [
#        _get_lib_location(app.LIB_FOLDER),
#        _get_lib_location(app.EXT_FOLDER)
#    ]

#    if sys.version_info[0] == 2:
        # Add Python 2-only vendored libraries
#        paths_to_insert.extend([
#            _get_lib_location(app.LIB2_FOLDER),
#            _get_lib_location(app.EXT2_FOLDER)
#        ])
#    elif sys.version_info[0] == 3:
        # Add Python 3-only vendored libraries
#        paths_to_insert.extend([
#            _get_lib_location(app.LIB3_FOLDER),
#            _get_lib_location(app.EXT3_FOLDER)
#        ])

    # Insert paths into `sys.path` and handle `.pth` files
    # Inspired by: https://bugs.python.org/issue7744
#    for dirpath in paths_to_insert:
        # Clear `sys.path`
#        sys.path, remainder = sys.path[:1], sys.path[1:]
        # Add directory as a site-packages directory and handle `.pth` files
#        site.addsitedir(dirpath)
        # Restore rest of `sys.path`
#        sys.path.extend(remainder)