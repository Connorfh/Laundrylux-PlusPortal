# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

# lss - change logo and titles ...
response.logo = A(B('Laundrylux'),XML('&reg;&nbsp;'),
                  _class="brand",_href="http://www.laundrylux.com/")
response.title = 'Laundrylux PLUS Portal'
response.subtitle = T('powered by Laundrylux')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Home'),URL('default','index')==URL(),URL('default','index'),[
        (T('Plus Location'),URL('default','plus_location_manage')==URL(),URL('default','plus_location_manage'),[]),
        (T('Plus Machine'),URL('default','plus_machine_manage')==URL(),URL('default','plus_machine_manage'),[]),
        (T('Plus SMS Log'),URL('default','plus_smslog_manage')==URL(),URL('default','plus_smslog_manage'),[]),
        (T('Plus SMS Receive'),URL('default','receivesms')==URL(),URL('default','receivesms'),[])
    ])
]

# lss - add wiki menu items to non wiki actions/views
# from gluon.tools import Wiki
#if request.function != 'wiki':
#    response.menu += Wiki(auth).menu(controller="default", function="wiki")

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (SPAN('Dev', _class='highlighted'), False, URL('admin', 'default', 'design/%s' % app), [
            (T('My Apps'), False, URL('admin', 'default', 'site')),
            (T('This App'), False, URL('admin', 'default', 'design/%s' % app), [
                (T('DB Model'), False, URL('admin', 'default', 'edit/%s/models/db.py' % app)),
                (T('Menu Model'), False, URL('admin', 'default', 'edit/%s/models/menu.py' % app)),
                (T('Controller'), False, URL('admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
                (T('View'), False, URL('admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
                (T('Layout'), False, URL('admin', 'default', 'edit/%s/views/layout.html' % app)),
                (T('Stylesheet'), False, URL('admin', 'default', 'edit/%s/static/css/web2py.css' % app)),
                (T('Errors'), False, URL('admin', 'default', 'errors/' + app)),
                (T('About'), False, URL('admin', 'default', 'about/' + app)),
                ]),
            (T('Appadmin'), False, URL('appadmin', 'index'), [
                (T('state'), False, URL('appadmin', 'state')), 
                (T('cache'), False, URL('appadmin', 'ccache')),
                ]),            
            ('web2py.com', False, 'http://www.web2py.com', [
                (T('Download'), False, 'http://www.web2py.com/examples/default/download'),
                (T('Support'), False, 'http://www.web2py.com/examples/default/support'),
                (T('Demo'), False, 'http://web2py.com/demo_admin'),
                (T('Quick Examples'), False, 'http://web2py.com/examples/default/examples'),
                (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
                (T('Videos'), False, 'http://www.web2py.com/examples/default/videos/'),
                (T('Free Applications'), False, 'http://web2py.com/appliances'),
                (T('Plugins'), False, 'http://web2py.com/plugins'),
                (T('Layouts'), False, 'http://web2py.com/layouts'),
                (T('Recipes'), False, 'http://web2pyslices.com/'),
                (T('Semantic'), False, 'http://web2py.com/semantic'),
                ]),
            (T('Documentation'), False, 'http://www.web2py.com/book', [
                (T('Preface'), False, 'http://www.web2py.com/book/default/chapter/00'),
                (T('Introduction'), False, 'http://www.web2py.com/book/default/chapter/01'),
                (T('Python'), False, 'http://www.web2py.com/book/default/chapter/02'),
                (T('Overview'), False, 'http://www.web2py.com/book/default/chapter/03'),
                (T('The Core'), False, 'http://www.web2py.com/book/default/chapter/04'),
                (T('The Views'), False, 'http://www.web2py.com/book/default/chapter/05'),
                (T('Database'), False, 'http://www.web2py.com/book/default/chapter/06'),
                (T('Forms and Validators'), False, 'http://www.web2py.com/book/default/chapter/07'),
                (T('Email and SMS'), False, 'http://www.web2py.com/book/default/chapter/08'),
                (T('Access Control'), False, 'http://www.web2py.com/book/default/chapter/09'),
                (T('Services'), False, 'http://www.web2py.com/book/default/chapter/10'),
                (T('Ajax Recipes'), False, 'http://www.web2py.com/book/default/chapter/11'),
                (T('Components and Plugins'), False, 'http://www.web2py.com/book/default/chapter/12'),
                (T('Deployment Recipes'), False, 'http://www.web2py.com/book/default/chapter/13'),
                (T('Other Recipes'), False, 'http://www.web2py.com/book/default/chapter/14'),
                (T('Buy this book'), False, 'http://stores.lulu.com/web2py'),
                ]),
            (T('Community'), False, None, [
                ('Google User Group', False, 'http://groups.google.com/group/web2py'),
                (T('Groups'), False, 'http://www.web2py.com/examples/default/usergroups'),
                (T('Twitter'), False, 'http://twitter.com/web2py'),
                (T('Live Chat'), False, 'http://webchat.freenode.net/?channels=web2py'),
                ]),
            (T('Plugins'), False, None, [
                (T('Other Plugins'), False, 'http://web2py.com/plugins'),
                (T('Layout Plugins'), False, 'http://web2py.com/layouts'),
                ])
            ])
        ]
if DEVELOPMENT_MENU: _()
