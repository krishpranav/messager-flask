#!/usr/bin/env/python

from .settings_common import *

# conditionally import additional settings depending on whether we're developing or in production

# can be set, for example by checking for a given environment variable or by detacting the hostname
production = False

if production:
	from .settings_prod import *
else:
	from .settings_dev import *
