#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
===============================
    [[Shimehari Config]]
    config
    ~~~~~~

===============================
"""

from datetime import timedelta
from shimehari.configuration import Config, ConfigManager

ConfigManager.addConfigs([
    Config('development', {
        'DEBUG': False,

        'TEST': False,

        #アプリのディレクトリ名
        'APP_DIRECTORY': 'app',

        'MAIN_SCRIPT': 'main',

        #アプリケーションinstanceの名前
        'APP_INSTANCE_NAME': 'app',

        'CONTROLLER_DIRECTORY': 'controllers',

        'VIEW_DIRECTORY': 'views',

        'ASSESTS_DIRECTORY':'assets',

        #for daiginjou
        'MODEL_DIRECTORY': 'models',

        'PREFERRED_URL_SCHEME': 'http',

        'AUTO_SETUP': True,

        'CONTROLLER_AUTO_NAMESPACE': True,

        'TEMPLATE_ENGINE': 'jinja2',

        'SECRET_KEY': '_hagedown',

        'SERVER_NAME': None,

        'PRESERVE_CONTEXT_ON_EXCEPTION': None,

        'PERMANENT_SESSION_LIFETIME': timedelta(days=31),

        'SESSION_COOKIE_NAME': 'session',

        'SESSION_COOKIE_HTTPONLY': True,

        'SESSION_COOKIE_SECURE': False,

        #キャッシュ
        'CACHE_STORE': None,

        'CACHE_DEFAULT_TIMEOUT': 300,

        'CACHE_THRESHOLD': 500,

        'CACHE_KEY_PREFIX': None,

        'CACHE_DIR': None,

        'CACHE_OPTIONS': None,

        'CACHE_ARGS': [],

        'LOG_FILE_OUTPUT': False,

        'LOG_FILE_ROTATE': False,

        'LOG_ROTATE_MAX_BITE': (5 * 1024 * 1024),

        'LOG_ROTATE_COUNT': 5,

        'LOG_FILE_DIRECTORY': 'app/log',

        'LOG_DEBUG_FORMAT': '--------------------------------------------------------------------------------\n%(levelname)s in %(module)s [%(pathname)s:%(lineno)d]:\n%(message)s\n--------------------------------------------------------------------------------',

        'LOG_OUTPUT_FORMAT': '%(asctime)s %(levelname)s in %(module)s [%(pathname)s:%(lineno)d]:\n%(message)s\n--------------------------------------------------------------------------------',


        ###application config###

        'PER_PAGE':5
    })
])