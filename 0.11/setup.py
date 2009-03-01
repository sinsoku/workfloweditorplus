#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
#ticket-workflow
setup(
    name = 'WorkflowEditorPlugin',
    version = '1.0.1',
    description = "Edit Ticket Workflow",
    url = "http://trac-hacks.org/wiki/WorkflowEditorPlugin",
    author = "Takanori Suzuki",
    author_email = "takanorig@gmail.com",
    license = "New BSD",
    zip_safe=True,
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {
        'trac.plugins': [
            'workfloweditor.workfloweditor_admin = workfloweditor.workfloweditor_admin',
        ]
    },
    package_data={'workfloweditor': [
                                     'templates/*.html',
                                     'templates/*.ini',
                                     'htdocs/css/*.css',
                                     'htdocs/images/*.*',
                                     'htdocs/js/*.js',
                                     'htdocs/js/grid/*.js',
                                     'htdocs/js/ui/*.js',
                                    ]}
)
