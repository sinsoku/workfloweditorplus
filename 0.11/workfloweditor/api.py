# -*- coding: utf-8 -*-

from os import environ
from trac.core import Component

class LocaleUtil(Component):
    
    def get_locale(self, req):
        """Get client locale from the http request.
        """
        
        locale = None
        locale_array = req.environ['HTTP_ACCEPT_LANGUAGE'].split(",")
        if (len(locale_array) > 0):
            locale = locale_array[0].strip()
            
        return locale
