from django.db import models
from solo.models import SingletonModel


class SessionSecurityConfiguration(SingletonModel):
    expire_after = models.IntegerField(
        verbose_name='Logout after',
        help_text='Logout after inactivity, seconds',
        default=600
    )
    warn_after = models.IntegerField(
        verbose_name='Warn after',
        help_text='Warn user about inactivity, seconds',
        default=540)

    def __unicode__(self):
        return u"Session Security Configuration"

    class Meta:
        verbose_name = "Session Security Configuration"
