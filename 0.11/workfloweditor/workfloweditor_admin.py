# -*- coding: utf-8 -*-

from trac import ticket
from trac.core import *
from trac.web.chrome import ITemplateProvider, add_stylesheet, add_script
from trac.admin import IAdminPanelProvider
from trac.web.api import ITemplateStreamFilter, IRequestHandler
from trac.web.chrome import Chrome
from genshi.filters.transform import Transformer
from genshi.template import MarkupTemplate
from api import LocaleUtil
import os

class WorkflowEditorAdmin(Component):
    implements(ITemplateProvider, ITemplateStreamFilter, IAdminPanelProvider)
    
    # ITemplateProvider method
    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('workfloweditor', resource_filename(__name__, 'htdocs'))]
    
    # ITemplateProvider method
    def get_templates_dirs(self):
        from pkg_resources import resource_filename
        return [resource_filename(__name__, 'templates')]


    # ITemplateStreamFilter method
    def filter_stream(self, req, method, filename, stream, data):    
        return stream

    # IAdminPanelProvider method
    def get_admin_panels(self, req):
        if req.perm.has_permission('TRAC_ADMIN'):
            # localization
            locale = LocaleUtil(self.env).get_locale(req)
            if locale in ['ja', 'ja-JP']:
                yield ('ticket', u'チケットシステム', 'workfloweditor', u'ワークフロー')
            else:
                yield ('ticket', 'Ticket System', 'workfloweditor', 'Workflow')

    # IAdminPanelProvider method
    def render_admin_panel(self, req, cat, page, path_info):
        req.perm.assert_permission('TRAC_ADMIN')
        add_script(req, 'workfloweditor/js/jquery.jqGrid.js')
        add_script(req, 'workfloweditor/js/grid/jqModal.js')
        add_script(req, 'workfloweditor/js/grid/jqDnR.js')
        add_script(req, 'workfloweditor/js/grid/jquery.tablednd.js')
        add_script(req, 'workfloweditor/js/ui/ui.core.js')
        add_script(req, 'workfloweditor/js/ui/ui.tabs.pack.js')
        add_script(req, 'workfloweditor/js/workfloweditor.js')
        add_stylesheet(req, 'workfloweditor/css/grid.css')
        add_stylesheet(req, 'workfloweditor/css/jqModal.css')
        add_stylesheet(req, 'workfloweditor/css/ui.tabs.css')
        add_stylesheet(req, 'workfloweditor/css/workfloweditor.css')
        
        if req.method == 'POST':
            self._update_config(req)
            
        page_param = {}
        self._create_page_param(req, page_param)
        
        # localization
        locale = LocaleUtil(self.env).get_locale(req)
        if locale in ['ja', 'ja-JP']:
            page_template = 'workfloweditor_admin_ja.html'
        else:
            page_template = 'workfloweditor_admin.html'

        return page_template, {'template': page_param}

    def _update_config(self, req):
        # get ticket-workflow section
        section = self.config._sections['ticket-workflow']
        
        # delete old data
        for (name, value) in section.options():
            self.config.remove('ticket-workflow', name)
        
        # parse input data
        input_string = req.args['workflow_config']
        config_list = input_string.split('\n')
        for config_string in config_list:
            if config_string.find('=') == -1:
                continue
            (name, value) = config_string.split('=', 1)
            # set to memory
            section.set(name.strip(), value.strip())
            
        # save to file
        self.config.save()
    
    def _create_page_param(self, req, page_param):
        # page_param['workflow_config']
        
        # sort config for display
        section = self.config._sections['ticket-workflow']
        name_list = []
        for (name, value) in section.options():
            name_list.append(name)
        name_list.sort()

        # create config data for display
        ret_val = ''
        for name in name_list:
            ret_val += name + '=' + section.get(name) + '\n'
        
        page_param['workflow_config'] = ret_val
        
        # page_param['workflow_default_config']
        
        # localization
        locale = LocaleUtil(self.env).get_locale(req)
        if locale in ['ja', 'ja-JP']:
            init_file = 'trac_jp.ini'
        else:
            init_file = 'trac.ini'
        
        # read defalut config
        template = Chrome(self.env).load_template(init_file, 'text')
        stream = template.generate()
        default_config = stream.render('text')
        
        page_param['workflow_default_config'] = default_config


class WorkflowChangeHandler(Component):
    implements(IRequestHandler)

    # IRequestHandler method
    def match_request(self, req):
        match = False
        if req.path_info == '/admin/ticket/workfloweditor/edit':
            match = True
        
        return match
    
    # IRequestHandler method
    def process_request(self, req):
        req.send_response(200)
        req.send_header('Content-Type', 'content=text/html; charset=UTF-8')
        req.end_headers()
        req.write("OK")
