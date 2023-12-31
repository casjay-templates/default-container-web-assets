#!/usr/bin/env python
# -*-python-*-
#
# Copyright (C) 1999-2012 The ViewCVS Group. All Rights Reserved.
#
# By using this file, you agree to the terms and conditions set forth in
# the LICENSE.html file which can be found at the top level of the ViewVC
# distribution or at //viewvc.org/license-1.html.
#
# For more information, visit //viewvc.org/
#
# -----------------------------------------------------------------------
#
# query.cgi: View CVS/SVN commit database by web browser
#
# -----------------------------------------------------------------------
#
# This is a teeny stub to launch the main ViewVC app. It checks the load
# average, then loads the (precompiled) viewvc.py file and runs it.
#
# -----------------------------------------------------------------------
#

#########################################################################
#
# INSTALL-TIME CONFIGURATION
#
# These values will be set during the installation process. During
# development, they will remain None.
#

LIBRARY_DIR = r"/usr/share/viewvc/lib"
CONF_PATHNAME = r"/etc/viewvc/viewvc.conf"

#########################################################################
#
# Adjust sys.path to include our library directory
#

import sys
import os

if LIBRARY_DIR:
  sys.path.insert(0, LIBRARY_DIR)
else:
  sys.path.insert(0, os.path.abspath(os.path.join(sys.argv[0],
                                                  "../../../lib")))

#########################################################################

import sapi
import viewvc
import query

server = sapi.CgiServer()
cfg = viewvc.load_config(CONF_PATHNAME, server)
viewvc_base_url = cfg.query.viewvc_base_url
if viewvc_base_url is None:
  viewvc_base_url = "viewvc.cgi"
query.main(server, cfg, viewvc_base_url)
