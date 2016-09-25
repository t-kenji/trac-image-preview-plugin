# -*- coding: utf-8 -*-

import os
import re

from trac.core import *
from trac.web.api import IRequestFilter
from trac.web.chrome import ITemplateProvider, \
                            add_script, add_stylesheet

class ImagePreview(Component):
    
    implements(IRequestFilter, ITemplateProvider)

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename

        return [('tracimagepreview', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return []

    # IRequestFilter methods
    
    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        if template is not None and template in ('ticket.html', 'bs_ticket.html',
                                                 'wiki_view.html', 'bs_wiki_view.html'):
            add_stylesheet(req, 'tracimagepreview/css/imagepreview.css')
            add_script(req, 'tracimagepreview/js/imagepreview.js')
        return template, data, content_type
