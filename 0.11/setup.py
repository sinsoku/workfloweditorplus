#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
#ticket-workflow
setup(
    name = 'WorkflowEditorPlusPlugin',
    version = '1.0.0a',
    description = "Edit Ticket Workflow",
    url = "http://github.com/sinsoku/workfloweditorplus/wiki",
    author = "Takumi Shotoku",
    author_email = "sinsoku.listy@gmail.com",
    license = "New BSD",
    zip_safe=True,
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {
        'trac.plugins': [
            'workfloweditorplus.workfloweditor_admin = workfloweditorplus.workfloweditor_admin',
        ]
    },
    package_data={'workfloweditorplus': [
                                     'templates/*.html',
                                     'templates/*.ini',
                                     'htdocs/css/*.css',
                                     'htdocs/images/*.*',
                                     'htdocs/js/*.js',
                                     'htdocs/js/grid/*.js',
                                     'htdocs/js/ui/*.js',
                                    ]}
)
