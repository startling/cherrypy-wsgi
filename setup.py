#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = "cherrypy-wsgi",
    version = "0.1.1",
    author = "startling",
    author_email = "tdixon51793@gmail.com",
    description = "A script for running wsgi applications from the command-line with cherrypy.",
    scripts = ['cherrypy-wsgi'],
    install_requires = ['cherrypy'],
)
