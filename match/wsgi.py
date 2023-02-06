"""
匹配项目的WSGI配置。

它将WSGI可调用作为名为“application”的模块级变量公开。

有关此文件的详细信息，请参阅
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'match.settings')

application = get_wsgi_application()
