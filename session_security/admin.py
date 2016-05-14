from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SessionSecurityConfiguration

admin.site.register(SessionSecurityConfiguration, SingletonModelAdmin)
