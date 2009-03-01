# -*- coding: utf-8 -*-

from os import environ

class LocaleUtil:
    
    def get_locale(self, req):
        """Get client locale from the http request."""
        
        locale = None
        locale_array = None
        
        if req.environ.has_key('HTTP_ACCEPT_LANGUAGE'):
            locale_array = req.environ['HTTP_ACCEPT_LANGUAGE'].split(",")
        
        if (len(locale_array) > 0):
            locale = locale_array[0].strip()
        
        if (len(locale) > 2):
            locale = locale[0:2];
        
        return locale
