# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyslalib']

package_data = \
{'': ['*']}

install_requires = \
['numpy<1.24']

setup_kwargs = {
    'name': 'pyslalib',
    'version': '1.0.9',
    'description': 'f2py and numpy based wrappers for SLALIB',
    'long_description': 'pySLALIB v1.0.2  (Dec 2010)\n---------------\n\nThis is archive contains new f2py-generated (and hand-tweaked to\neliminate unnecessary function/subroutine arguments) wrappers for the\nFortran version of P.T. Wallace\'s SLALIB positional astronomy library.\nSLALIB used to be hosted by the STARLINK site, although that service\nhas been suspended.  The version of SLALIB included here is 2.5-4\n(with several additional tweaks) and is released under the GPL.\n\nThe python wrappers cover every function in SLALIB and a comprehensive\nset of unit tests are available in the test/ directory.  The only\nexternal dependency is numpy (http://numpy.scipy.org).  These wrappers\nare not related to the older (and apparently abandoned) pySLALIB that\nwas once available on the Web (and which depended on Numeric as\nopposed to numpy).\n\nInstallation\n------------\nMost users will only need to do:\n  > python setup.py install\nto generate the wrappers, build, and install the library.\n\nOnce slalib.so has been installed in your PYTHONPATH, you can run the\nunittests via:\n  > python test/test_slalib.py\n\nExample Usage (using IPython)\n-------------\nIn [1]: from pyslalib import slalib\n\nIn [2]: slalib.sla_veri()\nOut[2]: 2005004\n\nIn [3]: slalib.sla_caldj(1999, 12, 31)\nOut[3]: (51543.0, 0)\n\nIn [4]: slalib.sla_etrms(1976.9)\nOut[4]: array([ -1.62161710e-06,  -3.31007009e-07,  -1.43529663e-07])\n\nIn [5]: slalib.sla_fk45z(1.234, -0.123, 1984)\nOut[5]: (1.2446165107316911, -0.12141858395865548)\n\nIn [6]: slalib.sla_dafin("-00 03 34.6", 1)\nOut[6]: (12, -0.0010404101596610642, 0)\n\nIn [7]: slalib.sla_obs(0, "GBT")\nOut[7]:\n(\'GBT\',\n \'Green Bank Telescope                    \',\n 1.3934679949996727,\n 0.67078450520692623,\n 880.0)\n\nIf you import "sladoc" you can print the original Fortran doc\nstrings using something like:\n\nIn [1]: from pyslalib import slalib, sladoc\n\nIn [2]: print sladoc[\'sla_caldj\']\n"""\n*     - - - - - -\n*      C A L D J\n*     - - - - - -\n*\n*  Gregorian Calendar to Modified Julian Date\n*\n*  (Includes century default feature:  use sla_CLDJ for years\n*   before 100AD.)\n*\n*  Given:\n*     IY,IM,ID     int    year, month, day in Gregorian calendar\n*\n...\n\nThanks go to Prasanth for adding the docstring capabilities!\n\nIf you would like to build a shared library for linking with other\nprograms, a simple Makefile is also included that should work with\nonly minor tweaks for most Unix-like OSs.\n\nPlease let me know if you find any problems.\n\nScott\n\n----------------------------------\nScott M. Ransom <sransom@nrao.edu>\nhttp://www.cv.nrao.edu/~sransom',
    'author': 'Jashandeep Sohi',
    'author_email': 'jsohi@lco.global',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
