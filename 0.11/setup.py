#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
#ticket-workflow
setup(
    name = 'WorkflowEditorPlugin',
    version = '0.1',
    license = "New BSD",
    zip_safe=True,
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {
        'trac.plugins': [
            'workfloweditor.workfloweditor_admin.py = workfloweditor.workfloweditor_admin.py',
        ]
    },
    package_data={'workfloweditor': [ 'templates/*.html', 'htdocs/*.css', 'templates/*.ini']}
)
